# Internship Master II, Sorbonne University (Paris)
The Internship of 5 months, from the 3d April 2023 to the 12th September 2023

## The general missions of the internship
- Complete the education by a full-time profesional pratice in a Paris association
- Acquire a first professional experience as a developement ingineer
- Determine the initial orientation of the career, in particular computer sciences applied to the social life
- Acquire new knowledge, techniques, approaches, methods, méthodes, toolsls, etc, in practice
- Acquire know-how and the code of associations
- Evaluate the capacity of integration in the professional environment
- So, ensure the entrance to the work et

## The particular missions of the internship in the context 
Thus project is aimed at automatical detecting of propagandistic information in Telegram channels. 

That is the infoirmation, which may not be objective and may be selectively presenting facts to encourage a particular perception, or using loaded language to produce an emotional rather than a rational response to the information. [^6]

The Telegram Messenger is an application similar to WhatApp, Viber, Signal, etc. Its particularities are that it has a lot of channels on different subjects (chiefly in Russian) with little censorship limitations.

## What the appication does
1) Real time verification of Telegram messages veracity by two methods:
- Looking for the marks of the propaganda [^8] in every separate message via OpenAI
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
4) Server 2, via its provided public API, after having treated a message by Server 1, returns permanently the current results of the analysis to the server vue.js
5) Server vue.js displays the results to the user in the form of a graph of the channels, where every summit contains the id of the channel and its trust coefficient, and every edge is the measure of similarity of two concerned channels

Simultaneously, the learning service is working:
1) Server 2, via public API that it provides, proposes to the user to correct the previous responses of OpenAI
2) As soon as the user provides the corrected examples, server 2 puts them to the database
3) Server 1 attaches these corrected examples to every new OpenAI request (in the limit of several examples)   

### The same scheme of the appication in programming languages
- [server 1 in python](https://github.com/akostrik/stage_telegram/tree/main/server1)
- [server 2 in node.js](https://github.com/akostrik/stage_telegram/tree/main/server2/server.js)
- [the user interface in vue.js](https://github.com/akostrik/stage_telegram/tree/main/user_interface/src)

## How to use the application
### Database MongoDB Atlas configuration (in the cloud)
[Create a MongoDB account](https://cloud.mongodb.com/) 

In your account, create a database by the name 'telegram'

[Import the collection](https://www.mongodb.com/docs/atlas/import/mongoimport/) 'characteristics' from [this file](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/collection_characteristics.json) to your database 'telegram': ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

```
sudo mongoimport --db telegram --collection characteristics --file collection_characteristics.json
```

Go [to the MongoDB interface](https://cloud.mongodb.com) - Database Deployments - to add your current ip adresse

Go [to the MongoDB interface](https://cloud.mongodb.com/) - Database - Connect - Drives - to get you MonogDB connection string 

In the line 13 of [here](https://github.com/akostrik/stage_telegram/blob/main/server2/server2.js) put the same MongoDB connection string as in server1/.env: **.env** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
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
**in any folder ?** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
### Compile and run
In the first terminal launch server1
```
python server1/server1.py
```
In the second terminal launch Vue server:
```
cd user_interface
npm run dev
```
In the third terminal launch server2:
```
node server2/server2.js
```
### Go to the user interface
After having installed and configured all noted above, [enjoy the service](http://localhost:5173/) 

## How does the application work
### The parameters of the application
- The characteristics of the propaganda
- [The text of the characteristis request](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20request%20characteristics) 
- [The text of the affirmations request](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20reauest%20affirmations)
- OpenAI model for a characteristis request
- OpenAI model for a affirmations request
- OpenAI temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more deterministic. If set to 0, the model will use log probability to automatically increase the temperature until certain thresholds are hit. [^2]
- OpenAI request maximal lenth (in tokens [^1])
- Telegram message maximal lenth (in characters)
- The time where a message is considered as recent (in hours)

### Technical details
#### General details, the data, computation, etc 
_Similarity measure of two channels (channel1, channel2)_ = the numbre of their similar affirmations  - the number of their opposite affirmations

_The trust coefficient of a channel_ is a number in the interval [0 … 100]

The appication does O(N) OpenAI requests and O(N*K) MongoDB requests, where N is the total numbre of messages, K is the nuber of followed channels

Output of server 1 is saved in the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log)

#### Python
The server 1 is written in Python, because:
- Python is well adapted to [data science projects](https://en.wikipedia.org/wiki/Data_science) because of its [specilised libraries](https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist) like telethon, DateTime, requests, pymongo, openai
- Python is a rather easy language (partly because it frees the memory automatically)

#### Javascript
The user interface is written in Vue.js, because its programming model is adapted to efficiently develop user interfaces, be they simple or complex [^3], it has a simple syntax and intuitive documentation and suits for smaller projects and novice developers [^7]
Data-driven developpement 

Vite, a development server used by default by Vue, monitors files as they're being edited and upon file save the web browser reloads the code being edited through a process called Hot Module Replacement (HMR) which works by just reloading the specific file being changed instead of recompiling the entire application. [^5]

Cross-origin resource sharing (CORS) is a mechanism that allows restricted resources on a web page to be accessed from another domain outside the domain from which the first resource was served.

**Other details** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

#### Asynchronous requests
Telegram requests are asynchronous 

OpenAI server 1 requests are **not asynchronous** 

MongoDB server 1 requests are **not all asynchronous**

Server 2 requests ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

#### Database
A noSql database usage is explained chiefly by the changing number of the _characteristics_, as well as by changing of the _characteristics_ themselves, while adjusting the application (it concerns the collections _Characteristics_ and _Messages_) 

**Why MongoDB** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) 

## The limits of the application
- It is developped only for Linux
### The limits related to MongoDB
- MongoDB database size is limited to 16 Mgb (for free accounts) **to verify** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png) 
- The instructions are provided here only for the cloud version MongoDB (MongoDB Atlas), however a user can use MongoDB installed locally ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
### The limits related to OpenAI
- The application work **slowly** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png), chieflt beacuse gpt-4 treats about 5 messages per minute. However, the [language model](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) analysis, respesenting the lowest part of the appliation, may be accelerated :
  * by involving a great number of powerful machines
  * by involving a grand numbre of OpenAI accounts
  * using of other language models can be envisaged, for example [Facebook Artificial Intelligence Research](https://fr.wikipedia.org/wiki/Facebook_Artificial_Intelligence_Research), **which is ...**
- Errors of OpenAI analisys, which may be improuved :
  * by cross-analysis by several language models 
  * by learning
- The length of an examined message is limited (see [The parameters of the application](https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application)), a message is cut off beyond this length
- The learning service is limited to 5 examples par a request (but if the message, the examples and the OpenAI response are altogether longer than [_The maximal lenth of OpenAI request_]((https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application)) parameter, then the learninh is limites to less than 5 examples)
- OpenAI is paying

### The limits related to Telegram
- The application **can't read some channels**, for example [this one](https://t.me/generallsvr) ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)
### Non-technical limits 
- The learning and the choice of the characteristics are founded on a human subjective opinion
- The application may help to the malefactors to adjust the propagandistic messages to make them pass unnoticed
- The application doesn't aime at the deep causes of the propaganda 

## Experimentations
### OpenAI experimentations
<img align="right" width="300" height="300" src="https://github.com/akostrik/stage_telegram/assets/22834202/9176b2d8-a75b-4335-8a97-80e82197579a">

Extracting of detailed information from a message, like its main subject, the people it deals with, etc, that is "undesrstanding" of the message : because the analysis did not work corectly. Sorry for the example in Russian, the pour quality of the analysis

The comparaison of paires of messages directly via OpenAI (instead of extracting the principal information in the form of affirmations) demands O(N<sup>2</sup>) operations and so is too long (see [log example](https://github.com/akostrik/stage_telegram/blob/main/server1/log/log_2023_09_28_18h08%20ERROR%20LIMITE%20GPT4.txt)).

To test the bonds of the trust coefficient and the temperature parameter, I launched two tests, every of the tests on two groups of channels, a propagandistic group and a non-propagandistic one (accordingly to my intuition). In the table, I noted the difference of the average coefficient of the two groups. The tests show a tendancy of better distinction between the two groups while the temperature parameter is hier.    
| Temperature    | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| difference     |  2  |  2  |  2  |  2  |  3  |  4  |  3  |  3  |  5  |  5  |  5  |
| difference     |  1  |  1  |  2  |  3  |  1  |  1  |  3  |  4  |  2  |  4  |  4  |

Extracting of the affirmations with gpt-3 didn't work.

The direct question to OpenAI, _Is there marks of the propagande in this message?_, didn't work correctly.

### Other experimentations
Keeping of a part of the data in the application memory, and not in the database : because the application has no acces to the results of the previous executions 

Elasticsearch ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

Distances euclidienne, jaccrd, cos, ... ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

**дописать** ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

## How the internship has been orgainized (the methodology)
Agile scrum [#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

## Why an application like this
...

## Some projects of similar orientation
- [The project of Huan Cao [ru]](https://hightech.fm/2018/08/28/fakenews?is_ajax=1&ysclid=ln2wvj9vsp325940854), exploring activity and localistation of the users, etc
- [Detecting of communities with similar ideologies by cross-channel interactions](https://medium.com/dfrlab/understanding-telegrams-ecosystem-of-far-right-channels-in-the-us-22e963c09234) by [DRFLab](https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/)
- Machine learning project [Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation](https://arxiv.org/abs/2203.05386)
- Machine learning project [Botometer](https://botometer.osome.iu.edu/faq#how-does-it-works)
- Machine learning project by [The Institute of Mathematical and Computing Sciences (Brazil)](https://cemeai.icmc.usp.br/)
- Machine learning project [Buster.ai](https://www.buster.ai/)
- Workshops [Fever](https://fever.ai/workshop.html)
- [Auxipresse](https://auxipress.be/)

## Sources
[image source](https://tenor.com/fr/view/welcome-emoji-smile-gif-10359622) 

## Welcome
<img align="right" width="60" height="60" src="https://github.com/akostrik/stage_telegram/assets/22834202/9d78c9d6-c4c6-4566-9e83-3dcbc02e311e"> 

[All the questions are welcome](mailto:stage.mongodb@gmail.com)

[Get help to install the application](mailto:stage.mongodb@gmail.com) 

[^1]: in English 1 token ≈ 3/4 of a word
[^2]: https://platform.openai.com/docs/api-reference/audio/createTranscription#audio/createTranscription-temperature 
[^3]: [https://www.scalablepath.com/front-end/vue-vs-react](https://vuejs.org/guide/introduction.html#what-is-vue)https://vuejs.org/guide/introduction.html#what-is-vue 
[^5]: https://en.wikipedia.org/wiki/Vite_(software)
[^6]: https://www.britannica.com/topic/propaganda
[^7]: https://skillbox.ru/media/code/vuejs-chto-takoe-kak-on-ustroen-i-chem-otlichaetsya-ot-react/ 
[^8]: https://www.cairn.info/revue-questions-de-communication-2020-2-page-371.htm 
