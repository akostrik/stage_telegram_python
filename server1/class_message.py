import openai
import time # The only exception are modules in the Python Standard Library, which is a collection of modules (e.g. time , random , os ) that are built into Python
import requests
from pymongo.errors import DuplicateKeyError
import ast # ast is part of the standard library of python, you don't need to install it separately
from datetime import datetime

class Message:
    def __init__(self, telegram_id, text, timestamp, channel):
        self.telegram_id  = telegram_id
        self.text         = text
        self.timestamp    = timestamp
        self.channel      = channel
        self.affirmations = []
        self.score        = []

    def __str__(self):
        return f"Message(ID: {self.telegram_id}, Text: {self.text}, Timestamp: {self.timestamp}, Channel: {self.channel})"

    async def calc_score(self, prompt_c, model_c, temperature, max_tokens, collection_messages, group):
        try:
            time_start = time.time()
            # print ("\n" + datetime.now().strftime("%S:%M:%Hh %d/%m/%Y") + " OpenAI request: " + prompt_c.to_string(self, collection_messages))
            response = openai.ChatCompletion.create(
                model           = model_c,
                max_tokens      = max_tokens,
                temperature     = temperature,
                messages        = [{"role": "user", "content": prompt_c.to_string(self, collection_messages)}]
            )
            group.total_time_requests_c += time.time() - int(time_start)
            group.total_time_requests_c += 1
            response_as_text = response['choices'][0]['message']['content'].split("\n")
            print ("\nOpenAI response: " + str(response_as_text) + "\n")
            for i in range(len(prompt_c.characteristics)):
                try:
                    response_to_characteristic = int(response_as_text[i].split(". ")[1])
                except (IndexError, ValueError):
                    response_to_characteristic = int(0)
                self.score.append(response_to_characteristic)
        except (openai.error.Timeout, requests.exceptions.ReadTimeout, openai.error.ServiceUnavailableError, openai.error.APIError):
            print('openai error when calculating score')
            pass # retry ?

    async def calc_affirmations(self, prompt_a, model_a, temperature, max_tokens, collection_messages, group):
        try:
            time_start = time.time()
            response = openai.ChatCompletion.create( # await ?
                model       = model_a,
                max_tokens  = max_tokens,
                temperature = temperature,
                messages    = [{"role": "user", "content": prompt_a.to_string(self, collection_messages)}]
            )
            group.total_time_requests_a += time.time() - int(time_start)
            group.total_time_requests_a += 1
            self.affirmations = response['choices'][0]['message']['content'].replace('true', 'True').replace('false', 'False')
        except (openai.error.Timeout, requests.exceptions.ReadTimeout, openai.error.ServiceUnavailableError, openai.error.APIError):
            print('openai error when calculating affirmations')
            pass

    def put_to_mongo(self, collection_messages): # do not put async
        collection_messages.delete_many({}) ################## TMP
        existing_record = collection_messages.find_one({"telegram_id": self.telegram_id, "channel": self.channel}) # no need telegram_id is key
        if existing_record:
            print(f"Record with telegram_id {self.telegram_id} already exists in the database.")
            return
        try:
          print ("affirmations : " + str(self.affirmations))
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
          print("Put message to mongo successful.")
        except TypeError as e:
            print(f"Failed to insert record due to TypeError: {e}")
        except DuplicateKeyError:
            pass
        except Exception as e:
            print(f"Failed to insert record {e}")


####################################################### ARCHIVE, MAY BE TO USE LATER
    def to_string(self, channel_name): # __str__
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

    def get_score(self):
        return sum(self.score)