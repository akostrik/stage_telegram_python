# Internship Master II, Sorbonne University (Paris)
An Internship of 5 months, from the 3 April 2023 to the 12 September 2023, 

in the association Ouverture du cœur (Paris)

## The goal of the application
Real time verification of Telegram messages veracity by two methods:

1) Looking for the marks of the propaganda in every separate message

2) Comparison of the information diffused by several channels in order to detect similar channels

## The scheme of the appication (except Learning service)

![Screenshot from 2023-10-08 21-42-47](https://github.com/akostrik/stage_telegram/assets/22834202/fb1a73ae-25fb-4732-916d-e04c3dc3fd01)

## Server 1 (python)
1) Listens to the Telegram channels
2) Treats a new message :
- estimates the marks of the propaganda of the message via OpenAI, basing on them calculates the trust coefficient of the message 
- so the server updates the trust coefficient of the channels
- extracts the principal information of the new message, in the form of several affirmations, via OpenAI
- compares these affirmations to the recent affirmations of the other followed channels
- so the server updates the measure of similarity of the channels
- constructs the graph of the channels, where every summit contains the id of the channel and its trust coefficient, and every edge is the measure of similarity of two channels 
  
### Setup 
Install python version >= 3.7.1

Install the libraries :
```
sys
```
```
os
```
```
telethon
```
```
time
```
```
datetime
```
```
dotenv
```
```
requests
```
```
pip install pymongo
```
```
pip install --upgrade openai
```
### Configuration
#### Create the file "server1/.env" 
```
API_ID=...
API_HASH=...
OPENAI=...
MONGO=...
```
The linens to get these values :

Télégram credentials (API_ID and API_HASH) : https://my.telegram.org/auth

OpenAI key (OPENAI): https://platform.openai.com/account/api-keys

MonogDB connection string (MONGO): https://cloud.mongodb.com/ - Database - Connect - Drives - connection string

#### Configuration MongoDB

Create database 'telegram'

Import the collection 'characteristics' from the file characteristics.json to your mongo database:

```
sudo mongoimport --db telegram --collection characteristics --file collection_characteristics.json
```

If you use MongoDB Atlas, do this: https://cloud.mongodb.com - Database Deployments - "add current ip adresse"

#### Configuration Telegram
During the first launching, enter the phone number of your Telegram account and then enter the confirmation code
### Compile and Run
In the first terminal launch server1
```
server1/python server1.py
```

## Server 2 (node.js)
### Setup
```
npm install
```
### Configuration
In the line 13 of server2/backend/server2.js put the same MongoDB connection string as in server1/.env:
> const mongoUrl = 'mongodb+srv...';
### Compile and Run
In the second terminal launch Vue:
```
cd server2
npm run dev
```
In the third terminal launch server2:
```
node server2/backend/server2.js
```
