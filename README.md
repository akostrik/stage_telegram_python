# Internship Master II, Sorbonne University (Paris)
An Internship of 5 months, from the 3 April 2023 to the 12 September 2023

## The missions of the internship
1) Real time verification of Telegram messages veracity by two methods:

- Looking for the marks of the propaganda in every separate message via OpenAI

- Comparison of the information diffused by several channels via OpenAI in order to detect similar channels

2) Constant improvement of the results by the mean of attaching of examples corriged by a user to OpenAI requests 

## The easy scheme of the appication (except Learning service)
![Screenshot from 2023-10-10 15-49-01](https://github.com/akostrik/stage_telegram/assets/22834202/89b2eab1-2291-44ea-a008-7a32fd9e0678)

## The scheme of the appication in programmer style
![Screenshot from 2023-10-10 16-19-29](https://github.com/akostrik/stage_telegram/assets/22834202/9da78718-4776-4c9f-ba2a-80432dc43723)


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
pip3 install telethon
```
```
pip install DateTime
```
```
npm i dotenv
```
```
pip install requests
```
```
pip install pymongo
```
```
pip install --upgrade openai
```
### Configuration
#### Configuration database MongoDB Atlas (in the cloud)
Create a MongoDB account : https://cloud.mongodb.com/ 

In your account, create database by the name 'telegram'

Import the collection 'characteristics' from the file characteristics.json to your mongo database 'telegram':

https://www.mongodb.com/docs/atlas/import/mongoimport/

```
sudo mongoimport --db telegram --collection characteristics --file collection_characteristics.json
```

Do this: https://cloud.mongodb.com - Database Deployments - "add current ip adresse"

Get you MonogDB connection string : https://cloud.mongodb.com/ - Database - Connect - Drives - connection string

PS You can use MongoDB installed locally
#### Configuration OpenAI 

Get your OpenAI key (OPENAI) here: https://platform.openai.com/account/api-keys

Your account should have acces to gpt-4

#### Configuration Telegram 

Get Telegram credentials (api_id and api_hash) here: https://my.telegram.org/auth

During the first launching of the application, enter the phone number of your Telegram account and then enter the confirmation code

#### Create the file "server1/.env" 
```
API_ID=...
API_HASH=...
OPENAI=...
MONGO=...
```
MONGO = your MonogDB connection string

OPENAI = OpenAI key

API_ID and API_HASH = Telegram credentials

#### Configuration Telegram
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
> const mongoUrl = '...';
### Compile and Run
In the second terminal launch Vue server:
```
cd server2
npm run dev
```
In the third terminal launch server2:
```
node server2/backend/server2.js
```
## User interface (vue.js)
After having installed and configured all noted above, go to http://localhost:5173/ et enjoy the service

## The limits of the application
- only for Linux
- MongoDB free size is limited to ... Mg
- OpenQI reauires payment

## The tests of other 

## PS
For technilcal details of server1 and server2, see README files in the corresponding folders.
All the questions are welcome at stage.mongodb at gmail.com
To have help to install the application, please write also to stage.mongodb at gmail.com  
