import time
import openai
import ast
from datetime import datetime, timedelta
from pymongo.errors import DuplicateKeyError
from statistics import mean
import class_channel as c
import class_message as m

class Group:
    def __init__(self):
        self.channels              = set()
        self.number_requests_c     = 0
        self.total_time_requests_c = 0
        self.number_requests_a     = 0
        self.total_time_requests_a = 0

    async def new_message_handler(self, event, prompt_c, prompt_a, model_c, model_a, temperature, max_tokens, how_many_hours_verification, collection_messages, collection_channels_id, collection_channels_score, collection_channels_similarity):
        message = m.Message(event.message.id, event.message.text, event.message.date, event.chat_id)
        print ("server1 has received the message :" + str(event.message.text))

        self.channels.append(event.chat_id)
        try:
            collection_channels_id.insert_one({"telegram_id": event.chat_id}) # TypeError: object InsertOneResult can't be used in 'await' expression
        except DuplicateKeyError:
            pass
        print("server1 listens to the channels " + str(self.channels))

        await message.calc_score(prompt_c, model_c, temperature, max_tokens, collection_messages, self)
        await message.calc_affirmations(prompt_a, model_a, temperature, max_tokens, collection_messages, self)
        if len(message.text) == 0:
            return
        message.put_to_mongo(collection_messages)
        await self.update_channels_score(message, collection_messages, collection_channels_score)
        await self.update_channels_similarity(message, collection_messages, collection_channels_similarity, how_many_hours_verification)
        # free(message) ?

    async def update_channels_from_mongo(self, collection_channels_id):
        channels = collection_channels_id.find({}, {})
        self.channels = [channel['telegram_id'] for channel in channels]
        print("server1 listens to the channels " + str(self.channels))

    async def update_channels_score(self, new_message, collection_messages, collection_channels_score):
        try:
            messages_this_channel = collection_messages.find({"channel": new_message.channel})
            print (f"messages_of_this_channel = {str(messages_this_channel)}")
            list_scores_this_channel = [msg["score"] for msg in messages_this_channel]
            print (f"scores_of_this_channel = {str(list_scores_this_channel)}")
            new_average = mean(list_scores_this_channel) if (len(list_scores_this_channel) >0) else 0
            print (f"new_average = {sum(list_scores_this_channel)} / {len(list_scores_this_channel)} = {new_average}")
            existing_record = collection_channels_score.find_one({"telegram_id": new_message.channel}) #
            if existing_record:
                collection_channels_score.update_one(
                    {"telegram_id": new_message.channel},
                    {"$set": {"average_score": new_average}}
                )
                print(f"Updated average score for channel {new_message.channel} to {new_average}")
            else:
                collection_channels_score.insert_one({
                    "telegram_id": new_message.channel,
                    "average_score": new_average,
                    # {"$set": {"average_score": new_average}} # ?
                })
                print(f"Updated average score for channel {new_message.channel} to {new_average}")
        except TypeError as e:
            print(f"Failed to insert record due to TypeError: {e}")
        except DuplicateKeyError: # как эта ошибка может возникнуть
            print(f"Failed to insert record due to duplicate _id.") # telegram_id = key ?

    async def update_channels_similarity(self, message, collection_messages, collection_channels_similarity, how_many_hours_verification):

        recent_messages = list(collection_messages.find({}))
        # timestamp_boundary = (datetime.now() - timedelta(hours=how_many_hours_verification)) * 1000
        #recent_messages = list(collection_messages.find({"timestamp.$date.$numberLong": {"$gte": str(timestamp_boundary)}})) ####

        for old_message in recent_messages:
            if message.channel != old_message["channel"]:
                score = 0
                for affirmation, truth_value in ast.literal_eval(message.affirmations).items():
                    if affirmation in old_message["affirmations"]:
                        if old_message["affirmations"][affirmation] == truth_value:
                              score += 1
                        else:
                              score -= 1
                two_channels = sorted([message.channel, old_message["channel"]])
                existing_record = collection_channels_similarity.find_one({
                    "channel_a": two_channels[0],
                    "channel_b": two_channels[1]
                })
                if existing_record:
                    new_score = existing_record["relation"] + score
                    collection_channels_similarity.update_one(
                        {"_id": existing_record["_id"]},
                        {"$set": {"relation": new_score}}
                    )
                else:
                    collection_channels_similarity.insert_one({
                        "channel_a": two_channels[0],
                        "channel_b": two_channels[1],
                        "relation": score
                    })
                print(f"collection channels_similarity updated")


####################################################### ARCHIVE, MAY BE TO USE LATER
    def score(self, promptC):
        if len(self.channels) == 0:
            return (int(0))
        score = 0
        for channel in self.channels:
            score += channel.score(promptC)
        return round (score / len(self.channels))

    def score_list(self, promptC):
        if (len(self.channels) == 0): 
            return (int(0))
        score_list = []
        for i in range(len(promptC.characteristics)):
            score_list.append(0)
            nb_channels = 0
            for channel in self.channels:
                p = channel.score_list(promptC)
                try:
                    score_list[i] += p[i]
                    nb_channels += 1
                except TypeError:
                    pass
            score_list[i] = round(score_list[i] / nb_channels, 1)
        return score_list

    async def calc_similarities_via_openai(self, model, temperature, promptS):
        print ("*********************************************************\n")
        time_start = time.time()
        nb_requests = 0
        self.similarities = []
        for ch1 in self.channels:
            self.similarities.append([])
            for ch2 in self.channels:
                if self.channels.index(ch1) < self.channels.index(ch2):
                    print (f" dist ai  {ch1.name.ljust(32)} {ch2.name.ljust(32)} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ...")
                    self.similarities[self.channels.index(ch1)].append(0)
                    for m1 in ch1.messages:
                        for m2 in ch2.messages:
                            # retries = 5
                            # while retries > 0:
                            # try:
                                # в промт резюме а не целое сообщение ?
                            response = openai.ChatCompletion.create(
                                model             = model,
                                max_tokens        = 10, # ?
                                temperature       = temperature,
                                request_timeout   = 30,
                                top_p             = 0.1,
                                frequency_penalty = 0.1,
                                presence_penalty  = 0.1,
                                stop              = None,
                                messages          = [{"role": "user", "content": promptS.to_string(m1, m2)}]
                            )
                            if int(response['choices'][0]['message']['content'].strip()) == 1:
                                self.similarities[self.channels.index(ch1)][self.channels.index(ch2)] += 1
                            nb_requests += 1
                            if (model == "gpt-4"):
                                time.sleep(15) # ?
                            if (model == "gpt-3.5-turbo"):
                                time.sleep(10)
                        # except (ValueError):
                        #     break
                        # except (openai.error.RateLimitError, openai.error.ServiceUnavailableError, openai.error.APIError, openai.error.Timeout, requests.exceptions.ReadTimeout, socket.timeout) as e:
                        #     if e: 
                        #         print(e)
                        #         print('Timeout error, retrying...')
                        #         retries -= 1
                        #         time.sleep(5)
                        #     else:
                        #         raise e
        self.speed_promptS = round(nb_requests / ((time.time() - int(time_start)) / 60.))
        print ()	

    def similarities_to_string(self):
        string = "similarities:\n    "
        for i in range(len(self.channels) - 1):
            string += str(i).rjust(3) + " "
        string += "\n"
        for channel in self.channels:
            string += "-----"
        string += "\n"
        for x in range(len(self.similarities)):
            string += str(len(x)).rjust(2) + "| "
            for y in range(len(self.similarities[x])):
                string += str(round(self.similarities[x][y], 2)).rjust(3) + " "
            string += "\n"
        return string

    def time_weight(m1, m2): # timezone ###
        time_difference = abs(m1.date - m2.date)
        return 1 + (1 / (1 + time_difference.total_seconds() / 3600))

    def calc_similarities_via_affirmations(self, coll_msgs_affirmations, collection_channels_similarities):
        self.similarities = []
        for ch1 in self.channels:
            self.similarities.append([])
            for ch2 in self.channels:
                self.similarities[self.channels.index(ch1)].append(0)
        for ch1 in self.channels:
            for m1 in list(coll_msgs_affirmations.find({'channel' : ch1.name})): ##
                for a1 in m1.affirmations: ##
                    for ch2 in self.channels:
                        if self.channels.index(ch1) < self.channels.index(ch2):
                            for m2 in list(coll_msgs_affirmations.find({'channel' : ch2.name})): ##
                                for a2 in m2.affirmations: ##
                                    if a1['affirmation'] == a2['affirmation'] and a1['truthValue'] == a2['truthValue']:
                                        self.similarities[self.channels.index(ch1)][self.channels.index(ch2)] += self.time_weight(m1, m2)
                                    elif a1['affirmation'] == a2['affirmation'] and a1['truthValue'] != a2['truthValue']:
                                        self.similarities[self.channels.index(ch1)][self.channels.index(ch2)] -= self.time_weight(m1, m2)
        collection_channels_similarities.delete_many({}) ##
        for ch1 in self.channels:
            for ch2 in self.channels:
                collection_channels_similarities.insert_one({"ch1":ch1.name, "ch2":ch2.name, "similarity":self.similarities[self.channels.index(ch1)][self.channels.index(ch2)]})

    # def new_message_handler(self, new_message, coll_msgs_affirmations, coll_similarities):
    #     for m1 in list(coll_msgs_affirmations.find({'channel' : ch1.name})): ##
    #     all_msgs_affirmations = list(coll_msgs_affirmations.find({}))
    #     for channel in self.channels:
    #         for message in channel.messages:
    #             for a1 in message.affirmations: ##
    #                 for a2 in m2.affirmations: ##
    #                     if a1['affirmation'] == a2['affirmation'] and a1['truthValue'] == a2['truthValue']:
    #                         self.similarities[self.channels.index(channel)][self.channels.index(ch2)] += self.time_weight(message, m2)
    #                     elif a1['affirmation'] == a2['affirmation'] and a1['truthValue'] != a2['truthValue']:
    #                         self.similarities[self.channels.index(channel)][self.channels.index(ch2)] -= self.time_weight(message, m2)

    #     for old_msg in all_msgs_affirmations:
    #         key = f"{new_msg['channelID']}_{old_msg['channelID']}" # их порядок
    #         if key not in similarities:
    #             similarities[key] = 0

    #         time_difference = new_message.timestamp - old_msg.timestamp
    #         time_weight = 1 + (1 / (1 + time_difference.total_seconds() / 3600)) 

    #         if new_message['binaryAffirmation'] == old_msg['binaryAffirmation'] and new_message['truthValue'] == old_msg['truthValue']:
    #             similarities[key] += time_weight
    #         elif new_message['binaryAffirmation'] == old_msg['binaryAffirmation'] and new_message['truthValue'] != old_msg['truthValue']:
    #             similarities[key] -= time_weight

    def number_per_minute_promptC(self):
        return round((self.total_time_requests_c / (60 * self.number_requests_c )))

    def number_per_minute_promptA(self):
        return round((self.total_time_requests_a / (60 * self.number_requests_a )))

    def score_to_string(self, promptC):
        if (len(self.channels) == 0):
            return ("SET *****************************************************")
        string = f"SET ***************************************************** {self.score(promptC)}\n"
        for channel in self.channels:
            string += f"{channel.name.ljust(32)} {channel.score(promptC)}/100\n"
        for i in range(len(promptC.characteristics)):
            string += f"{str(i + 1).rjust(5)} "
        string += "\n"
        for i in range(len(promptC.characteristics)):
            string = string + "------"
        string += "\n"
        for score in self.score_list(promptC):
            string += str(score).rjust(5) + " "
        string += "\n\n"
        for channel in self.channels:
            string += channel.score_to_string_full(promptC)
        return (string)

    def messages_to_string(self):
        string = "*********************************************************\n"
        for channel in self.channels:
            string += channel.messages_to_string()
        return (string)

    # def log_to_mongo(coll_log): #
    #     if (log_to_mongo == 1):
    #         coll_log.insert_one({
    #             "_id"                    : str(uuid.uuid4()),
    #             "live_mode"              : str(live_mode),
    #             "model"                  : str(model),
    #             "temperature"            : str(temperature),
    #             "nb_messages"            : str(nb_messages),
    #             "nb_messages_par_minute" : str(nb_messages_par_minute),
    #             "set1"                   : { str(i) : channel.name for i, channel in enumerate(set1.channels) },
    #             "set2"                   : { str(i) : channel.name for i, channel in enumerate(set2.channels) },
    #             "set1 score"             : str(set1.average_score()),
    #             "set2 score"             : str(set2.average_score()),
    #             "log_file"               : log_file,
    #         })

    async def read_messages(self, nb_messages, client_tg):
        for channel in self.channels:
            await channel.read_messages(nb_messages, client_tg)

    async def calc_score(self, promptC, model, temperature, max_tokens): # (coll_log, log_file, log_to_mongo):
        time_start = time.time()
        for channel in self.channels:
            print (f"calculating score  {channel.name.ljust(32)} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ...")
            await channel.calc_score(promptC, model, temperature, max_tokens)
        self.total_time_requests_c += channel.seconds_promptC
        self.number_requests_c += channel.number_promptC
        print ()

    async def calc_affirmations(self, promptA, model, temperature, max_tokens, coll_msgs_affirmations):
        time_start = time.time()
        for channel in self.channels:
            print (f"calculating affirm {channel.name.ljust(32)} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ...")
            channel.calc_affirmations(promptA, model, temperature, max_tokens, coll_msgs_affirmations) # await
            self.total_time_requests_a += channel.seconds_promptA
            self.number_requests_a += channel.number_promptA
        self.speed_promptA = round(len(self.channels[0].messages) * len(self.channels) / ((time.time() - int(time_start)) / 60.))
        print ()


