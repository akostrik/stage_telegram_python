# Internship in the context of Master II study at Sorbonne University (Paris) 
The project has been developped during an Internship of 5 months, from the 3d April 2023 to the 12th September 2023, realized in Paris associations.

## The objectives
- Professional experience: Engage in full-time professional practice
- Skill development: Cultivate skills as a development engineer, focusing on real-world applications
- Career exploration: Investigate potential career trajectories, especially in computer sciences applied to societal challenges
- Hands-on learning: Immerse in new techniques, methodologies, tools, and their practical applications
- Association ethics: Grasp the ethical considerations and operational nuances of associations
- Professional adaptability: Evaluate the ability to integrate and adapt in a professional environment
- Job market tеransition: Equip oneself with the skills and experience to seamlessly enter the job market

## The context and motivation
The technologies has been always influenced greatly the social relations. In particular, the present-day computer science is an exceptional tool for cooperation and co-reflection, with a huge potential to bring many changes to the life of people. 

This project is aimed at automatical detecting of propagandistic information in Telegram [^13] channels. That is, the information, which may not be objective and may be selectively presenting facts to encourage a particular perception, or using loaded language to produce an emotional rather than a rational response to the information. [^6]

## Some projects of similar orientation
- [Detecting of communities with similar ideologies by cross-channel interactions](https://medium.com/dfrlab/understanding-telegrams-ecosystem-of-far-right-channels-in-the-us-22e963c09234) by [DRFLab] (https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/) (United States)
- [The project of Huan Cao (ru)](https://hightech.fm/2018/08/28/fakenews?is_ajax=1&ysclid=ln2wvj9vsp325940854), exploring activity and localistation of the users, etc (China)
- Machine learning project [Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation](https://arxiv.org/abs/2203.05386) (United States)
- Machine learning project [Botometer](https://botometer.osome.iu.edu/faq#how-does-it-works)
- Machine learning project by [The Institute of Mathematical and Computing Sciences (Brazil)](https://cemeai.icmc.usp.br/)
- Machine learning project [Buster.ai](https://www.buster.ai/) (France)
- Workshops [Fever](https://fever.ai/workshop.html) (international)
- [Auxipresse](https://auxipress.be/) (Belgium)

## The methodology
The project followed the [agile practices](https://en.wikipedia.org/wiki/Agile_software_development) which include requirements discovery and solutions improvement through self-organizing and cross-functional teams with the users, except that both the developpers team and the users were represented by myself only.

The approach to development followed the Scrum principes like:
- to break work into goals to be completed within time-boxed iterations, called sprints, where the sprints were dedicated to the contexte study, the [large language models](https://en.wikipedia.org/wiki/Large_language_model) sudy, the architecture, python and its interactions with the concerned API, the datababases and elasticsearch, node.js, vue.js);
- bringing decision-making authority to an operational level;
- continuous feedback and flexibility; 
- changing of the requirements as the project evolves.

## Aquired competences
A lof of completely new experience was aquired, like:
- the conception of a whole application with several servers, several API, several external services
- programming languages (python, node.js)
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

## Simplified diagram of the application (except _Learning service_)
![Capture d’écran de 2023-10-12 10-38-38](https://github.com/akostrik/stage_telegram/assets/22834202/41252982-3978-40d9-9b2b-20483566d203)

## Diagram of the application in the programmer style
![Capture d’écran de 2023-10-13 11-59-32](https://github.com/akostrik/stage_telegram/assets/22834202/a3d62bcc-3215-4064-accf-dd6ab5df59f8)

## Application components
[`Server 1`](https://github.com/akostrik/stage_telegram/tree/main/) in python handles real-time data streaming from Telegram, processes messages, and interacts with OpenAI for analysis.

[`Server 2`](https://github.com/akostrik/stage_telegram/tree/main/server2/server.js) in node.js manages data retrieval from MongoDB and serves it to the frontend.

[`Server 3`](https://github.com/akostrik/stage_telegram/tree/main/user_interface/src) in vue.js presents the analyzed data to users in an intuitive and interactive manner.

## Description of the application
1) `Server 3` gets from the web browser an identificator of Telegram channel to examinate, via `Server 3` [API](https://fr.wikipedia.org/wiki/Interface_de_programmation)
2) `Server 3` transmet the identificator of the channel to `Server 2`, via `Server 2` API
3) `Server 2` put puts the identificator of the channel to [MongoDB Atlas database](https://www.mongodb.com/fr-fr/cloud/atlas/lp/try4), via MongoDB API
4) `Server 1` permanently updates the list of the identificators from _MongoDB Atlas_, via MongoDB API
5) `Server 1` listens to the chosen channels, via Telegram API
6) `Server 1` treats every new message, that is:
- estimates the marks of the propaganda of the message, via OpenAI API
- based on these marks of the propaganda, it calculates the trust coefficient of the message
- extracts the principal information of the new message, in the form of several affirmations, via OpenAI API
- compares these affirmations to the recent affirmations of the other followed channels
- stocks the message itself, the result if its analisys, updates the trust coefficients of the channels, updates the index of similarity of the channels in _MongoDB Atlas_ database, via MongoDB API
1) `Server 3` requests conbstantly the results of the computations from `Server 2`, via `Server 2` API
1) `Server 2` fetchs the results of the computations in _MongoDB Atlas_, via MongoDB API, and returns them to `Server 3`
1) `Server 3` passes the results to the web browser in the form of a graph of the channels, where every summit contains the id of the channel and its trust coefficient, and every edge is the index of similarity of two concerned channels, via `Server 3` API
1) The web browser displays the graph to the user

Simultaneously, the _Learning service_ is working:
1) `Server 3` proposes to the user to correct OpenAI's previous responses in the web browser, via the `Server 3` API
2) As soon as the user provides the corrected examples, `Server 3` passes them to `Server 2`
3) `Server 2` puts the corrected examples to the database, via MongoDB API
4) `Server 1` attaches a limited number of corrected examples to every new OpenAI request 

# Setup and usage
The user should have a web browser compatible with ECMAScript 5 (for example, IE8 and its previous versions are  not compatible with ECMAScript 5)

## MongoDB Atlas configuration

[MondoDB Atlas](https://www.mongodb.com/fr-fr/cloud/atlas/lp/try4) in a database MongoDB the in cloud.

[Create a MongoDB account](https://cloud.mongodb.com/) 

In your account, create a database by the name of `telegram`

[Import the collection](https://www.mongodb.com/docs/atlas/import/mongoimport/) `characteristics` from [this file](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/collection_characteristics.json) to the database `telegram`

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
Put your MongoDB connection token (`MONGO`), OpenAI connection token (`OPENAI`) and Telegram credentials (`API_ID`, `API_HASH`) in the file `server1/.env.example`: 
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
[Install python](https://www.python.org/downloads/) (version >= 3.7.1)

Install python libraries and modules:
```bash
pip3 install telethon
pip install DateTime
pip install requests
pip install pymongo
pip install --upgrade openai
npm install dotenv --save
```
[Install Node and npm](https://www.mongodb.com/docs/drivers/node/current/quick-start/download-and-install/#std-label-node-quick-start-download-and-install)

Install Vue [^15]
```bash
npm install vue
```

_NB `npm install` should be executed in the same folder where `package.json` file is_

## Compile and run
In the first terminal launch `Server 1`
```bash
python server1/server1.py
```
In the second terminal launch `Server 2`
```bash
node server2/server2.js
```
In the third terminal launch `Server 3`
```bash
cd user_interface
npm run dev
```

Enjoy the service http://localhost:5173/ 

# Technical details of the deveppement
_To unserstand this section, the reader should have basic knowledge of computer sciences teminology_

Separation of the data treatment provided by `Server 1` and the presentation functoinality provided by `Server 2` and `Server 3` falls into the pattern of [Model-View-ViewModel (MVVM)](https://ru.wikipedia.org/wiki/Model-View-ViewModel).

`Server 1` and `Server 2` represent the backend functionality, while `Server 3` ensures the Frontend one.

`Server 1` creates a listening socket on Telegram API, and then blocks while waiting for new connections. `Server 2` listens, by the same means, to `Server 2` API, and `Server 3` listens to `Server 3` API. It means, than the kernel puts the processus into an interruptible sleep state and runs other processes. [^14]

## The parameters of the application
- The characteristics of the propaganda
- [The text of the characteristics OpenAI prompt](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20request%20characteristics) 
- [The text of the affirmations OpenAI prompt](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20reauest%20affirmations)
- OpenAI model for a characteristics request
- OpenAI model for a affirmations request
- OpenAI temperature, between 0 and 1: higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more deterministic (if set to 0, the model will use log probability to automatically increase the temperature until certain thresholds are hit [^2])
- OpenAI request maximal lenth (in tokens [^1])
- Telegram message maximal length (in characters)
- The time where a message is considered as recent (in hours)

## Computation details 
`The similarity index of two channels (channel1, channel2)` is the numbre of their similar affirmations  - the number of their opposite affirmations

`The trust coefficient of a channel` is a number in the interval [0 … 100]

The application executes 2 OpenAI requests par message and O(K) MongoDB requests par message, where K is the number of followed channels. Besides, it executes contanstly MongoDB requests in order to integrate immediately a new channel added by the user.

## Python details
The `Server 1` is written in Python, because:
- Python is well adapted to [data science projects](https://en.wikipedia.org/wiki/Data_science) because of its [specilised libraries](https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist) like `telethon`, `DateTime`, `requests`, `pymongo`, `openai`
- it is a rather easy language (partly becauseof its easy syntax)

## node.js details
[Node.js](https://nodejs.org/en/about), an asynchronous event-driven JavaScript runtime environment and library, runs the application outside of the client’s web browser. No function in node.js directly performs I/O, so the process never blocks [^10]. Besides, MongoDB site provides [detailes examples](https://www.mongodb.com/docs/drivers/node/current/usage-examples/
) of node.js usage. So node.js matches well to deal with MongoDB, though there are also many [other possibilities](https://www.mongodb.com/docs/drivers/) to do it.

[Express](https://expressjs.com/) Node web framework, is used by `Server 2` to:
- write handlers for requests
- set the port to use, and the location of templates that are used for rendering the response
- integrate with "view" rendering engines in order to generate responses by inserting data into templates.

Routing refers to how an application’s endpoints (URIs) respond to client requests. For an introduction to routing, see Basic routing.

You define routing using methods of the Express app object that correspond to HTTP methods; for example, app.get() to handle GET requests and app.post to handle POST requests. For a full list, see app.METHOD. You can also use app.all() to handle all HTTP methods and app.use() to specify middleware as the callback function (See Using middleware for details).

## Vue details
[Vue](https://vuejs.org/) framework choice as programming model to develop the user interface on the user's side (regarding to Angular and React as its alternatives), is explained by the simple syntax of Vue, its intuitive documentation and its pertinence for smalle projects and novice developers [^7] [^9]. Vue manipulates the DOM.

[Vite](https://vitejs.dev/), a local development server used by Vue, monitors files as they're being edited. Upon file save the web browser reloads the code being edited through a process called Hot Module Replacement (HMR) which works by reloading only the specific file being changed. [^5]

It consists of two major parts:
- A `dev` server that provides feature enhancements over native ES modules, for example HMR.
- A `build` command that bundles the code with Rollup, pre-configured to output highly optimized static assets.

a HTTP client [axios](https://v2.fr.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html) provides gets the data from `Server 2` API.

The grap is visualizated with a a graph visualization library [Cytoscape](https://cytoscape.org/).

## Asynchrony details

[Asynchrony](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) refers to the actions instigated by a program that take place concurrently with program execution, without the program blocking to wait for results. In this application, it concerns the requests to Telegram, OpenAI and MongoDB.

Telegram requests are asynchronous 

OpenAI server 1 requests are not asynchronous

MongoDB server 1 requests are not all asynchronous

Server 2 requests ...

## Database details
A noSql database usage is explained chiefly by the changing number of the `characteristics`, as well as by changing of the `characteristics` themselves, while adjusting the application (it concerns the collections `characteristics` and `messages`).

MongoDB usage is explained by its cloud database service _MongoDB Atlas_ and its popularity. The database operations of this project are simple, so another noSql databases would probably provide about the same functionnalty and speed.  

_MongoDB Atlas_ provides automatic failover, ensuring high availability, to prevent data loss. 

## Other technical details
Output of server 1 is saved in the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log)

# Limitatoins, challenges and future enhancements 

It is developped only for Linux.

## The limits related to OpenAI
Gpt-4 :
- treats about 5 requests per minute an respesents the lowest part of the appliation,
- doesn't provide always the analysis of high-quality,
- is paying.

However, the [large language model](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) analysis may be improved in all these respects by the means like:
                                
| the means                       | speed    | quality  | investissement | cost                   |
|---------------------------------|----------|----------|----------------|------------------------|
| many powerful machines          | better   | the same | yes            | increasing             |
| many LLM accounts               | better   | the same | no             | increasing             |
| cross-analysis by several LLM   | worse    | better   |                | the same or increasing |
| prompt design                   | the same | better   | no or little   | the same               |
| learning (prompt with examples) | the same | better   | no or little   | the same               |
| fine-tuning *                   | better   | better ! | yes            | decreasing             |

(*) for example, to train a self-hosted model (like LLama2) on a corpus proofread by humans, since it has been proven that smaller models can perform way better than larger models [^12]

The _Learning service_ of the application is limited to 5 examples par a request (but if the message, the examples and the OpenAI response are altogether longer than [_The maximal length of OpenAI request_]((https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application)) parameter, then it is less than 5 examples).

The length of an examined message is limited (see [The parameters of the application](https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application)), a message is cut off beyond this length.

## The limits related to MongoDB

The installation instructions are provided in this document only for the cloud version _MongoDB Atlas_, however the user can [install MongoDB locally](https://www.mongodb.com/docs/manual/administration/install-on-linux/).

The speed of MongoDB requests is not critical in this project, because they are much faster than OpenAI requests. However, once OpenAI operations are accelerated (by the means descibed above or others), the databade requests can be accelerated by installing MongoDn locally et may be by using other databases.

A BSON document in MongoDB cannot excede 16 Mb [^11] and a MongoDB database cannot exceed 64 TB in size. 

## The limits related to Telegram
- The application could not read [this channel](https://t.me/generallsvr) 

## The limits related to Vue
Vue supports web browsers compatible with ECMAScript 5

## Conceptual limits 
The learning and the choice of the characteristics are founded on a human subjective opinion, there's always a margin of error.

The application may help to the malefactors to adjust propagandistic messages to make them pass unnoticed.

The application doesn't aime at the deep causes of the propaganda.

# Experimentations, evolution, iterations
## Prototype Phase
The initial prototype relied on keyword matching to flag potential propaganda messages. It was a simplistic approach that served as a proof of concept.

The prototype was limited to the set of fixed (direclty in the code) channels, primarily to understand challenges to face.

## Version 1.0
<img align="right" width="300" height="300" src="https://github.com/akostrik/stage_telegram/assets/22834202/9176b2d8-a75b-4335-8a97-80e82197579a">

Integration of LLM to analyze the context of messages significantly improved detection accuracy but had its own set of challenges, especially false positives.

User Feedback Mechanism, where the user could flag incorrect detections, was the first step towards a self-improving system.

Extracting of detailed information (like the main subject, the people it deals with, etc) from a message, that is "undesrstanding" of the meaning of a message, didn't worked correctly because of the poor quality of the analysis. Sorry for the example in Russian.

The direct question to OpenAI, _Is there any marks of the propagande in this message?_, didn't work correctly.

Extraction of affirmations via Gpt-3 didn't work correctly.

Keeping the data in the application memory, and not in the database, preventd the application to have acces to the results of the previous executions.

## Version 2.0
Gpt-4 improved the quality of the analysis by characteristics, though extraction of affirmations via Gpt-4 without examples attached to the prompt often didn't work correctly.

The comparaison of paires of messages directly via OpenAI (instead of extracting the principal information in the form of affirmations) demands O(N<sup>2</sup>) operations and proved to be too long (see [log example](https://github.com/akostrik/stage_telegram/blob/main/server1/log/log_2023_09_28_18h08%20ERROR%20LIMITE%20GPT4.txt)).

The analysis of a series of messages, instead of analyzing messages one by one, was tested, though it did not prove acceptable results.

Detecting of the kind of channel content wss tested, helping the user to choose which channels to follow. The clasterisation of channels according to their subject, so [the cluster_analysis](https://en.wikipedia.org/wiki/Cluster_analysis) was postponed.

The idea of definition of a _similatiry index_ of channels via [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance), [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance), [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance), [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) or [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) was postponed till the moment when the application will be fast enought to test all these possibilities. The terms _metric_ or _distance_ should not be involved, because the positivity axiome [^16] doens't necessary hold true.

## Version 3.0 (Current)
Real-time analysis of messages, giving users instant feedback on the content they are consuming.

Echo chamber detection: One of the standout features of the current version is the ability to detect echo chambers, where multiple channels promote the same narrative, potentially indicating coordinated propaganda efforts.

The tests launched on two groups of channels, a propagandistic group and a non-propagandistic one (accordingly to personal intuition), shows the difference of the average trust coefficients of the groups between 3 and 8 points:

![test](https://github.com/akostrik/stage_telegram/assets/22834202/dbc311e8-38f4-46f5-a31d-c060e9f28c1e)

Two tests on the values of the trust coefficient depending in the temperature parameter, every of the tests launched on the two groups of channels, show a tendancy of better distinction between the two groups while the temperature parameter is hier.    
| Temperature         | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| difference (test 1) |  2  |  2  |  2  |  2  |  3  |  4  |  3  |  3  |  5  |  5  |  5  |
| difference (test 2) |  1  |  1  |  2  |  3  |  1  |  1  |  3  |  4  |  2  |  4  |  4  |

Constant adaptation of the _characteristics_ helps to improve the results.

Logs

## Future enhancements
As technology and misinformation tactics evolve, so will this application.
Future versions aim to:
- integrate with other messaging platforms beyond Telegram
- allow users to customize their propaganda detection parameters
- provide real-time alerts to users about exceptional analysis results
- detection of the first channel to spead information
- comparison of the rusults with other projects
- customizable detection parameters: Recognizing that propaganda can be subjective, I introduced features that allow users to customize detection parameters, tailoring the system to their individual needs
- usage of docker containers for installation and configuration instructions
- it addition to transmission of a channel identificator added by user via MongoDB, `Server 3` will pass it directly to `Server 1` via `Server 3` API, in order to release `Server 1` from constant observation of the MongoDB collection
  
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
[^14]: https://superuser.com/questions/837933/how-do-web-servers-listen-to-ip-addresses-interrupt-or-polling#:~:text=Essentially%2C%20they%20use%20blocking%20I,state%20and%20runs%20other%20processes.
[^15]: https://v2.fr.vuejs.org/v2/guide/installation.html 
[^16]: the distance between two distinct points is always positive
