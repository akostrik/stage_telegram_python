import telethon
from telethon.tl.functions.messages import GetHistoryRequest
import class_message as m

####################################################### NOT USED
class Channel:
    def __init__(self, name):
        self.name            = name
        self.messages        = []
        # self.affirmations    = []
        self.number_promptC  = 0
        self.seconds_promptC = 0
        self.number_promptA  = 0
        self.seconds_promptA = 0

    async def calc_score(self, promptC, model, temperature, max_tokens, coll_msgs):
        # try:
        for message in self.messages:
            message.calc_score(promptC, model, temperature, max_tokens, coll_msgs) # await
        self.seconds_promptC += message.seconds_promptC
        self.number_promptC += 1
        # except (ValueError):
        #     pass

    async def calc_affirmations(self, promptA, model, temperature, max_tokens, coll_msgs_affirmations):
        for message in self.messages:
            message.calc_affirmations(promptA, model, temperature, max_tokens, coll_msgs_affirmations) # await
            self.seconds_promptA += message.seconds_promptA
            self.number_promptA += 1

    def score(self, promptC): # normalized  [0 ... 100]
        if len(self.messages) == 0:
            return (int(0))
        score_msg_max = 0
        score_msg_min = 0
        for characteristic in promptC.characteristics:
            score_msg_max += characteristic.score if (characteristic.score > 0) else 0
            score_msg_min += characteristic.score if (characteristic.score < 0) else 0
        score_channel_max = score_msg_max * len(self.messages)
        score_channel_min = score_msg_min * len(self.messages)
        score_channel = 0
        for message in self.messages:
            score_channel += message.score()
        try:
            return round ((score_channel - score_channel_min) * 100 / (score_channel_max - score_channel_min))
        except ZeroDivisionError:
            return round(score_channel)

    def score_list(self, promptC):
        if len(self.messages) == 0:
            return (int(0))
        score_list = []
        for i in range(len(promptC.characteristics)):
            score_message = 0
            for message in self.messages:
                try:
                    score_message += message.score_lst[i]
                except IndexError:
                    pass
            score_list.append(score_message)
        for i in range(len(promptC.characteristics)):
            score_list[i] = round (score_list[i] / len(self.messages), 1)
        return score_list

    def messages_to_string(self):
        if len(self.messages) == 0:
            return ("")
        string = ""
        i = 1
        for message in self.messages:
            string += "MESSAGE " + str(i) + " " + message.to_string(self.name) + "\n"
            i = i + 1
        return string

    def score_to_string_full(self, promptC):
        if len(self.messages) == 0:
            return ("")
        try:
            string = f"{self.name.upper()} {self.score(promptC)}/100 :\n"
            for i in range(len(promptC.characteristics)):
                string += f"{str(i).rjust(5)} "
            string += "\n"
            for i in range(len(promptC.characteristics)):
                string += "------"
            string += "\n"
            for message in self.messages:
                for score_characteristic in message.score_lst:
                    string += f"{str(score_characteristic).rjust(5)} "
                string += "\n"
            for i in range(len(promptC.characteristics)):
                string += "------"
            string += "\n" + self.average_scores_par_characteristic_to_string(promptC)
            return string + "\n"
        except IndexError:
            return ""

    def average_scores_par_characteristic_to_string(self, promptC):
        if len(self.messages) == 0:
            return ("")
        string = ""
        for score in self.score_list(promptC):
            string += str(score).rjust(5) + " "
        return (string + "\n")

    async def read_messages(self, nb_messages, client_tg):
        try:
            await client_tg.get_entity(self.name)
            messages_json = await client_tg(GetHistoryRequest(
                peer=self.name,
                limit=nb_messages,
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))
            for message_json in messages_json.messages:
                message = m.Message(message_json.message, message_json.date, self.name)
                self.messages.append(message)
        except (ValueError, telethon.errors.rpcerrorlist.UsernameInvalidError):
            pass
