# Internship Master II, Sorbonne University (Paris)
The Internship of 5 months, from the 3d April 2023 to the 12th September 2023

## The missions of the internship
- Complete the education by a full-time profesional pratice in a Paris association
- Acquire a first professional experience as a developement ingineer
- Determine the initial orientation of the career, in particular computer sciences applied to the social life
- Acquire new knowledge, techniques, approaches, methods, méthodes, toolsls, etc, in practice
- Acquire know-how and the code of some French associations
- Evaluate the capacity of integration in the professional environment
- And so, ensure the entrance to the work market

## The context
The Telegram Messenger is a messenger application like WhatApp, Viber, Signal, etc, which is very popular in Russia and where there are many channels of different subjects

## What the developped appication can do
1) Real time verification of Telegram messages veracity by two methods:
- Looking for the marks of the propaganda in every separate message via OpenAI
- Comparison, via OpenAI, of the recent information diffused by several channels, in order to detect similar channels
2) Constant improvement of its results by the mean of the Learning service, which consiste of attaching of some previous OpenIA responses, corriged by a user, to OpenAI requests

### The easy scheme of the appication (except Learning service)
![Screenshot from 2023-10-10 15-49-01](https://github.com/akostrik/stage_telegram/assets/22834202/89b2eab1-2291-44ea-a008-7a32fd9e0678)

### The same scheme of the appication in the programmer style
![Screenshot from 2023-10-10 22-21-58](https://github.com/akostrik/stage_telegram/assets/22834202/99074446-16eb-4096-877b-af61d3f9efc6)

### The same scheme of the appication in English
1) Server 2, via its provided public API, gets, from the user, the names of Telegram channels to examinate 
2) Server 1 listens to the chosen channels
3) Server 1 treats every new message, that is:
- estimates the marks of the propaganda of the message via OpenAI
- basing on these marks of the propaganda calculates the trust coefficient of the message 
- extracts the principal information of the new message, in the form of several affirmations, via OpenAI
- compares these affirmations to the recent affirmations of the other followed channels
- stocks all obteined information in the database (the message itself, the result if its analisys, updates the trust coefficients of the channels, updates the measure of similarity of the channels)
4) Server 2, via its provided public API, after having treated a message by Server 1, returns the current results of the analysis to the server vue.js
5) Server vue.js displays the results to the user in the form of a graph of the channels, where every summit contains the id of the channel and its trust coefficient, and every edge is the measure of similarity of two concerned channels

Simultaneously, the learning service is working:
1) Server 2, via public API that it provides, propose to the user to correct the previous responses of OpenAI
2) As soon as the user provides the corrected examples, server 2 put it to the database
3) Server 1 attaches these corrected examples to every new OpenAI request (in the limit of examples)   

### The same scheme of the appication in programming languages
See :
- [server 1 code in python](https://github.com/akostrik/stage_telegram/tree/main/server1)
- [server 2 code in node.js](https://github.com/akostrik/stage_telegram/tree/main/server2/backend/server.js)
- [the user interface code in vue.js](https://github.com/akostrik/stage_telegram/tree/main/server2/src)

### The technical details
#### The parameters of the application
- Time where the messages are considered as recent (in hours)
- The model OpenAI for a characteristis request
- The model OpenAI for a affirmations request
- The maximal lenth of a Telegram message (a message is cut off beyond this length)
#### Other
- _Similarity measure of two channels (channel1, channel2)_ is equal to the numbre of similar affirmations in these channels for the 
- _The trust coefficient of a channel_ is a number in the interval [0 … 100]

See :
- [server 1 details](https://github.com/akostrik/stage_telegram/tree/main/server1)
- [server 2 details](https://github.com/akostrik/stage_telegram/tree/main/server1)

## How to use the application
### Database MongoDB Atlas configuration (in the cloud)
[Create a MongoDB account](https://cloud.mongodb.com/) 

In your account, create database by the name 'telegram'

Import the collection 'characteristics' from the file characteristics.json to your mongo database 'telegram':

https://www.mongodb.com/docs/atlas/import/mongoimport/

```
sudo mongoimport --db telegram --collection characteristics --file collection_characteristics.json
```

Go [here](https://cloud.mongodb.com) - Database Deployments - to add your current ip adresse

Go [here](https://cloud.mongodb.com/) - Database - Connect - Drives - to get you MonogDB connection string 

In the line 13 of [here](https://github.com/akostrik/stage_telegram/blob/main/server2/backend/server2.js) put the same MongoDB connection string as in server1/.env:
> const mongoUrl = '...';
Be careful not to pulish your MongoDB connection string on the internet

### OpenAI configuration 

[Get your OpenAI key](https://platform.openai.com/account/api-keys)

Your account should have acces to gpt-4 (a paying option)

### Telegram configuration  

[Get Telegram credentials api_id and api_hash ](https://my.telegram.org/auth)

During the first launching of the application, enter the phone number of your Telegram account and then enter the confirmation code

### Create the file "server1/.env" 
```
API_ID=...
API_HASH=...
OPENAI=...
MONGO=...
```
MONGO = your MonogDB connection string

OPENAI = OpenAI key

API_ID and API_HASH = Telegram credentials

### Server 1 setup
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

### Server 2 setup
```
npm install
```
### Compile and run
In the first terminal launch server1
```
server1/python server1.py
```
In the second terminal launch Vue server:
```
cd server2
npm run dev
```
In the third terminal launch server2:
```
node server2/backend/server2.js
```
### Go to the user interface (vue.js)
After having installed and configured all noted above, [enjoy the service](http://localhost:5173/) 
## The limits of the application
- only for Linux
### The limits related to MongoDB
- MongoDB free size is limited to ... Mg
- The instructions are provided here only for the cloud version MongoDB (MongoDB Atlas), however a user can use MongoDB installed locally
### The limits related to OpenAI
- OpenQI requires payment
- The learning service is limited to 5 examples par a request (and if the message or the examples are long, then less than 5)
- The length of an examined Telegram message is limites to 1000 tokens (words)
- The application work slowly (about 5 messages per minute), chiefly because of the gpt-4 long analysys   

## The prospectives to overpass these limits of the application
The OpenAI analysis, which is long by nature, may be accelerated by using a great number of powerful machines. Besides, others [language models](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) can be envisaged.  

## PS
[All the questions are welcome](mailto:stage.mongodb@gmail.com)

[Get help to install the application](mailto:stage.mongodb@gmail.com)  
