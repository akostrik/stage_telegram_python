Verification of the Telegram messages veracity by two methods:
1) Looking for the marks of the propaganda in a separate message
2) Comparison of the information diffused by several channels in order to detect similar channels

## Project Setup

1) In the folder 'python' create a file named ".env" :
```sh
API_ID=... (Telegram connection)
API_HASH=... (Telegram connection)
OPENAI=... (OpenAI key)
MONGO=... (MonogDB connection string like mongodb+srv: ... @cluster0.fnbrrzu.mongodb.net/?retryWrites=true&w=majority
```

2) Configure MongoDB Atlas:
- go to https://cloud.mongodb.com 
- sign in 
- go to Database Deployments
- presse "add current ip adresse"

Create database 'telegram'

Import collection 'characteristics' from the file characteristics.json :

```sh
sudo mongoimport --db telegram --collection characteristics --file characteristics.json
```

During the first Telegram connection enter your phone and then the confirmation code.

### The first server :
1) Listens to the Telegran channels
2) Treats a new message :
- estimates the marks of the propaganda via OpenAI Analysis, basing on them calculate the trust coefficient of the message 
- so the server updates the trust coefficient of the group of the channels
- extracts the principal information of the message via OpenAI analysis in the form of several affirmations
- compares this affirmations to the recent affirmations of all the other channels
- so the server updates the mesure of similarity of the channels
-  
#### Compile and Run
```sh
python/python main.py
```
