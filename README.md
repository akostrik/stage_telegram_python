# The project
Real time verification of the Telegram messages veracity by two methods:
1) Looking for the marks of the propaganda in every separate message
2) Comparison of the information diffused by a group of channels in order to detect similar channels

## The first server
1) Listens to the Telegram channels
2) Treats a new message :
- estimates the marks of the propaganda of the message via OpenAI, basing on them calculates the trust coefficient of the message 
- so the server updates the trust coefficient of the channels
- extracts the principal information of the new message, in the form of several affirmations, via OpenAI
- compares this affirmations to the recent affirmations of the other channels of the group
- so the server updates the measure of similarity of the channels
- constructs the graph of the channels, there every edge is the measure of similarity of two channels, and every summit contains the id of the channel and its trust coefficient 
  
### Setup
1) Create the file "python/.env" : 
```sh
API_ID=... (Telegram connection)
API_HASH=... (Telegram connection)
OPENAI=... (OpenAI key)
MONGO=... (MonogDB connection string)
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
3) During the first Telegram connection enter your phone and then the confirmation code
### Compile and Run
```sh
python/python main.py
```
