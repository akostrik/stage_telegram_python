# 10 21
# Append the fetched records to the prompt
    for example in examples:
        prompt += f"\n\nMessage: {example['message']}"
        prompt += f"\nAffirmations: {example['affirmations']}"
        prompt += f"\nCorrected Affirmations: {example['corrected_affirmations']}"

    print(prompt)

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        max_tokens=2000,
        temperature=0.1,
        messages=messages
    )
    
    content = response['choices'][0]['message']['content']
    content = content.replace('true', 'True').replace('false', 'False')
    # The content should already be in the expected format
    print(content)
    try:
        affirmation_list = eval(content) # Use eval to parse the content

        affirmation_document = {
            "message": message,
            "affirmations": affirmation_list,
            "corrected_affirmations": affirmation_list,  # As per your request, corrected is same as bot's reply for now
            "toUse": False,  # Default value
            "timestamp": datetime.utcnow()  # Using datetime module to get current UTC timestamp
        }

        # Insert the document into the affirmations collection
        affirmations.insert_one(affirmation_document)

        #print(affirmation_list)
        return affirmation_list
    except Exception as e:
        print(f"Error parsing content: {e}")
        return []

# Function to compare messages and update graph
def compare_messages(new_msg):
    all_messages = list(collection.find({}))

    for old_msg in all_messages:
        key = f"{new_msg['channelID']}_{old_msg['channelID']}"
        #print(channel_connections)
        if key not in channel_connections:
            channel_connections[key] = 0

        time_difference = new_msg['timestamp'] - old_msg['timestamp']
        time_weight = 1 + (1 / (1 + time_difference.total_seconds() / 3600)) 

        if new_msg['binaryAffirmation'] == old_msg['binaryAffirmation'] and new_msg['truthValue'] == old_msg['truthValue']:
            channel_connections[key] += time_weight
        elif new_msg['binaryAffirmation'] == old_msg['binaryAffirmation'] and new_msg['truthValue'] != old_msg['truthValue']:
            channel_connections[key] -= time_weight

# Subscribe to channels
@client.on(events.NewMessage(chats=[-1001842901217, -1001905441409, -1001863996867, -1001944316671, -1001919265899]))
async def new_message_handler(event):
    message = event.message.text
    channel = event.chat_id
    timestamp = event.message.date
    binary_affirmations = get_binary_affirmation(message)
    #print(binary_affirmations)

    for affirmation, truth_value in binary_affirmations.items():
        new_msg = {
            'channelID': channel,
            'binaryAffirmation': affirmation,
            'truthValue': truth_value, 
            'timestamp': timestamp  # Store the timestamp with the message
        }
        
        collection.insert_one(new_msg)
        compare_messages(new_msg)
    update_and_draw_graph()


#Graph Generation
G = nx.Graph()
update_and_draw_graph()

client.run_until_disconnected()


###### 10 21
from telethon import TelegramClient, events
from pymongo import MongoClient
import networkx as nx
from ast import literal_eval
import requests
import openai
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from datetime import datetime

def draw_graph():
    plt.clf()
    
    # Define custom positions
    pos = {
        "Chaîne 1": (1, 2),
        "Chaîne 2": (0, 1),
        "Chaîne 3": (2, 1),
        "Chaîne 4": (0, 0),
        "Chaîne 5": (2, 0),
        "Chaîne 6": (1, 0.5)
    }

    edge_colors = ["green" if G[u][v]['weight'] > 0 else "red" for u, v in G.edges()]
    edge_widths = [abs(G[u][v]['weight'])/5 for u, v in G.edges()]  # Adjusted edge width based on weight

    # Draw nodes and labels
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', width=edge_widths, edge_color=edge_colors, alpha=0.6)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.title("Relationships between Channels")
    plt.pause(0.1)
    plt.savefig('graph.png')



def update_and_draw_graph():
    for key, score in channel_connections.items():
        channelA, channelB = key.split("_")

        # Determine edge color
        edge_color = 'green' if score > 0 else 'red'

        # Add edge with attributes
        G.add_edge(channelA, channelB, weight=abs(score), color=edge_color)

    draw_graph()

load_dotenv()


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient('anon', api_id, api_hash)
client.start()

# MongoDB Setup
mongo_client = MongoClient(os.getenv("MONGO"))
db = mongo_client["telegram"]
collection = db["messages"]
affirmations = db["affirmations"]
channel_connections = {
    "Chaîne 1_Chaîne 2": 10,  # Strong positive relation between Chaîne 1 and Chaîne 2
    "Chaîne 1_Chaîne 3": 10,  # Strong positive relation between Chaîne 1 and Chaîne 3
    "Chaîne 2_Chaîne 3": 10,  # Strong positive relation between Chaîne 2 and Chaîne 3
    
    "Chaîne 4_Chaîne 5": 7,   # Positive relation between Chaîne 4 and Chaîne 5
    
    "Chaîne 4_Chaîne 1": -3,  # Negative relation between Chaîne 4 and the first group
    "Chaîne 4_Chaîne 2": -3,
    "Chaîne 4_Chaîne 3": -3,
    
    "Chaîne 5_Chaîne 1": -3,  # Negative relation between Chaîne 5 and the first group
    "Chaîne 5_Chaîne 2": -3,
    "Chaîne 5_Chaîne 3": -3,

    # Neutral Chaîne 6 has slight relations with others but not too strong either way
    "Chaîne 6_Chaîne 1": 1,
    "Chaîne 6_Chaîne 2": 1,
    "Chaîne 6_Chaîne 3": 1,
    "Chaîne 6_Chaîne 4": 1,
    "Chaîne 6_Chaîne 5": 1
}



openai.api_key = os.getenv("OPENAI")


# Function to get binary affirmation
def get_binary_affirmation(message):

    examples = affirmations.find({'toUse': True}).limit(15)

    prompt = f"""
    Please generate binary affirmations from the provided news message:

    '{message}'

    For each affirmation:

    1. Extract key assertions from the message. 
    2. Convert negations into their positive counterparts.
    3. Each affirmation must be standalone and provide full context. If there's an attributed source in the message, ensure it's included in the affirmation.
    4. Provide a truth value for each affirmation based on its accuracy within the message.

    The result should be in this format:
    {{
        'Binary affirmation 1': true/false,
        'Binary affirmation 2': true/false,
        ...
    }}

    Ensure that each binary affirmation is concise, clear, and independent. They should almost function as a unique hash of the information they contain.

    For example. Here I provide examples already checked by gpt-4, with corrections = result that should appear instead, or close to it. You need understand what I mean with these examples and strictly follow :



    """


############ 10 21












from telethon import TelegramClient, events
from pymongo import MongoClient
import networkx as nx
from ast import literal_eval
import requests
import openai
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

def draw_graph():
    plt.clf()
    G.remove_edges_from(nx.selfloop_edges(G))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.pause(0.1)
    plt.savefig('graph.png')

load_dotenv()


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient('anon', api_id, api_hash)
client.start()

# MongoDB Setup
mongo_client = MongoClient(os.getenv("MONGO"))
db = mongo_client["telegram"]
collection = db["messages"]
channel_connections = {}


openai.api_key = os.getenv("OPENAI")


# Function to get binary affirmation
def get_binary_affirmation(message):
    prompt = f"""Generate a list of binary affirmations in dictionary format from the given news message: '{message}'.

    Each key in the dictionary will either be:
    - A negated version of an original positive affirmation. 
    - The original negative affirmation, if it is already negative.

    The values will be 'true' or 'false' based on the validity of the statement.

    Please adhere strictly to the following format:
    {{'Negated Binary affirmation 1': true/false}}, {{'Negated Binary affirmation 2': true/false, ...}}

    If the original message contains an attributed statement (e.g., 'Erdogan said Ukraine starts the war'), ensure to include the attribution in the key so that each affirmation can stand alone and be understood independently."""

    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=2000,
        temperature=0.73,
        messages=messages
    )
    
    content = response['choices'][0]['message']['content']
    content = content.replace('true', 'True').replace('false', 'False')
    # The content should already be in the expected format
    print(content)
    try:
        affirmation_list = eval(content)  # Use eval to parse the content
        print(affirmation_list)
        return affirmation_list
    except Exception as e:
        print(f"Error parsing content: {e}")
        return []

# Function to compare messages and update graph
def compare_messages(new_msg):
    all_messages = list(collection.find({}))

    for old_msg in all_messages:
        key = f"{new_msg['channelID']}_{old_msg['channelID']}"
        #print(channel_connections)
        if key not in channel_connections:
            channel_connections[key] = 0

        if new_msg['binaryAffirmation'] == old_msg['binaryAffirmation'] and new_msg['truthValue'] == old_msg['truthValue']:
            channel_connections[key] += 1
        elif new_msg['binaryAffirmation'] == old_msg['binaryAffirmation'] and new_msg['truthValue'] != old_msg['truthValue']:
            channel_connections[key] -= 1

# Subscribe to channels
@client.on(events.NewMessage(chats=[-1001842901217, -1001905441409, -1001863996867, -1001944316671, -1001919265899]))
async def new_message_handler(event):
    message = event.message.text
    channel = event.chat_id
    binary_affirmations = get_binary_affirmation(message)
    print(binary_affirmations)

    for affirmation_dict in binary_affirmations:
        for affirmation, truth_value in affirmation_dict.items():
            new_msg = {
                'channelID': channel,
                'binaryAffirmation': affirmation,
                'truthValue': truth_value  # Taken directly from the dictionary
            }
            collection.insert_one(new_msg)
            compare_messages(new_msg)

    # Update and draw graph
    for key, score in channel_connections.items():
        channelA, channelB = key.split("_")
        if score > 0:
            G.add_edge(channelA, channelB, weight=score)

    #draw_graph()


# Graph Generation
G = nx.Graph()
for key, score in channel_connections.items():
    channelA, channelB = key.split("_")
    G.add_edge(channelA, channelB, weight=score)

client.run_until_disconnected()

        # self.characteristics.append(chr.Characteristic(-1, 'positive author attitude'))
        # self.characteristics.append(chr.Characteristic(-1, 'the message is advantageous for the actual political power'))
        # self.characteristics.append(chr.Characteristic(-1, 'exaggerations'))
        # self.characteristics.append(chr.Characteristic(-2, 'lack of object concordance'))
        # self.characteristics.append(chr.Characteristic(+1, 'appeal to the intellect'))
        # self.characteristics.append(chr.Characteristic(-1, 'appeal to emotions'))
        # self.characteristics.append(chr.Characteristic(-1, 'appeal to virtues'))
        # self.characteristics.append(chr.Characteristic(-1, 'appeal to ethics'))
        # self.characteristics.append(chr.Characteristic(-1, 'appeal to blinding generalities as fatherland, peace, glory, justice, honor'))
        # self.characteristics.append(chr.Characteristic(-1, 'appeal to fear'))
        # self.characteristics.append(chr.Characteristic(-1, 'appeal to the threat from other countries'))
        # self.characteristics.append(chr.Characteristic(-1, 'appeal to hatred')) #
        # self.characteristics.append(chr.Characteristic(-1, 'appeal to authority'))
        # self.characteristics.append(chr.Characteristic(+1, 'appeal to human rights')) # ?
        # self.characteristics.append(chr.Characteristic(+1, 'criticism of the actual political power'))
        # self.characteristics.append(chr.Characteristic(-1, 'generalizations'))
        # self.characteristics.append(chr.Characteristic(-1, 'seemingly scientific appearance, but only seemingly'))
        # self.characteristics.append(chr.Characteristic(+1, 'real scientific proofs of the information'))
        # self.characteristics.append(chr.Characteristic(+1, 'real proofs of the information')) # ?
        # self.characteristics.append(chr.Characteristic(-1, 'euphemismes replacing offensive expressions'))
        # self.characteristics.append(chr.Characteristic(-1, 'euphemismes replacing war or victims'))
        # self.characteristics.append(chr.Characteristic(-1, 'formal register of the texte')) # ?
        # self.characteristics.append(chr.Characteristic(-1, 'beneficiaries of the information regarding to politics'))
        # self.characteristics.append(chr.Characteristic(-1, 'flattery to the reader'))
        # self.characteristics.append(chr.Characteristic(-1, 'dilemma between only two possibilities'))
        # self.characteristics.append(chr.Characteristic(-1, 'criticisme of a person instead of criticism of his arguments')) 
        # self.characteristics.append(chr.Characteristic(-1, 'underestimation of the proofs of the opponents'))
        # self.characteristics.append(сharacteristic.Characteristic(+1, 'objectivity')) # портит
        # Object Concordance  : Positive (the message indicates that the disarmament process has begun under the control of Russian peacekeepers) 0

