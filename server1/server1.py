import os       # module in the Python Standard Library, built into Python
import sys      # --
import openai
import pymongo
from   dotenv   import load_dotenv
from   telethon import TelegramClient, events
from   pymongo  import MongoClient
from   datetime import datetime
import classes_prompts as p
import class_group     as g

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

path_log                       = "server1/log"
try:
    os.mkdir(path_log)
except FileExistsError:
    pass

load_dotenv()
openai.api_key                = os.getenv("OPENAI")
api_id                        = os.getenv("API_ID")
api_hash                      = os.getenv("API_HASH")
client_mongo                  = MongoClient(os.getenv("MONGO"))
client_tg                     = TelegramClient('anon', api_id, api_hash)
client_tg.start()

db                            = client_mongo['telegram']
collection_characteristics    = db['characteristics']
collection_messages           = db['messages']
collection_channels_id        = db['channels_id']
collection_channels_score     = db['channels_score']
collection_channels_simiarity = db['channels_similarity']
try:
    collection_messages.create_index([('telegram_id', pymongo.ASCENDING)], unique=True)
    collection_channels_id.create_index([('telegram_id', pymongo.ASCENDING)], unique=True) #telegram_id
    #collection_channels_score.create_index([('telegram_id', pymongo.ASCENDING)], unique=True) #telegram_idf
except pymongo.errors.ServerSelectionTimeoutError:
    print("Have you added this IP addresse in your MongoDB account?")
#collection_log               = db['log']
model_c                       = "gpt-3.5-turbo"
model_a                       = "gpt-4"
temperature                   = 0.2 #0.73, # 1
max_tokens                    = 2000
max_len_telegram_message      = 600
request_timeout               = 10
how_many_hours_verification   = 0.016 # 10
prompt_c                      = p.Prompt_c(max_len_telegram_message, collection_characteristics)
prompt_a                      = p.Prompt_a(max_len_telegram_message)
log_file                      = path_log + "/log_" + datetime.now().strftime("%Y_%m_%d_%Hh%M_%S") + ".txt"
sys.stdout                    = LoggerStdout(log_file)
sys.stderr                    = LoggerStderr(log_file)
sys.stdout.flush()
sys.stderr.flush()
group_channels                = g.Group()


print("openai model for propaganda marks = " + str(model_a))
print("openai model for affirmations     = " + str(model_c))
print("temperature                       = " + str(temperature))
print("max_len_telegram_message          = " + str(max_len_telegram_message))
print("verification of the messages for the last " + str(how_many_hours_verification) + " hours")
print()
print (prompt_c.characteristics_to_string())

@client_tg.on(events.NewMessage())
async def new_message_handler(event):
    await group_channels.update_channels_from_mongo(collection_channels_id)
    if event.chat_id in group_channels.channels:
        await group_channels.new_message_handler(event, prompt_c, prompt_a, model_c, model_a,temperature, max_tokens, how_many_hours_verification, collection_messages, collection_channels_id, collection_channels_score, collection_channels_simiarity)


with client_tg:
    client_tg.run_until_disconnected()


    #await group_channels.calc_score(promptC, model, temperature, max_tokens)
    #await group_channels.calc_affirmations(promptA, model, temperature, max_tokens)
    #await group_channels.calc_distances_openai(model, temperature, promptS)
    #await group_channels.calc_similarities_via_affirmations(model, temperature, promptS)
    # print ("request openai characteristics " + group_channels.number_per_minute_promptA() + " messages per minute")
    # print ("request openai affirmations    " + group_channels.number_per_minute_promptA() + " messages per minute")
    # print (group_channels.score_to_string(promptC))
    # print (group_channels.similarities_to_string())
    # print (group_channels.messages_to_string())

