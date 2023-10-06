import uuid
import openai
import time
import requests
from pymongo.errors import DuplicateKeyError
import ast
from datetime import datetime, timedelta


class Message:
    def __init__(self, telegram_id, text, timestamp, channel):
        self.telegram_id        = telegram_id
        self.text               = text
        self.timestamp          = timestamp
        self.channel            = channel
        self.affirmations       = []
        self.score              = []
    
    def __str__(self):
        return f"Message(ID: {self.telegram_id}, Text: {self.text}, Timestamp: {self.timestamp}, Channel: {self.channel})"

 
    async def calc_score(self, prompt_c, model, temperature, max_tokens, request_timeout, collection_messages, group):
        try:
            time_start = time.time()
            response = openai.ChatCompletion.create(
                model           = model,
                max_tokens      = max_tokens,
                temperature     = temperature,
                request_timeout = request_timeout,
                messages        = [{"role": "user", "content": prompt_c.to_string(self, collection_messages)}]
            )
            group.seconds_prompt_c += time.time() - int(time_start)
            group.number_prompt_c += 1
            response_as_text = response['choices'][0]['message']['content'].split("\n")

            for i in range(len(prompt_c.characteristics)):
                try:
                    response_to_characteristic = int(response_as_text[i].split(". ")[1])
                except (IndexError, ValueError):
                    response_to_characteristic = int(0)
                self.score.append(response_to_characteristic)
        except (openai.error.Timeout, requests.exceptions.ReadTimeout, openai.error.ServiceUnavailableError, openai.error.APIError):
            print('openai error when calculating score')
            pass # ? retry ?

    async def calc_affirmations(self, prompt_a, model, temperature, max_tokens, request_timeout, collection_messages, group):
        time_start = time.time()
        response = openai.ChatCompletion.create( # await ?
            model       = model,
            max_tokens  = max_tokens,
            temperature = temperature,
            # request_timeout = request_timeout,
            messages    = [{"role": "user", "content": prompt_a.to_string(self, collection_messages)}]
        )
        group.seconds_prompt_a += time.time() - int(time_start)
        group.number_prompt_a += 1
        self.affirmations = response['choices'][0]['message']['content'].replace('true', 'True').replace('false', 'False')
        # except (openai.error.Timeout, requests.exceptions.ReadTimeout, openai.error.ServiceUnavailableError, openai.error.APIError):
        #с     pass # ?

    async def put_to_mongo(self, prompt_c, prompt_a, collection_messages, collection_channels, collection_relations):
        # Check if a record with the given telegram_id exists
        def get_messages_last_10_hours(collection_messages):
            ten_hours_ago = datetime.now() - timedelta(hours=10)
            timestamp_boundary = ten_hours_ago.timestamp() * 1000
            return list(collection_messages.find({}))
            #return list(collection_messages.find({"timestamp.$date.$numberLong": {"$gte": str(timestamp_boundary)}}))

        def compare_affirmations(new_affirmations, old_message):
            score = 0
            for affirmation, truth_value in new_affirmations.items():
                if affirmation in old_message["affirmations"]:
                    if old_message["affirmations"][affirmation] == truth_value:
                        score += 1
                    else:
                        score -= 1
            return score
        
        existing_record = collection_messages.find_one({"telegram_id": self.telegram_id, "channel": self.channel})
        if existing_record:
            print(f"Record with telegram_id {self.telegram_id} already exists.")
            return    

        if len(self.text) > 0:
            try:

                # here we update average score for the channel

                cursor = collection_messages.find({"channel": self.channel})
                all_scores = [doc["score"] for doc in cursor]
                all_scores.append(sum(self.score))
                new_average = sum(all_scores) / len(all_scores)
                collection_channels.update_one(
                    {"channel": self.channel},
                    {"$set": {"average_score": new_average}}
                )

                print(f"Updated average score for channel {self.channel} to {new_average}")

                collection_messages.insert_one({
                    "telegram_id": self.telegram_id,
                    "text": self.text,
                    "timestamp": self.timestamp,
                    "channel": self.channel,
                    
                    "score": sum(self.score),

                    "score_list": self.score,
                    "score_list_corrections": self.score,
                    "score_list_explanations": {},

                    "affirmations": ast.literal_eval(self.affirmations),
                    "affirmations_corrections": ast.literal_eval(self.affirmations),

                    "to_use_c": False,
                    "to_use_a": False,

                })

                print("Put to mongo successful.")

                #here we compare affirmations with each other
                messages_last_10_hours = get_messages_last_10_hours(collection_messages)
                for old_message in messages_last_10_hours:
                    if self.channel != old_message["channel"]:
                        score = compare_affirmations(ast.literal_eval(self.affirmations), old_message)
                        channels = sorted([self.channel, old_message["channel"]])
                        
                        # Check if relation already exists
                        existing_relation = collection_relations.find_one({
                            "channel_a": channels[0],
                            "channel_b": channels[1]
                        })
                        
                        if existing_relation:
                            # Update the existing relation's score
                            new_score = existing_relation["relation"] + score
                            collection_relations.update_one(
                                {"_id": existing_relation["_id"]},
                                {"$set": {"relation": new_score}}
                            )
                        else:
                            # Insert a new relation
                            relation = {
                                "channel_a": channels[0],
                                "channel_b": channels[1],
                                "relation": score
                            }
                            collection_relations.insert_one(relation)

            
            except TypeError as e:
                print(f"Failed to insert record due to TypeError: {e}")

            except DuplicateKeyError:
                print(f"Failed to insert record due to duplicate _id.")

############################################### NOT USED
    def to_string(self, channel_name):
        string = ""
        string += f"{channel_name.upper()}\n"
        if len(self.score) > 0:
            i = 1
            for score_characteristic in self.score:
                string += f"{str(i).rjust(5)} "
                i += 1
            string += "\n"
            for score_characteristic in self.score:
                string += f"{str(score_characteristic).rjust(5)} "
        return string + f"\n{self.text}\n"

    def score(self):
        return sum(self.score)