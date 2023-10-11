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
The Telegram Messenger is a messenger application like WhatApp, Viber, Signal, etc, which is very popular in Russia and where there are many channels on different subjects

## What the developped appication can do
1) Real time verification of Telegram messages veracity by two methods:
- Looking for the marks of the propaganda in every separate message via OpenAI
- Comparison, via OpenAI, of the recent information diffused by several channels, in order to detect similar channels
2) Constant improvement of its results by the mean of the Learning service, which consiste of attaching of some previous OpenIA responses, corriged by a user, to OpenAI requests

### The easy scheme of the appication (except Learning service)
![Screenshot from 2023-10-10 22-21-58](https://github.com/akostrik/stage_telegram/assets/22834202/99074446-16eb-4096-877b-af61d3f9efc6)

### The same scheme of the appication in the programmer style
![Screenshot from 2023-10-10 22-24-14](https://github.com/akostrik/stage_telegram/assets/22834202/fa7b6eae-d1d0-47cc-8a89-92dcf5c57d68)

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
1) Server 2, via public API that it provides, proposes to the user to correct the previous responses of OpenAI
2) As soon as the user provides the corrected examples, server 2 puts it to the database
3) Server 1 attaches these corrected examples to every new OpenAI request (in the limit of several examples)   

### The same scheme of the appication in programming languages
- [server 1 in python](https://github.com/akostrik/stage_telegram/tree/main/server1)
- [server 2 in node.js](https://github.com/akostrik/stage_telegram/tree/main/server2/backend/server.js)
- [the user interface in vue.js](https://github.com/akostrik/stage_telegram/tree/main/server2/src)

## How to use the application
### Database MongoDB Atlas configuration (in the cloud)
[Create a MongoDB account](https://cloud.mongodb.com/) 

In your account, create a database by the name 'telegram'

[Import the collection](https://www.mongodb.com/docs/atlas/import/mongoimport/) 'characteristics' from [the file characteristics.json]() to your database 'telegram':

```
sudo mongoimport --db telegram --collection characteristics --file collection_characteristics.json
```

Go [here](https://cloud.mongodb.com) - Database Deployments - to add your current ip adresse

Go [here](https://cloud.mongodb.com/) - Database - Connect - Drives - to get you MonogDB connection string 

In the line 13 of [here](https://github.com/akostrik/stage_telegram/blob/main/server2/backend/server2.js) put the same MongoDB connection string as in server1/.env: **.env** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
> const mongoUrl = '...';

_Be careful not to publish your MongoDB connection string on the internet and not to transmit it to unfamiliar people_

### OpenAI configuration 

[Get your OpenAI key](https://platform.openai.com/account/api-keys)

Your account should have acces to gpt-4 (a paying option)

_Be very very careful not to publish your MongoDB connection string on the internet and not to transmit it to unfamiliar people_

### Telegram configuration  

[Get Telegram credentials api_id and api_hash ](https://my.telegram.org/auth)

During the first launching of the application, enter the phone number of your Telegram account and then enter the confirmation code

The application will create a [session file](https://docs.telethon.dev/en/stable/concepts/sessions.html) _anon.session_ in the folder server1 in order to you can to login without re-sending the code. 
_Be careful not to publish this file on the internet and not to transmit it to unfamiliar people_

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
### Go to the user interface
After having installed and configured all noted above, [enjoy the service](http://localhost:5173/) 

## The parameters of the application
- The time where a messages is considered as recent (in hours)
- The model OpenAI for a characteristis request
- The model OpenAI for a affirmations request
- OpenAI temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use log probability to automatically increase the temperature until certain thresholds are hit. [^2]
- [The text of the characteristis request](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20request%20characteristics) 
- [The text of the affirmations request](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20reauest%20affirmations)
- The maximal lenth of a Telegram message (in characters)
- The maximal lenth of OpenAI request (in tokens [^1])

## The technical details
_Similarity measure of two channels (channel1, channel2)_ is equal to the numbre of similar affirmations in these channels

_The trust coefficient of a channel_ is a number in the interval [0 … 100]

The appication does O(N) OpenAI requests and O(N*K) MongoDB requests, where N is the total numbre of messages, K is the nuber of followed channels

Python is choosen for the server 1, because:
- it is well adapted to [data science projects](https://en.wikipedia.org/wiki/Data_science) because of its [specilised libraries](https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist)
- it is a rather easy language, partly because it frees the memory automatically

Every output of server 1 is saved in the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log)

Telegram requests are asynchronous 

OpenAI requests are **not asynchronous** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

MongoDB requests are **not all asynchronous** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

Why MongoDB ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

ls ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
## Experimentations
| Temperature | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|-------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| l’écart     |  2  |  2  |  2  |  2  |  3  |  4  |  3  |  3  |  5  |  5  |  5  |
| l’écart     |  1  |  1  |  2  |  3  |  1  |  1  |  3  |  4  |  2  |  4  |  4  |

## Exprerimentations that were not included in the final functionality
<img align="right" width="300" height="300" src="https://github.com/akostrik/stage_telegram/assets/22834202/9176b2d8-a75b-4335-8a97-80e82197579a">

- Extracting of detailed information from a message, like its main subject, the people it deals with, etc, that is "undesrstanding" of the message : because the analysis did not work corectly. Sorry for the example in Russian, the pour quality of the analysis

- Comparaison of paires of messages directly via OpenAI (instead of extracting the principal information in the form of affirmations) : demands O(N<sup>2</sup>) operations and so is too long (see [log example](https://github.com/akostrik/stage_telegram/blob/main/server1/log/log_2023_09_28_18h08%20ERROR%20LIMITE%20GPT4.txt)).

- Keeping of a part of the data in the application memory, and not in the database : because the application has no acces to the results of the previous executions 

- Extracting of the affirmations with gpt-3 : didn't work

- **дописать** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
## The limits of the application
- It is developped only for Linux
### The limits related to MongoDB
- MongoDB database size is limited to 16 Mgb (for free accounts) **to verify** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) 
- The instructions are provided here only for the cloud version MongoDB (MongoDB Atlas), however a user can use MongoDB installed locally
### The limits related to OpenAI
- The application work **slowly** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) (about 5 messages per minute), the [language models](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) analysis respesenting the lowest part of the appliation may be accelerated :
  * by using a great number of powerful machines
  * by using grand nombre of OpenAI accounts
  * others language models can be envisaged, for example [Facebook Artificial Intelligence Research](https://fr.wikipedia.org/wiki/Facebook_Artificial_Intelligence_Research), **because ...**
- Errors of OpenAI analisys, which may be improuved :
  * by learning
  * by cross-analysis by several language models 
- The length of an examined Telegram message is limited (see [The parameters of the application](https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application)), a message is cut off beyond this length
- The learning service is limited to 5 examples par a request (but if the message, the examples and the OpenAI response are altogether longer than [_The maximal lenth of OpenAI request_]((https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application)) parameter, then less than 5 examples)
- OpenAI is paying

### The limits related to Telegram
- The application can't read some channels, [for example this one](https://t.me/generallsvr) **why** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
### Non-technical limits 
- The learning and the choice of the characteristics are founded on a human subjective opinion
- The application may help to the malefactors to adjust the propagandistic messages to make them pass unnoticed
- The application doesn't aime at the deep causes of the propaganda 


## PS
<img align="right" width="60" height="60" src="https://github.com/akostrik/stage_telegram/assets/22834202/9d78c9d6-c4c6-4566-9e83-3dcbc02e311e"> 

[All the questions are welcome](mailto:stage.mongodb@gmail.com)


[Get help to install the application](mailto:stage.mongodb@gmail.com) 


## Sources
[image source](https://tenor.com/fr/view/welcome-emoji-smile-gif-10359622) 

[^1]: in English 1 token ≈ 3/4 of a word
[^2]: https://platform.openai.com/docs/api-reference/audio/createTranscription#audio/createTranscription-temperature 
