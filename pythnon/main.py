import sys
import openai
import os
from telethon import TelegramClient, events
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
from datetime import datetime
import classes_prompts as p
import class_group     as g
import test_data

class LoggerStdout:
    def __init__(self, filename):
        self.my_stdout = sys.stdout
        self.file = open(filename, 'a')
 
    def write(self, message):
        self.my_stdout.write(message)
        self.file.write(message)

    def flush(self):
        self.my_stdout.flush()
        self.file.flush()

class LoggerStderr:
    def __init__(self, filename):
        self.my_stderr = sys.stderr
        self.file = open(filename, 'a')
 
    def write(self, message):
        self.my_stderr.write(message)
        self.file.write(message)

    def flush(self):
        self.my_stderr.flush()
        self.file.flush()

load_dotenv()
openai.api_key                 = os.getenv("OPENAI")
api_id                         = os.getenv("API_ID")
api_hash                       = os.getenv("API_HASH")
client_mongo                   = MongoClient(os.getenv("MONGO"))
client_tg                      = TelegramClient('anon', api_id, api_hash)
client_tg.start()

path_log                       = "log"
try:
    os.mkdir(path_log)
except FileExistsError:
    pass

db                            = client_mongo['telegram']
collection_characteristics    = db['characteristics']       #           mongo
collection_messages           = db['messages']              #           mongo
#collection_similarities       = db['similarities']          # local and mongo
collection_channels           = db['channels']
collection_relations          = db['relations']
collectio_log                 = db['log']                   # files and mongo
model                         = "gpt-4"
#model                        = "gpt-4"
temperature                   = 0.2 #0.73, # 1
max_tokens                    = 2000 #
#nb_messages                   = 8 #
request_timeout               = 10 # ?
max_len_message               = 600 #
#live_mode                     = 0 # LIVE = 1, FIXED_MESSAGES = 0
log_to_mongo                  = 0 #
promptC                       = p.Prompt_c(max_len_message, collection_characteristics) # model temperature max_tokens
promptA                       = p.Prompt_a(max_len_message)
log_file                      = path_log + "/log_" + datetime.now().strftime("%Y_%m_%d_%Hh%M_%S") + ".txt"
sys.stdout                    = LoggerStdout(log_file)
sys.stderr                    = LoggerStderr(log_file)
sys.stdout.flush()
sys.stderr.flush()
#channels_nammes               = [-1001842901217, -1001905441409, -1001863996867, -1001944316671, -1001919265899]
group                         = g.Group()

# if live_mode == 0:
#     group = test_data.group1
# else:
#     group = g.Group(test_data.channels_names1 + test_data.channels_names2)
#     await group.read_messages(nb_messages, client_tg)

print("model           = " + str(model))
print("temperature     = " + str(temperature))
print("max_len_message = " + str(max_len_message))
#print("channels        = " + str(channels_nammes))
print()
# print (promptC.characteristics_to_string())

def get_channel_names_from_db():
    channels = collection_channels.find({}, {})
    return [channel['channelId'] for channel in channels]

@client_tg.on(events.NewMessage())
async def new_message_handler(event):
    channels_names = get_channel_names_from_db()  # Fetch the channels list each time
    print(channels_names)
    if event.chat_id in channels_names:
        await group.new_message_handler(event, promptC, promptA, model, temperature, max_tokens, request_timeout, collection_messages, collection_channels, collection_relations)

    #await group.calc_score(promptC, model, temperature, max_tokens)
    #await group.calc_affirmations(promptA, model, temperature, max_tokens)
    #await group.calc_distances_openai(model, temperature, promptS)
    #await group.calc_similarities_via_affirmations(model, temperature, promptS)

    # print ("request openai characteristics " + group.number_per_minute_promptA() + " messages per minute")
    # print ("request openai affirmations    " + group.number_per_minute_promptA() + " messages per minute")
    # print (group.score_to_string(promptC))
    # print (group.similarities_to_string())
    # print (group.messages_to_string())



with client_tg:
    client_tg.run_until_disconnected()