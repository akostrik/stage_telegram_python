# Internship Master II, Sorbonne University (Paris)
The project hase been developped during an Internship of 5 months, from the 3d April 2023 to the 12th September 2023, realized in Paris associations.

## The objectives:
- Professional Experience: Engage in full-time professional practice within Parisian associations
- Skill Development: Cultivate skills as a development engineer, focusing on real-world applications
- Career Exploration: Investigate potential career trajectories, especially in computer sciences applied to societal challenges
- Hands-on Learning: Immerse in new techniques, methodologies, tools, and their practical applications
- Association Ethics: Grasp the ethical considerations and operational nuances of associations
- Professional Adaptability: Evaluate one's ability to integrate and adapt in a professional environment
- Job Market Transition: Equip oneself with the skills and experience to seamlessly enter the job market

## Context and motivation
The technologies has been always influenced greatly the social relations. In particular, the present-day computer science is an exceptional tool for cooperation and co-reflection.

This project is aimed at automatical detecting of propagandistic information in Telegram [^13] channels. That is, the information, which may not be objective and may be selectively presenting facts to encourage a particular perception, or using loaded language to produce an emotional rather than a rational response to the information. [^6]

## Some projects of similar orientation
- [Detecting of communities with similar ideologies by cross-channel interactions](https://medium.com/dfrlab/understanding-telegrams-ecosystem-of-far-right-channels-in-the-us-22e963c09234) by [DRFLab](https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/)
- [The project of Huan Cao [ru]](https://hightech.fm/2018/08/28/fakenews?is_ajax=1&ysclid=ln2wvj9vsp325940854), exploring activity and localistation of the users, etc
- Machine learning project [Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation](https://arxiv.org/abs/2203.05386)
- Machine learning project [Botometer](https://botometer.osome.iu.edu/faq#how-does-it-works)
- Machine learning project by [The Institute of Mathematical and Computing Sciences (Brazil)](https://cemeai.icmc.usp.br/)
- Machine learning project [Buster.ai](https://www.buster.ai/)
- Workshops [Fever](https://fever.ai/workshop.html)
- [Auxipresse](https://auxipress.be/)

## The methodology
The project followed the [agile practices](https://en.wikipedia.org/wiki/Agile_software_development) which include requirements discovery and solutions improvement through self-organizing and cross-functional teams with the users, except that both the developpers team and the users were represented by myself only.

The approach to development followed the Scrum principes like:
- to break work into goals to be completed within time-boxed iterations, called sprints, where the sprints were dedicated to the contexte, the [large language models](https://en.wikipedia.org/wiki/Large_language_model), the architecture, python and its interactions with the concerned API study, the datababases and elasticsearch, frontend);
- bringing decision-making authority to an operational level;
- continuous feedback and flexibility; 
- changing of the requirements as the project evolves.

## Aquired competences
A lof of completely new experience was aquired, like:
- the conception of a whole application with several servers, several API, several external services
- programming languages languanges (python, node.js)
- frameworks (Vue, express, ...) 

## Acknowleggements
This project wouldn't have been possible without the guidance of the faculty at Sorbonne University, the feedback from early users and the continuous support from the associations.

# Project overview

## Application features
1. Real-time Telegram messages verification by two methods:
- Scan individual messages for propaganda markers via OpenAI [^8];
- Analyze recent information from various channels to identify and highlight similarities, ensuring users are aware of potential echo chambers.
2. Continuous learning and improvement:
- Feedback Loop: The application learns from its mistakes. By leveraging previous OpenAI responses, which are corrected by users, the system refines its accuracy over time.

## Simplified diagram of the application (except Learning service)
![Capture d’écran de 2023-10-12 10-38-38](https://github.com/akostrik/stage_telegram/assets/22834202/41252982-3978-40d9-9b2b-20483566d203)

## Diagram of the application in the programmer style
![Screenshot from 2023-10-10 22-24-14](https://github.com/akostrik/stage_telegram/assets/22834202/fa7b6eae-d1d0-47cc-8a89-92dcf5c57d68)

## Application components
[_Server 1_](https://github.com/akostrik/stage_telegram/tree/main/) in python handles real-time data streaming from Telegram, processes messages, and interacts with OpenAI for analysis.

[_Server 2_](https://github.com/akostrik/stage_telegram/tree/main/server2/server.js) in node.js manages data retrieval from MongoDB and serves it to the frontend.

[_Server 3_](https://github.com/akostrik/stage_telegram/tree/main/user_interface/src) in vue.js presents the analyzed data to users in an intuitive and interactive manner.

## Description of the application
1) _Server 3_ gets from the web browser a name of Telegram channel to examinate, via Server 3 [API](https://fr.wikipedia.org/wiki/Interface_de_programmation)
2) _Server 3_ transmet the name of the channel to _Server 2_, via Server 2 API
3) _Server 2_ put puts the name of the channel to [MongoDB Atlas database](https://www.mongodb.com/fr-fr/cloud/atlas/lp/try4), via MongoDB API
4) _Server 1_ permanently gets the names of the channels from MongoDB Atlas, via MongoDB API
5) _Server 1_ listens permanently to the chosen channels, via Telegram API
6) _Server 1_ treats every new message, that is:
- estimates the marks of the propaganda of the message, via OpenAI API
- based on these marks of the propaganda it calculates the trust coefficient of the message
- extracts the principal information of the new message, in the form of several affirmations, via OpenAI API
- compares these affirmations to the recent affirmations of the other followed channels
- stocks all obtained information in MongoDB Atlas database (the message itself, the result if its analisys, updates the trust coefficients of the channels, updates the measure of similarity of the channels), via MongoDB API
7) _Server 2_ consults permanently the results of the computations in MongoDB Atlas, via MongoDB API
8) _Server 2_ returns permanently the current results of the computations to the _Server 3_, via Server 2 API
9) _Server 3_ passes the the results to the web browser in the form of a graph of the channels, where every summit contains the id of the channel and its trust coefficient, and every edge is the measure of similarity of two concerned channels, via Server 3 API
10) The web browser displays the graph to the user

Simultaneously, the _Learning service_ is working:
1) _Server 3_ proposes to the user to correct OpenAI's previous responses in the web browser, via the Server 3 API
2) As soon as the user provides the corrected examples, _Server 3_ passes them to _Server 2_
3) _Server 3_ puts the corrected examples to the database, via MongoDB API
4) _Server 1_ attaches (a limited number of) corrected examples to every new OpenAI request 

# Setup and usage
The user should have a web browser compatible with ECMAScript 5 (for example, IE8 and its previous versions are  not compatible with ECMAScript 5)

## MongoDB Atlas configuration

[MondoDB Atlas](https://www.mongodb.com/fr-fr/cloud/atlas/lp/try4) in a database MongoDB the in cloud.

[Create a MongoDB account](https://cloud.mongodb.com/) 

In your account, create a database by the name 'telegram'

[Import the collection](https://www.mongodb.com/docs/atlas/import/mongoimport/) 'characteristics' from [this file](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/collection_characteristics.json) to your database 'telegram': ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

```bash
sudo mongoimport --db telegram --collection characteristics --file collection_characteristics.json
```

Go [to the MongoDB interface](https://cloud.mongodb.com) - Database Deployments - `to add your current ip address`

Go [to the MongoDB interface](https://cloud.mongodb.com/) - Database - Connect - Drives - `to get you MongoDB connection string` 

_Be careful not to publish your MongoDB connection token on the internet and not to transmit it to unfamiliar people_

## OpenAI configuration 

[Get your OpenAI connection token](https://platform.openai.com/account/api-keys)

Your account should have access to gpt-4 (a paying option)

_Be very very careful not to publish your OpenAI connection token on the internet and not to transmit it to unfamiliar people_

## Telegram configuration

[Get Telegram credentials api_id and api_hash ](https://my.telegram.org/auth)

During the first launching of the application, enter the phone number of your Telegram account and then enter the confirmation code

The application will create a [session file](https://docs.telethon.dev/en/stable/concepts/sessions.html) `anon.session` in the folder `server1` in order to you can to login without re-sending the code. 

_Be very very careful not to publish the Telegram credentials on the internet and not to transmit them to unfamiliar people_

## `.env` file configuration 
Put MONGO = your MongoDB connection token, OPENAI = OpenAI connection token, API_ID and API_HASH = Telegram credentials in the file `server1/.env.example`: 
```
API_ID=...
API_HASH=...
OPENAI=...
MONGO=...
```
Rename `server1/.env.example` to `server1/.env`

Copy `server1/.env` to `server2/.env`

_Be very very careful not to publish this file on the internet and not to transmit it to unfamiliar people_

## Setup
Install python version >= 3.7.1

Install the python libraries :
```bash
pip3 install telethon
pip install DateTime
npm i dotenv
pip install requests
pip install pymongo
pip install --upgrade openai
```
Install [nmp package manager](https://www.npmjs.com/)
```
cd server3
npm install
```
_PS `npm install` should be executed in the same folder where `package.json` file is_

## Compile and run
In the first terminal launch _Server 1_
```bash
python server1/server1.py
```
In the second terminal launch _Server 2_
```bash
node server2/server2.js
```
In the third terminal launch _Server 3_
```bash
cd user_interface
npm run dev
```
## Go to the user interface
After having installed and configured all noted above, enjoy the service http://localhost:5173/ 

# Technical details of the deveppement
_To unserstand this section, the reader should have basic knowledge of the teminology of computer sciences_

Separation of the data treatment provided by _Server 1_ and the presentation functoinality provided by _Server 2_ and _Server 3_ falls into the pattern of [Model-View-ViewModel (MVVM)](https://ru.wikipedia.org/wiki/Model-View-ViewModel).

_Server 1_ and _Server 2_ represent the backend functionality, while _Server 3_ ensures the Frontend one.

## The parameters of the application
- The characteristics of the propaganda
- [The text of the characteristics request](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20request%20characteristics) 
- [The text of the affirmations request](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20reauest%20affirmations)
- OpenAI model for a characteristics request
- OpenAI model for a affirmations request
- OpenAI temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more deterministic. If set to 0, the model will use log probability to automatically increase the temperature until certain thresholds are hit. [^2]
- OpenAI request maximal lenth (in tokens [^1])
- Telegram message maximal length (in characters)
- The time where a message is considered as recent (in hours)

## Computation details 
_Similarity measure of two channels (channel1, channel2)_ = the numbre of their similar affirmations  - the number of their opposite affirmations

_The trust coefficient of a channel_ is a number in the interval [0 … 100]

The application executes 2 OpenAI requests par message.

The application executes O(K) MongoDB requests par message, where K is the number of followed channels. Besides, it executes contanstly MongoDB requests in order to integrate immediately a new channel added by the user.

## Python details
The _Server 1_ is written in Python, because:
- Python is well adapted to [data science projects](https://en.wikipedia.org/wiki/Data_science) because of its [specilised libraries](https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist) like telethon, DateTime, requests, pymongo, openai
- Python is a rather easy language (partly becauseof its easy syntax)

## Presentation functionality (node.js and Vue) details

[Node.js](https://nodejs.org/en/about), a asynchronous event-driven JavaScript runtime environment and library, runs the application outside of the client’s web browser, which is a raisonable choice because no function in Node.js directly performs I/O, so the process never blocks except when the I/O is performed using synchronous methods of Node.js standard library [^10].

[Vue](https://vuejs.org/) framework choice as programming model to develop the user interface (regarding to Angular and React as its possible alternatives), is explained by the simple syntax of Vue, its intuitive documentation and its pertinence for smalle projects and novice developers [^7] [^9].

[Express](https://expressjs.com/) Node web framework, is used by _Server 2_ to:
- write handlers for requests
- set the port to use, and the location of templates that are used for rendering the response
- integrate with "view" rendering engines in order to generate responses by inserting data into templates.

[Vite](https://vitejs.dev/), a local development server used by Vue, monitors files as they're being edited. Upon file save the web browser reloads the code being edited through a process called Hot Module Replacement which works by reloading only the specific file being changed. [^5]

## Asynchrony details

[Asynchrony](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) refers to the actions instigated by a program that take place concurrently with program execution, without the program blocking to wait for results. In this application, it concerns the requests to Telegram, OpenAI and MongoDB.

Telegram requests are asynchronous 

OpenAI server 1 requests are **not asynchronous** 

MongoDB server 1 requests are **not all asynchronous**

Server 2 requests ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

## Database details
A noSql database usage is explained chiefly by the changing number of the `characteristics`, as well as by changing of the `characteristics` themselves, while adjusting the application (it concerns the collections `characteristics` and `messages`).

MongoDB usage is explained by its SaaS offer and its popularity. The databse operations of this project are simple, so other noSql databases would provide the same functionnalty and at the speed.  

## Other technical details
Output of server 1 is saved in the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log)

# Limitatoins, challenges and future enhancements 

It is developped only for Linux.

The installation and configuration instructions are complicated for a user, they should be unified in one instruction by using Docker.
 
## The limits related to OpenAI
Gpt-4 treats only about 5 requests per minute. However, this [large language model](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) analysis, respesenting the lowest part of the appliation, may be accelerated :
  * by involving a great number of powerful machines
  * by involving a grand number of OpenAI accounts
  * using of other language models can be envisaged, for example

The quality of OpenAI analisys may be improuved :
  * by cross-analysis by several language models 
  * by prompt design
  * by learning ()
  * by fine-tuning

Alternatives to the paid approach could be to train a self-hosted model (like LLama2) on a corpus proofread by humans, since it has been proven that smaller models can perform way better than larger models. [^12]

The length of an examined message is limited (see [The parameters of the application](https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application)), a message is cut off beyond this length

The learning service is limited to 5 examples par a request (but if the message, the examples and the OpenAI response are altogether longer than [_The maximal length of OpenAI request_]((https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application)) parameter, then the learning is limited to less than 5 examples)

Extraction of affirmations gives acceptable results only with Gpt-4 (not with Gpt-3) and only with some examples included in the request.

## The limits related to MongoDB

The installation instructions are provided in this document only for the cloud version MongoDB (MongoDB Atlas), however the user can [install MongoDB locally](https://www.mongodb.com/docs/manual/administration/install-on-linux/).

The speed of MongoDB requests is not critical in this project, because they are much faster than OpenAI requests. However, once OpenAI operations are accelerated (by the means descibed above or others), the databade requests can be accelerated by installing MongoDn locally et may be by using other databases.

A BSON document in MongoDB cannot excede 16 Mb [^11] and a MongoDB database cannot exceed 64 TB in size. 

## The limits related to Telegram
- From 30 tested channels, the application could not read [this channel](https://t.me/generallsvr) 

## The limits related to Vue
Vue supports web browsers compatible with ECMAScript 5

## future enhancements
As technology and misinformation tactics evolve, so will this application.
Future versions aim to:
- integrate with other messaging platforms beyond Telegram
- allow users to customize their propaganda detection parameters
- provide real-time alerts to users about exceptional analysis results
- detection of the first channel to spead information
- comparison of the rusults with other projects

## Conceptual limits 
The learning and the choice of the characteristics are founded on a human subjective opinion, there's always a margin of error.

The application may help to the malefactors to adjust propagandistic messages to make them pass unnoticed.

The application doesn't aime at the deep causes of the propaganda.

# Experimentations, evolution, iterations
##Prototype Phase:
- Basic Propaganda Detection: The initial prototype was a rudimentary system that relied on keyword matching to flag potential propaganda messages. It was a simplistic approach that served as a proof of concept.
- Limited Channel Integration: The prototype was limited to a handful of Telegram channels, primarily to test the waters and understand the kind of data and challenges we would face.

## Version 1.0
- Introduction of AI: Realizing the limitations of keyword matching, I integrated basic AI models to analyze the context of messages. This significantly improved detection accuracy but had its own set of challenges, especially false positives.
- User Feedback Mechanism: I introduced a feedback mechanism where users could flag incorrect detections. This was our first step towards a self-improving system.

## OpenAI experimentations
The teste launched on two groups of channels, a propagandistic group and a non-propagandistic one (accordingly to personal intuition), shows the difference of the average trust coefficient of the two groups between 3 and 8 point:

![test](https://github.com/akostrik/stage_telegram/assets/22834202/dbc311e8-38f4-46f5-a31d-c060e9f28c1e)

Two tests on the values of the trust coefficient depending in the temperature parameter, every of the tests launched on the two groups of channels, show a tendancy of better distinction between the two groups while the temperature parameter is hier.    
| Temperature       | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|-------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| difference test 1 |  2  |  2  |  2  |  2  |  3  |  4  |  3  |  3  |  5  |  5  |  5  |
| difference test 2 |  1  |  1  |  2  |  3  |  1  |  1  |  3  |  4  |  2  |  4  |  4  |

<img align="right" width="300" height="300" src="https://github.com/akostrik/stage_telegram/assets/22834202/9176b2d8-a75b-4335-8a97-80e82197579a">

Extracting of detailed information (like the main subject, the people it deals with, etc) from a message, that is "undesrstanding" of the message, didn't worked correctly because of the poor quality of the analysis. Sorry for the example in Russian.

The comparaison of paires of messages directly via OpenAI (instead of extracting the principal information in the form of affirmations) demands O(N<sup>2</sup>) operations and so is too long (see [log example](https://github.com/akostrik/stage_telegram/blob/main/server1/log/log_2023_09_28_18h08%20ERROR%20LIMITE%20GPT4.txt)).

The direct question to OpenAI, _Is there any marks of the propagande in this message?_, didn't work correctly.

The classifying of the channes into groups according to their subject didn't prove to be useful in this project.

## Other experimentations
Keeping of a part of the data in the application memory, and not in the database : because the application has no acces to the results of the previous executions 

Elasticsearch ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

Distances euclidienne, jaccard, cos, ... ![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

![#f03c15](https://placehold.co/15x15/f03c15/f03c15.png)

# Welcome
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
[^9]: https://www.codeinwp.com/blog/angular-vs-vue-vs-react/#gref
[^10]: https://nodejs.org/en/about
[^11]: https://www.mongodb.com/docs/manual/reference/limits/
[^12]: https://deepgram.com/learn/the-underdog-revolution-how-smaller-language-models-outperform-llms 
[^13]: Telegram is an application similar to WhatApp, Viber, Signal, etc. Its particularities are that it has a lot of channels (a channel is a one-way broadcast tool) on different subjects, chiefly in Russian, with little censorship.  
