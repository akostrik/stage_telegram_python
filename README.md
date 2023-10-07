# Stage MAsteur II Sorbonne University (3, April 2023 - 12 September 2023)
Real time verification of the Telegram messages veracity by two methods:1) Looking for the marks of the propaganda in every separate message
2) Comparison of the information diffused by several channels in order to detect similar channels

## The first server (python)
1) Listens to the Telegram channels
2) Treats a new message :
- estimates the marks of the propaganda of the message via OpenAI, basing on them calculates the trust coefficient of the message 
- so the server updates the trust coefficient of the channels
- extracts the principal information of the new message, in the form of several affirmations, via OpenAI
- compares this affirmations to the recent affirmations of the other channels of the group
- so the server updates the measure of similarity of the channels
- constructs the graph of the channels, where every edge is the measure of similarity of two channels, and every summit contains the id of the channel and its trust coefficient 
  
### Setup
#### Install 
python version >= 3.5 

the libraries sys, openai, os, telethon, pymongo, time, datetime, dotenv, uuid, requests, ast  
#### Create the file "server1/.env" 
```sh
API_ID=... (Telegram connection)
API_HASH=... (Telegram connection)
OPENAI=... (OpenAI key)
MONGO=... (MonogDB connection string)
```
Télégram credentials API_ID and API_HASH may be obteined here my.telegram.org

OpenAI key here https://platform.openai.com/account/api-keys

MonogDB connection string here https://cloud.mongodb.com/ - Database - Connect - Drives - connection string

#### Configure MongoDB

Create database 'telegram'

Import the collection 'characteristics' from the file characteristics.json :

```sh
sudo mongoimport --db telegram --collection characteristics --file characteristics.json
```
If you use MongoDB Atlas, go to https://cloud.mongodb.com - Database Deployments, and presse "add current ip adresse"

#### Configure Telegram
During the first Telegram connection enter your phone and then the confirmation code
### Compile and Run
```sh
server1/python main.py
```
