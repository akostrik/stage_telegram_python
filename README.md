# Internship Master II, Sorbonne University (Paris)
An Internship of 5 months, from the 3 April 2023 to the 12 September 2023, in the association Ouverture du cœur (Paris)

## The goal of the application
Real time verification of Telegram messages veracity by two methods:

1) Looking for the marks of the propaganda in every separate message

2) Comparison of the information diffused by several channels in order to detect similar channels

## How does it work

![Capture d’écran de 2023-10-08 12-10-46](https://github.com/akostrik/stage_telegram/assets/22834202/9bbb5cb1-5a40-41ca-b504-8f6abf2d0756)

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
Install python version >= 3.5 

Install the libraries sys, openai, os, telethon, pymongo, time, datetime, dotenv, uuid, requests, ast  
### Configuration
#### Create the file "server1/.env" 
```sh
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

Import the collection 'characteristics' from the file characteristics.json :

```sh
sudo mongoimport --db telegram --collection characteristics --file collection_characteristics.json
```
If you use MongoDB Atlas, go to https://cloud.mongodb.com - Database Deployments, and presse "add current ip adresse"

#### Configuration Telegram
During the first Telegram connection enter your phone and then the confirmation code
### Compile and Run
In the first terminal launch server1
```sh
server1/python server1.py
```

## Server 2 (node.js)
### Setup
npm install
### Configuration
In the line 13 of server2/server.js put the same MongoDB connection string as in server1/.env:
```
const mongoUrl = 'mongodb+srv...';
```
### Compile and Run
In the second terminal launch vue:
```sh
cd server2
npm run dev
```
In the third terminal launch server2:
```sh
node server2/backend/server2.js
```
