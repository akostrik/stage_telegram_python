# Internship carried out as part of the Master II Software Sciences and Technologies, Sorbonne University (Paris)
The project presented was developed during a 5-month internship (from April 3, 2023 to September 12, 2023) carried out with two Parisian associations operating in the sector of alternative innovation solidarity projects.

# Table of contents 
<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->
- [Internship details](#internship-details)
   * [Objectives of the internship](#objectives-of-the-internship)
   * [Context and motivation](#context-and-motivation)
   * [Presentation of projects of similar orientation ](#presentation-of-projects-of-similar-orientation)
   * [Methodology](#methodology)
   * [Acquired skills](#acquired-skills)
   * [Acknowledgements](#acknowledgements)
- [Project overview](#project-overview)
   * [Application features](#application-features)
   * [Simplified diagram of the application (except _Learning service_)](#simplified-diagram-of-the-application-except-_learning-service_)
   * [Diagram of the application in the programmer style](#diagram-of-the-application-in-the-programmer-style)
   * [Description of the application](#description-of-the-application)
      + [Application components](#application-components)
      + [Functionality](#functionality)
   * [Output example](#output-example)
- [Setup and usage](#setup-and-usage)
   * [MongoDB Atlas configuration](#mongodb-atlas-configuration)
   * [OpenAI configuration ](#openai-configuration)
   * [Telegram configuration](#telegram-configuration)
   * [`.env` file configuration ](#env-file-configuration)
   * [Setup](#setup)
   * [Compile and run](#compile-and-run)
- [Technical details of the developement](#technical-details-of-the-developement)
   * [The parameters of the application](#the-parameters-of-the-application)
   * [Computation details ](#computation-details)
   * [`Server 1` (python) details](#server-1-python-details)
   * [`Server 2` (node.js) details](#server-2-nodejs-details)
   * [`Server 3` (Vue) details](#server-3-vue-details)
   * [Asynchrony details](#asynchrony-details)
   * [Database details](#database-details)
- [Limitations and challenges ](#limitations-and-challenges)
   * [The limitations related to OpenAI](#the-limitations-related-to-openai)
   * [The limitations related to MongoDB](#the-limitations-related-to-mongodb)
   * [The limitations related to Telegram](#the-limitations-related-to-telegram)
   * [The limitations related to Vue](#the-limitations-related-to-vue)
   * [Other technical limitations](#other-technical-limitations)
   * [Conceptual limitations ](#conceptual-limitations)
- [Experimentations, evolution, future enhancements ](#experimentations-evolution-future-enhancements)
   * [Prototype Phase](#prototype-phase)
   * [Version 1.0](#version-10)
   * [Version 2.0](#version-20)
   * [Version 3.0 (Current)](#version-30-current)
   * [Future enhancements](#future-enhancements)
- [Welcome to the app ](#welcome-to-the-app)

<!-- TOC end -->

<!-- TOC --><a name="internship-details"></a>
# Internship details

<!-- TOC --><a name="objectives-of-the-internship"></a>
## Objectives of the internship
- Professional experience: Engage in full-time professional practice
- Skill development: Cultivate skills as a development engineer, focusing on real-world applications
- Career exploration: Investigate potential career trajectories, especially in computer sciences applied to societal challenges
- Hands-on learning: Immerse in new techniques, methodologies, tools, and their practical applications
- Association ethics: Grasp the ethical considerations and operational nuances of associations
- Professional adaptability: Evaluate the ability to integrate and adapt in a professional environment
- In terms of transition into the labor market: equipping yourself with the skills and experience necessary to enter the labor market smoothly

<!-- TOC --><a name="context-and-motivation"></a>
## Context and motivation
Technology has always greatly influenced social relations. Nowadays, the IT sector constitutes an exceptional tool for cooperation and co-reflection, with exceptional potential to bring about changes in the organization of daily life.

This project deals with an application [Telegram](https://telegram.org/faq?setln=en#q-what-is-telegram-what-do-i-do-here), which is a messenger similar to WhatApp, Viber, Signal, etc. Its particularity is that it has a lot of [channels](https://telegram.org/faq?setln=en#q-what-39s-the-difference-between-groups-and-channels) on different subjects, chiefly in Russian, with little censorship. 

The project is aimed at automaticalle detecting [propagandistic information](https://www.britannica.com/topic/propaganda) in the channels. In other words, it involves detecting information that may not be objective, presenting facts selectively to encourage a particular perception, or using particularly salient language to produce an emotional rather than rational response to the information.

<!-- TOC --><a name="presentation-of-projects-of-similar-orientation"></a>
## Presentation of projects of similar orientation 
- [Detecting of communities with similar ideologies by cross-channel interactions](https://medium.com/dfrlab/understanding-telegrams-ecosystem-of-far-right-channels-in-the-us-22e963c09234) by [DFRLab](https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/) (United States)
- [The project of Huan Cao (ru)](https://hightech.fm/2018/08/28/fakenews?is_ajax=1&ysclid=ln2wvj9vsp325940854), exploring activity and localization of the users, etc (China)
- Machine learning project [Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation](https://arxiv.org/abs/2203.05386) (United States)
- Machine learning project [Botometer](https://botometer.osome.iu.edu/faq#how-does-it-works)
- Machine learning project by [The Institute of Mathematical and Computing Sciences](https://cemeai.icmc.usp.br/) (Brazil)
- Machine learning project [Buster.ai](https://www.buster.ai/) (France)
- Workshops [Fever](https://fever.ai/workshop.html) (international)
- [Auxipresse](https://auxipress.be/) (Belgium)

<!-- TOC --><a name="methodology"></a>
## Methodology
The project was based on the main pillars of [Agile development method](https://en.wikipedia.org/wiki/Agile_software_development) which include requirements discovery and solution improvement through self-organizing, cross-functional teams with users. With the exception that, as part of the internship, the team of developers and the users were represented only by myself.

The approach to development followed the Scrum principles like:
- breaking work into goals to be completed within time-boxed iterations, called sprints, which were dedicated to the context study, the [large language models](https://en.wikipedia.org/wiki/Large_language_model) study, the architecture, python and its interactions with the concerned API, the datababases and elasticsearch, node.js, Vue, the report);
- bringing decision-making authority to an operational level;
- continuous feedback and flexibility; 
- evolve requirements as the project evolves.

<!-- TOC --><a name="acquired-skills"></a>
## Acquired skills
During this experience, many completely new skills were acquired such as: 
- the design of a complete application with several servers, several APIs, several external services;
- the use of programming languages (Python, node.js);
- the use of frameworks (Vue, express).

<!-- TOC --><a name="acknowledgements"></a>
## Acknowledgements
This project wouldn't have been possible without the guidance of the faculty at Sorbonne University, the feedback from early users and the continuous support from the associations.

<!-- TOC --><a name="project-overview"></a>
# Project overview

<!-- TOC --><a name="application-features"></a>
## Application features
1. Real-time Telegram messages verification by two methods:
- Scan individual messages for [propaganda markers](https://www.cairn.info/revue-questions-de-communication-2020-2-page-371.html) via [OpenAI API](https://openai.com/product);
- Analyze recent information from various channels to identify and highlight similarities, ensuring users are aware of potential echo chambers.
2. Continuous improvement:
- Feedback Loop: The application learns from its mistakes. By leveraging previous OpenAI responses, which are corrected by users, the system refines its accuracy over time.

<!-- TOC --><a name="simplified-diagram-of-the-application-except-_learning-service_"></a>
## Simplified diagram of the application (except _Learning service_)
![Capture d’écran de 2023-10-14 01-59-09](https://github.com/akostrik/stage_telegram/assets/22834202/5a86cb95-3eb7-4a32-8a0e-5cd67cd9e578)

The data are kept in [MondoDB Atlas](https://www.mongodb.com/fr-fr/cloud/atlas/lp/try4), a database in the cloud.

<!-- TOC --><a name="diagram-of-the-application-in-the-programmer-style"></a>
## Diagram of the application in the programmer style
![Capture d’écran de 2023-10-13 13-44-03](https://github.com/akostrik/stage_telegram/assets/22834202/dee875cb-3956-4fe6-894c-c82164adebf5)

<!-- TOC --><a name="description-of-the-application"></a>
## Description of the application

<!-- TOC --><a name="application-components"></a>
### Application components
[`Server 1`](https://github.com/akostrik/stage_telegram/tree/main/) in python handles real-time data streaming from Telegram, processes messages, and interacts with OpenAI for analysis.

[`Server 2`](https://github.com/akostrik/stage_telegram/tree/main/server2/server.js) in node.js manages data retrieval from MongoDB and serves it to the frontend.

[`Server 3`](https://github.com/akostrik/stage_telegram/tree/main/user_interface/src) in vue.js presents the analysed data to users in an intuitive and interactive manner.

<!-- TOC --><a name="functionality"></a>
### Functionality
1) `Server 3` gets from the web browser an identifier of Telegram channel to examine, via `Server 3` [API](https://fr.wikipedia.org/wiki/Interface_de_programmation)
1) `Server 3` transmits the channel identifier to `Server 2`, via `Server 2` API
1) `Server 2` put puts the channel identifier in the _MongoDB Atlas_ database, via the MongoDB API
1) `Server 1` permanently updates the list of the identifiers from _MongoDB Atlas_, via MongoDB API
1) `Server 1` listens to the chosen channels, via Telegram API
1) `Server 1` treats every new message, that is:
  - estimates the propaganda marks of the message, via OpenAI API
  - based on these propaganda marks, it calculates the confidence coefficient of the message
  - extracts the principal information of the new message, in the form of several affirmations, via OpenAI API
  - compares these affirmations to the recent affirmations of the other followed channels
  - stocks the message itself, the result if its analysis, updates the confidence coefficients of the channels, updates the similarity index of the channels in _MongoDB Atlas_ database, via MongoDB API
7) `Server 3` requests constantly the results of the computations from `Server 2`, via `Server 2` API
8) `Server 2` retrieves the calculation results from _MongoDB Atlas_, via MongoDB API, and sends them back to `Server 3`
9) `Server 3` transmits the results to the web browser in the form of a channel graph, where each vertex contains the channel identifier and its confidence coefficient, and each edge is the similarity index of the two channels concerned, via `Server 3` API

10) The web browser displays the graph to the user

The Learning service runs concurrently. Which means that : 
1) `Server 3` proposes to the user to correct OpenAI's previous responses in the web browser, via the `Server 3` API
1) As soon as the user provides the corrected examples, `Server 3` passes them to `Server 2`
1) `Server 2` puts the corrected examples to the database, via MongoDB API
1) `Server 1` attaches a limited number of corrected examples to every new OpenAI request 

<!-- TOC --><a name="output-example"></a>
## Output example 

![output 6](https://github.com/akostrik/stage_telegram/assets/22834202/298cab88-cca6-4585-8982-91c7f060ed7a)

Channel 1: Focuses on positive aspects of government policies (e.g., new fiscal policy, economic growth, health budget increase, reforestation program, diplomatic alliances).

Channel 2: Criticizes government policies and predicts negative outcomes (e.g., negative view on fiscal policy, economic stagnation, public spending cuts, ineffective reforestation, diplomatic tensions).

Channel 3: Presents a balanced view of government reforms (e.g., fiscal reform for all, economic recovery, education funding, positive environmental plan, strengthening international relations).

Channel 4: Criticizes some government policies, showing concern about economic stability and environmental plans.

Channel 5: Offers a divided opinion on government policies, highlighting debates and contrasting views.

![output 1+](https://github.com/akostrik/stage_telegram/assets/22834202/d88d7f54-ff08-40cc-ae85-b8b15349b44e)


<!-- TOC --><a name="setup-and-usage"></a>
# Setup and usage
The user should have a web browser compatible with [ECMAScript 5](https://www.w3schools.com/js/js_es5.asp) (for example, Internet Explorer 8 and its previous versions are not compatible with ECMAScript 5).

<!-- TOC --><a name="mongodb-atlas-configuration"></a>
## MongoDB Atlas configuration

[Create a MongoDB account](https://cloud.mongodb.com/) 

In your account, create a database by the name of `telegram`

[Import the collection](https://www.mongodb.com/docs/atlas/import/mongoimport/) `characteristics` from [this file](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/collection_characteristics.json) to the database `telegram`

Go [to the MongoDB interface](https://cloud.mongodb.com) - Database Deployments - `to add your current ip address`

Go [to the MongoDB interface](https://cloud.mongodb.com/) - Database - Connect - Drives - `to get you MongoDB connection string` 

Note: Be careful not to publish your MongoDB connection token on the internet and not to transmit it to unknown people

<!-- TOC --><a name="openai-configuration"></a>
## OpenAI configuration 

[Get your OpenAI connection token](https://platform.openai.com/account/api-keys)

Your account should have access to gpt-4 (a paying option)

Note: Be careful not to publish your OpenAI connection token on the internet and not to transmit it to unknown people

<!-- TOC --><a name="telegram-configuration"></a>
## Telegram configuration

[Get Telegram credentials api_id and api_hash ](https://my.telegram.org/auth)

During the first launching of the application, enter the phone number of your Telegram account and then, enter the confirmation code.

The application will create a [session file](https://docs.telethon.dev/en/stable/concepts/sessions.html) `anon.session` in the folder `server1` in order to you can to login without re-sending the code. 

Note: Be careful not to publish your Telegram credentials on the internet and not to transmit them to unknown people

<!-- TOC --><a name="env-file-configuration"></a>
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

Note: Be careful not to publish this file on the internet and not to transmit it to unknown people

<!-- TOC --><a name="setup"></a>
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

[Install Vue](https://v2.fr.vuejs.org/v2/guide/installation.html)

Note: `npm install` should be executed in the same folder where `package.json` file is

<!-- TOC --><a name="compile-and-run"></a>
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
cd server3
npm run dev
```

Enjoy the service http://localhost:5173/ 

<!-- TOC --><a name="technical-details-of-the-developement"></a>
# Technical details of the developement
Note : To understand this section, the reader should have basic knowledge of computer sciences terminology.

Separation of the data treatment provided by `Server 1` and the presentation functionality provided by `Server 2` and `Server 3` falls into the pattern of [Model-View-ViewModel (MVVM)](https://ru.wikipedia.org/wiki/Model-View-ViewModel).

`Server 1` and `Server 2` represent the backend functionality, while `Server 3` ensures the frontend one.

`Server 1` creates a [listening](https://superuser.com/questions/837933/how-do-web-servers-listen-to-ip-addresses-interrupt-or-polling#:~:text=Essentially%2C%20they%20use%20blocking%20I,state%20and%20runs%20other%20processes) socket on Telegram API, and then blocks while waiting for new connections, the kernel puts the processus into an interruptible sleep state and runs other processes. `Server 2` listens, by the same means, to `Server 2` API, and `Server 3` listens to `Server 3` API. 

<!-- TOC --><a name="the-parameters-of-the-application"></a>
## The parameters of the application
- Propaganda marks (`characteristics`)
- [The characteristics prompt](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20request%20characteristics) 
- [The affirmations prompt](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20reauest%20affirmations)
- [OpenAI model](https://platform.openai.com/docs/models) for a `characteristics`
- [OpenAI model](https://platform.openai.com/docs/models) for a affirmations request
- [OpenAI temperature](https://platform.openai.com/docs/api-reference/audio/createTranscription#audio/createTranscription-temperature), between 0 and 1: higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more deterministic (if set to 0, the model will use log probability to automatically increase the temperature until certain thresholds are hit)
- OpenAI request maximal length (in tokens [^1])
- Telegram message maximal length (in characters)
- The time where a message is considered as recent (in hours)

<!-- TOC --><a name="computation-details"></a>
## Computation details 

_The confidence coefficient of a message_ is the summe a points attribuated by OpenAI for all the `characteristics`.

_The confidence coefficient of a channel_ is the summe of the confidence coefficients of its messages.

_The confidence coefficient of a group of channels_ is the normalized (in the interval [0 … 100]) summe of the confidence coefficients of its channels.

_The similarity index of two channels_ equals to the number of similar affirmations contained in these channels, minus the number of opposing affiramtions.

The application executes 2 OpenAI requests par message and O(K) MongoDB requests par message, where K is the number of followed channels. Besides, it executes constantly MongoDB requests in order to integrate immediately a new channel added by the user.

<!-- TOC --><a name="server-1-python-details"></a>
## `Server 1` (python) details
The `Server 1` is written in Python, because:
- Python is well adapted to [data science projects](https://en.wikipedia.org/wiki/Data_science) because of its [specialised libraries](https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist) like `telethon`, `DateTime`, `requests`, `pymongo`, `openai`
- it is a rather easy language (partly because of its easy syntax).

<!-- TOC --><a name="server-2-nodejs-details"></a>
## `Server 2` (node.js) details
[Node.js](https://nodejs.org/en/about) is an asynchronous event-driven JavaScript runtime environment. The ability to run JavaScript code on the server is used to generate dynamic web page content before the page is sent to the user's web browser. The process never blocks, for no function in node.js directly performs I/O. The MongoDB site provides [detailed examples of node.js usage](https://www.mongodb.com/docs/drivers/node/current/usage-examples/
). So node.js matches well to deal with MongoDB (though there are also many [other possibilities](https://www.mongodb.com/docs/drivers/) to do it).

`Server 2` uses [Express](https://expressjs.com/) framework in order to set up write handlers for requestsn that is to set the port to use and the location of templates rendering the response.

<!-- TOC --><a name="server-3-vue-details"></a>
## `Server 3` (Vue) details
The choice of [Vue](https://vuejs.org/) as a framework to manipulate the DOM on the user side (considering Angular and React as its alternatives), is explained by Vue's simple syntax, its intuitive documentation and its suitability for small projects and novice developers. [^7] [^9]

Vue uses [Vite](https://vitejs.dev/), a server that monitors files as they're being edited. 

The [axios HTTP client](https://v2.fr.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html) provides browser requests to the `Server 3` API. 

And when saving the file, the web browser reloads the code being edited (only the specific part being changed) through a process called Hot Module Replacement (HMR). [^5]

The visualisation is provided by the graph visualisation library [Cytoscape](https://cytoscape.org/).

<!-- TOC --><a name="asynchrony-details"></a>
## Asynchrony details

[Asynchrony](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) refers to the actions instigated by a program that take place concurrently with program execution, without the program blocking to wait for results. In this application, many requests are affected (see the dotted arrows on the application diagram).

<!-- TOC --><a name="database-details"></a>
## Database details
A noSql database usage is explained chiefly by the changing number of the `characteristics`, as well as by changing of the `characteristics` themselves, while adjusting the application. The `characteristics` are kept in the collections `characteristics` and `messages`.

The reason for using MongoDB is its _MongoDB Atlas_ cloud database service and its popularity. The operations affecting the database of this project are simple. As a result, another noSql database would likely provide roughly the same functionality and at the same speed.

_MongoDB Atlas_ provides automatic failover, ensuring high availability, to prevent data loss. 

<!-- TOC --><a name="limitations-and-challenges"></a>
# Limitations and challenges 

The application is developed only for Linux.

<!-- TOC --><a name="the-limitations-related-to-openai"></a>
## The limitations related to OpenAI
Gpt-4 :
- treats about 5 requests per minute and represents the slowest part of the application;
- doesn't provide always the analysis of high-quality;
- is paying.

However, the [large language model](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) analysis may be improved in all these respects by the means like:
                                
| the means                       | speed    | quality  | investissement | a request cost **   |
|---------------------------------|----------|----------|----------------|---------------------|
| many powerful machines          | better   | the same | yes            | 0                   |
| many LLM accounts               | better   | the same | no             | the same            |
| cross-analysis by several LLM   | worse    | better   | no             | greater             |
| prompt design                   | the same | better   | no             | the same            |
| learning (prompt with examples) | the same | better   | no             | the same            |
| fine-tuning *                   | better ! | better ! | yes            | 0                   |

(*) for example, to train a self-hosted model (like [LLama2](https://ai.meta.com/llama/)) on a corpus proofread by humans, since it has been proven that smaller models can perform way better than larger models [^12]

(**) we consider all the LLM being paying, except self-hosted ones

OpenAI limitations make it necessary to limit the _Learning service_ of the application (5 examples or less per request) and the length of an examined message (a message is cut off beyond this length). The adjustement of this limitation [depending of the model](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) will be implemented.

<!-- TOC --><a name="the-limitations-related-to-mongodb"></a>
## The limitations related to MongoDB

The installation instructions are provided in this document only for the cloud version _MongoDB Atlas_, however the user can [install MongoDB locally](https://www.mongodb.com/docs/manual/administration/install-on-linux/).

The speed of MongoDB requests is not critical in this project, because they are much faster than OpenAI requests. However, once OpenAI operations are accelerated (by the means described above or others), the database requests can be accelerated by installing MongoDB locally and may be, by using other databases.

A BSON document in MongoDB cannot exceed 16 Mb [^11] and a MongoDB database cannot exceed 64 TB in size.

<!-- TOC --><a name="the-limitations-related-to-telegram"></a>
## The limitations related to Telegram
The application could not read [this channel](https://t.me/generallsvr).

<!-- TOC --><a name="the-limitations-related-to-vue"></a>
## The limitations related to Vue
Vue supports web browsers compatible with ECMAScript 5.

<!-- TOC --><a name="other-technical-limitations"></a>
## Other technical limitations
In addition to putting of a channel identifier added by user to MongoDB, `Server 3` should pass it directly to `Server 1` via `Server 3` API, in order to release `Server 1` from constant observation of the MongoDB collection.

Asynchrony of all MongoDB requests and OpenAI requests will be implemented.

Installation an configuration instructions are complicated, bacause usage of docker containers for them will be implemented.

<!-- TOC --><a name="conceptual-limitations"></a>
## Conceptual limitations 
The learning and the choice of the `characteristics` are  based on subjective human opinion. Therefore, there is a margin of error. 

Moreover, the application can help malefactors adjust their propaganda messages to make them go unnoticed.

Thirdly, the applicaiton doesn't aime at the deep causes of the propaganda.

<!-- TOC --><a name="experimentations-evolution-future-enhancements"></a>
# Experimentations, evolution, future enhancements 
<!-- TOC --><a name="prototype-phase"></a>
## Prototype Phase
The initial prototype relied on keyword matching to flag potential propaganda messages. It was a simplistic approach that served as a proof of concept.

<!-- TOC --><a name="version-10"></a>
## Version 1.0
<img align="right" width="300" height="300" src="https://github.com/akostrik/stage_telegram/assets/22834202/9176b2d8-a75b-4335-8a97-80e82197579a">

Integration of LLM to analyze the context of messages significantly improved detection accuracy but has its own set of challenges, especially false positives.

Indeed, the extraction of detailed information (such as the main subject, the people to whom it is addressed, etc.) from a message, which therefore affects the “understanding” of the meaning of a message, did not work correctly due to the poor quality of the analysis (see an example in Russian onthe screen shot).

The direct question to OpenAI, _Are there any propaganda marks in this message?_, also didn't work correctly.

User Feedback Mechanism, where the user could flag incorrect detections, was the first step towards a self-improving system.

Keeping the data only in the application memory, and not in the database, prevented the application from having access to the results of the previous executions. Channels identifiers was fixed directly in the code.

The experimentations were important to understand challenges to face.

<!-- TOC --><a name="version-20"></a>
## Version 2.0
Gpt-4 improved the quality of the analysis by characteristics, though extraction of affirmations via Extraction via Gpt-3, as well as via Gpt-4 without examples attached to the prompt, didn't work correctly.

The comparison of paires of messages directly via OpenAI (instead of extracting the principal information in the form of affirmations) demands O(N<sup>2</sup>) operations and proved to be too long.

The analysis of a series of messages, instead of analysing messages one by one, did not prove acceptable results.

Detecting the subject of a channel content was tested, in order to help the user to choose the channels to follow. The [clustering]((https://en.wikipedia.org/wiki/Cluster_analysis)) of channels according to their subject was postponed, as not prioritary task.

The idea of definition of a _similarity index_ of channels via [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance), [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance), [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance), [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) or [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) was postponed till the moment when the application will be fast enough to test all these approaches. 

Note: The terms _metric_ or _distance_ regarding a pair of channels should not be involved, because [the positivity axiom](https://en.wikipedia.org/wiki/Metric_space) doesn't necessarily hold true for the set of channels.

<!-- TOC --><a name="version-30-current"></a>
## Version 3.0 (Current)
Real-time analysis of messages, giving users instant feedback on the content they are consuming.

Echo chamber detection: One of the standout features of the current version is the ability to detect echo chambers, where multiple channels promote the same narrative, potentially indicating coordinated propaganda efforts.

The tests launched on two groups of channels, a propagandistic group and a non-propagandistic one (accordingly to personal intuition), shows the difference of the average confidence coefficients of the groups between 3 and 8 points:

![test](https://github.com/akostrik/stage_telegram/assets/22834202/dbc311e8-38f4-46f5-a31d-c060e9f28c1e)

Two tests on the values of the confidence coefficient depending on the temperature parameter, every of the tests launched on the two groups of channels, show a tendency of better distinction between the two groups while the temperature parameter is higher:    
| Temperature         | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| difference (test 1) |  2  |  2  |  2  |  2  |  3  |  4  |  3  |  3  |  5  |  5  |  5  |
| difference (test 2) |  1  |  1  |  2  |  3  |  1  |  1  |  3  |  4  |  2  |  4  |  4  |

Output of `Server 1` is written to the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log), in order to keep trace of all the experimentations.

<!-- TOC --><a name="future-enhancements"></a>
## Future enhancements
As technology and misinformation tactics evolve, so will this application.
Future versions aim to:
- integrate with other messaging platforms beyond Telegram
- provide real-time alerts to users about exceptional analysis results
- detection of the first channel to spread information
- comparison of the results with ones of the other projects
- customizable detection parameters: features that allow users to customise detection parameters, tailoring the system to their individual needs
  
<!-- TOC --><a name="welcome-to-the-app"></a>
# Welcome to the app 
<img align="right" width="60" height="60" src="https://github.com/akostrik/stage_telegram/assets/22834202/9d78c9d6-c4c6-4566-9e83-3dcbc02e311e"> 

[All the questions are welcome](mailto:stage.mongodb@gmail.com)

[Get help to install the application](mailto:stage.mongodb@gmail.com) 


[^1]: in English 1 token ≈ 3/4 of a word https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them 
[^3]: [https://www.scalablepath.com/front-end/vue-vs-react](https://vuejs.org/guide/introduction.html#what-is-vue)https://vuejs.org/guide/introduction.html#what-is-vue 
[^5]: https://en.wikipedia.org/wiki/Vite_(software)
[^6]: https://www.britannica.com/topic/propaganda
[^7]: https://skillbox.ru/media/code/vuejs-chto-takoe-kak-on-ustroen-i-chem-otlichaetsya-ot-react/ 
[^9]: https://www.codeinwp.com/blog/angular-vs-vue-vs-react/#gref
[^11]: https://www.mongodb.com/docs/manual/reference/limits/
[^12]: https://deepgram.com/learn/the-underdog-revolution-how-smaller-language-models-outperform-llms  
