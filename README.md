# Internship in the context of Master II study at Sorbonne University (Paris) 
The project has been developed during an Internship of 5 months, from the 3d April 2023 to the 12th September 2023, realised in Paris associations.

## The objectives
- Professional experience: Engage in full-time professional practice
- Skill development: Cultivate skills as a development engineer, focusing on real-world applications
- Career exploration: Investigate potential career trajectories, especially in computer sciences applied to societal challenges
- Hands-on learning: Immerse in new techniques, methodologies, tools, and their practical applications
- Association ethics: Grasp the ethical considerations and operational nuances of associations
- Professional adaptability: Evaluate the ability to integrate and adapt in a professional environment
- Job market tеransition: Equip oneself with the skills and experience to seamlessly enter the job market

## The context and motivation
Technologiy has always greatly influenced the social relations. In particular, the present-day computer science is an exceptional tool for cooperation and co-reflection, with a huge potential to bring many changes into the people's organisation. 

This project is aimed at automaticalle detecting propagandistic information in Telegram [^13] channels. That is, the information, which may not be objective and may be selectively presenting facts to encourage a particular perception, or using loaded language to produce an emotional rather than a rational response to the information. [^6]

## Some projects of similar orientation
- [Detecting of communities with similar ideologies by cross-channel interactions](https://medium.com/dfrlab/understanding-telegrams-ecosystem-of-far-right-channels-in-the-us-22e963c09234) by [DRFLab] (https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/) (United States)
- [The project of Huan Cao (ru)](https://hightech.fm/2018/08/28/fakenews?is_ajax=1&ysclid=ln2wvj9vsp325940854), exploring activity and localization of the users, etc (China)
- Machine learning project [Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation](https://arxiv.org/abs/2203.05386) (United States)
- Machine learning project [Botometer](https://botometer.osome.iu.edu/faq#how-does-it-works)
- Machine learning project by [The Institute of Mathematical and Computing Sciences (Brazil)](https://cemeai.icmc.usp.br/)
- Machine learning project [Buster.ai](https://www.buster.ai/) (France)
- Workshops [Fever](https://fever.ai/workshop.html) (international)
- [Auxipresse](https://auxipress.be/) (Belgium)

## The methodology
The project followed the [agile practices](https://en.wikipedia.org/wiki/Agile_software_development) which include requirements discovery and solutions improvement through self-organising and cross-functional teams with the users, except that both the developers team and the users were represented by myself only.

The approach to development followed the Scrum principles like:
- to break work into goals to be completed within time-boxed iterations, called sprints, where the sprints were dedicated to the context study, the [large language models](https://en.wikipedia.org/wiki/Large_language_model) study, the architecture, python and its interactions with the concerned API, the datababases and elasticsearch, node.js, vue.js);
- bringing decision-making authority to an operational level;
- continuous feedback and flexibility; 
- changing of the requirements as the project evolves.

## Acquired competences
A lot of completely new experience was acquired, like:
- the conception of a whole application with several servers, several API, several external services;
- programming languages (python, node.js);
- frameworks (Vue, express, ...).

## Acknowledgements
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
![Capture d’écran de 2023-10-13 13-44-03](https://github.com/akostrik/stage_telegram/assets/22834202/dee875cb-3956-4fe6-894c-c82164adebf5)

## Application components
[`Server 1`](https://github.com/akostrik/stage_telegram/tree/main/) in python handles real-time data streaming from Telegram, processes messages, and interacts with OpenAI for analysis.

[`Server 2`](https://github.com/akostrik/stage_telegram/tree/main/server2/server.js) in node.js manages data retrieval from MongoDB and serves it to the frontend.

[`Server 3`](https://github.com/akostrik/stage_telegram/tree/main/user_interface/src) in vue.js presents the analysed data to users in an intuitive and interactive manner.

## Description of the application
1) `Server 3` gets from the web browser an identifier of Telegram channel to examine, via `Server 3` [API](https://fr.wikipedia.org/wiki/Interface_de_programmation)
1) `Server 3` transmet the identifier of the channel to `Server 2`, via `Server 2` API
1) `Server 2` put puts the identifier of the channel to [MongoDB Atlas database](https://www.mongodb.com/fr-fr/cloud/atlas/lp/try4), via MongoDB API
1) `Server 1` permanently updates the list of the identifiers from _MongoDB Atlas_, via MongoDB API
1) `Server 1` listens to the chosen channels, via Telegram API
1) `Server 1` treats every new message, that is:
  - estimates the marks of the propaganda of the message, via OpenAI API
  - based on these marks of the propaganda, it calculates the trust coefficient of the message
  - extracts the principal information of the new message, in the form of several affirmations, via OpenAI API
  - compares these affirmations to the recent affirmations of the other followed channels
  - stocks the message itself, the result if its analysis, updates the trust coefficients of the channels, updates the index of similarity of the channels in _MongoDB Atlas_ database, via MongoDB API
7) `Server 3` requests constantly the results of the computations from `Server 2`, via `Server 2` API
8) `Server 2` fetches the results of the computations in _MongoDB Atlas_, via MongoDB API, and returns them to `Server 3`
9) `Server 3` passes the results to the web browser in the form of a graph of the channels, where every summit contains the id of the channel and its trust coefficient, and every edge is the index of similarity of two concerned channels, via `Server 3` API
10) The web browser displays the graph to the user

Simultaneously, the _Learning service_ is working:
1) `Server 3` proposes to the user to correct OpenAI's previous responses in the web browser, via the `Server 3` API
1) As soon as the user provides the corrected examples, `Server 3` passes them to `Server 2`
1) `Server 2` puts the corrected examples to the database, via MongoDB API
1) `Server 1` attaches a limited number of corrected examples to every new OpenAI request 

# Setup and usage
The user should have a web browser compatible with ECMAScript 5 (for example, IE8 and its previous versions are  not compatible with ECMAScript 5).

## MongoDB Atlas configuration

[MondoDB Atlas](https://www.mongodb.com/fr-fr/cloud/atlas/lp/try4) in a database MongoDB in the cloud.

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

# Technical details of the developement
_To understand this section, the reader should have basic knowledge of computer sciences terminology._

Separation of the data treatment provided by `Server 1` and the presentation functionality provided by `Server 2` and `Server 3` falls into the pattern of [Model-View-ViewModel (MVVM)](https://ru.wikipedia.org/wiki/Model-View-ViewModel).

`Server 1` and `Server 2` represent the backend functionality, while `Server 3` ensures the Frontend one.

`Server 1` creates a listening socket on Telegram API, and then blocks while waiting for new connections. `Server 2` listens, by the same means, to `Server 2` API, and `Server 3` listens to `Server 3` API. It means that the kernel puts the processus into an interruptible sleep state and runs other processes. [^14]

## The parameters of the application
- The characteristics of the propaganda
- [The text of the characteristics OpenAI prompt](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20request%20characteristics) 
- [The text of the affirmations OpenAI prompt](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20reauest%20affirmations)
- OpenAI model for a characteristics request
- OpenAI model for a affirmations request
- OpenAI temperature, between 0 and 1: higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more deterministic (if set to 0, the model will use log probability to automatically increase the temperature until certain thresholds are hit [^2])
- OpenAI request maximal length (in tokens [^1])
- Telegram message maximal length (in characters)
- The time where a message is considered as recent (in hours)

## Computation details 
`The similarity index of two channels (channel1, channel2)` is the number of their similar affirmations  - the number of their opposite affirmations.

`The trust coefficient of a channel` is a number in the interval [0 … 100].

The application executes 2 OpenAI requests par message and O(K) MongoDB requests par message, where K is the number of followed channels. Besides, it executes constantly MongoDB requests in order to integrate immediately a new channel added by the user.

## `Server 1` in python details
The `Server 1` is written in Python, because:
- Python is well adapted to [data science projects](https://en.wikipedia.org/wiki/Data_science) because of its [specialised libraries];(https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist) like `telethon`, `DateTime`, `requests`, `pymongo`, `openai`
- it is a rather easy language (partly because of its easy syntax).

## `Server 2` in node.js details
[Node.js](https://nodejs.org/en/about), an asynchronous event-driven JavaScript runtime environment and library, runs the application outside of the client’s web browser. No function in node.js directly performs I/O, so the process never blocks [^10]. Besides, the MongoDB site provides [detailed examples](https://www.mongodb.com/docs/drivers/node/current/usage-examples/
) of node.js usage. So node.js matches well to deal with MongoDB, though there are also many [other possibilities](https://www.mongodb.com/docs/drivers/) to do it.

`Server 2` uses [Express](https://expressjs.com/) framework to:
- write handlers for requests: it defines routing using methods (that is to how an application’s endpoints respond to client requests) of the Express app object that correspond to HTTP methods;
- set the port to use and the location of templates rendering the response.

## `Server 3` in Vue details
[Vue](https://vuejs.org/) choice as a framework to manipulate the DOM on the user's side (regarding Angular and React as its alternatives), is explained by the simple syntax of Vue, its intuitive documentation and its pertinence for small projects and novice developers. [^7] [^9]

Vue uses [Vite](https://vitejs.dev/), a server that monitors files as they're being edited. 

An HTTP client [axios](https://v2.fr.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html) provides requests from the browser to `Server 3` API. And upon file save, the web browser reloads the code being edited (only the specific file being changed) through a process called Hot Module Replacement (HMR). [^5]

The visualisation is provided by the graph visualisation library [Cytoscape](https://cytoscape.org/).

## Asynchrony details

[Asynchrony](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) refers to the actions instigated by a program that take place concurrently with program execution, without the program blocking to wait for results. In this application, it concerns many requests (see the dotted arrows on the application diagram).

## Database details
A noSql database usage is explained chiefly by the changing number of the `characteristics`, as well as by changing of the `characteristics` themselves, while adjusting the application. The `characteristics` are kept in the collections `characteristics` and `messages`.

MongoDB usage is explained by its cloud database service _MongoDB Atlas_ and its popularity. The database operations of this project are simple, so another noSql database would probably provide about the same functionality and speed.  

_MongoDB Atlas_ provides automatic failover, ensuring high availability, to prevent data loss. 

# Limitations, challenges and future enhancements 

The application is developed only for Linux.

## The limitations related to OpenAI
Gpt-4 :
- treats about 5 requests per minute and represents the slowest part of the application,
- doesn't provide always the analysis of high-quality,
- is paying.

However, the [large language model](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) analysis may be improved in all these respects by the means like:
                                
| the means                       | speed    | quality  | investissement | cost                |
|---------------------------------|----------|----------|----------------|---------------------|
| many powerful machines          | better   | the same | yes            | greater             |
| many LLM accounts               | better   | the same | no             | greater             |
| cross-analysis by several LLM   | worse    | better   |                | the same or greater |
| prompt design                   | the same | better   | no or little   | the same            |
| learning (prompt with examples) | the same | better   | no or little   | the same            |
| fine-tuning *                   | better   | better ! | yes            | less                |

(*) for example, to train a self-hosted model (like LLama2) on a corpus proofread by humans, since it has been proven that smaller models can perform way better than larger models [^12]

OpenAI limitations make it necessary to limit the _Learning service_ of the application (5 examples or less per request) and the length of an examined message (a message is cut off beyond this length). See [The parameters of the application](https://github.com/akostrik/stage_telegram/blob/main/README.md#the-parameters-of-the-application).

## The limitations related to MongoDB

The installation instructions are provided in this document only for the cloud version _MongoDB Atlas_, however the user can [install MongoDB locally](https://www.mongodb.com/docs/manual/administration/install-on-linux/).

The speed of MongoDB requests is not critical in this project, because they are much faster than OpenAI requests. However, once OpenAI operations are accelerated (by the means described above or others), the database requests can be accelerated by installing MongoDB locally and may be, by using other databases.

A BSON document in MongoDB cannot exceed 16 Mb [^11] and a MongoDB database cannot exceed 64 TB in size.

## The limitations related to Telegram
The application could not read [this channel](https://t.me/generallsvr).

## The limitations related to Vue
Vue supports web browsers compatible with ECMAScript 5.

## Conceptual limitations 
The learning and the choice of the characteristics are founded on a human subjective opinion, where there's a margin of error.

The application may help the malefactors to adjust propagandistic messages to make them pass unnoticed.

The application doesn't aime at the deep causes of the propaganda.

# Experimentations, evolution, iterations
## Prototype Phase
The initial prototype relied on keyword matching to flag potential propaganda messages. It was a simplistic approach that served as a proof of concept.

## Version 1.0
<img align="right" width="300" height="300" src="https://github.com/akostrik/stage_telegram/assets/22834202/9176b2d8-a75b-4335-8a97-80e82197579a">

Integration of LLM to analyze the context of messages significantly improved detection accuracy but has its own set of challenges, especially false positives.

Extracting detailed information (like the main subject, the people it deals with, etc) from a message, that is "understanding" of the meaning of a message, didn't work correctly because of the poor quality of the analysis. Sorry for the example in Russian.

The direct question to OpenAI, _Is there any marks of the propaganda in this message?_, also didn't work correctly.

User Feedback Mechanism, where the user could flag incorrect detections, was the first step towards a self-improving system.

Keeping the data only in the application memory, and not in the database, prevented the application from having access to the results of the previous executions. Channels identifiers was fixed directly in the code.

The experimentations were important to understand challenges to face.

## Version 2.0
Gpt-4 improved the quality of the analysis by characteristics, though extraction of affirmations via Extraction via Gpt-3, as well as via Gpt-4 without examples attached to the prompt, didn't work correctly.

The comparison of paires of messages directly via OpenAI (instead of extracting the principal information in the form of affirmations) demands O(N<sup>2</sup>) operations and proved to be too long.

The analysis of a series of messages, instead of analysing messages one by one did not prove acceptable results.

Detecting the subject of a channel content was tested, in order to help the user to choose the channels to follow. The clustering of channels according to their subject, so [the cluster_analysis](https://en.wikipedia.org/wiki/Cluster_analysis) was postponed.

The idea of definition of a _similarity index_ of channels via [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance), [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance), [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance), [Jaccard similarity coefficient](https://en.wikipedia.org/wiki/Jaccard_index) or [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) was postponed till the moment when the application will be fast enough to test all these approaches. 

NB The terms _metric_ or _distance_ should not be involved, because the positivity axiom [^16] doesn't necessarily hold true for a set of channels.

## Version 3.0 (Current)
Real-time analysis of messages, giving users instant feedback on the content they are consuming.

Echo chamber detection: One of the standout features of the current version is the ability to detect echo chambers, where multiple channels promote the same narrative, potentially indicating coordinated propaganda efforts.

The tests launched on two groups of channels, a propagandistic group and a non-propagandistic one (accordingly to personal intuition), shows the difference of the average trust coefficients of the groups between 3 and 8 points:

![test](https://github.com/akostrik/stage_telegram/assets/22834202/dbc311e8-38f4-46f5-a31d-c060e9f28c1e)

Two tests on the values of the trust coefficient depending on the temperature parameter, every of the tests launched on the two groups of channels, show a tendency of better distinction between the two groups while the temperature parameter is higher.    
| Temperature         | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| difference (test 1) |  2  |  2  |  2  |  2  |  3  |  4  |  3  |  3  |  5  |  5  |  5  |
| difference (test 2) |  1  |  1  |  2  |  3  |  1  |  1  |  3  |  4  |  2  |  4  |  4  |

Output of `Server 1` is written to the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log), to keep trace of all the experimentations.

## Future enhancements
As technology and misinformation tactics evolve, so will this application.
Future versions aim to:
- integrate with other messaging platforms beyond Telegram
- provide real-time alerts to users about exceptional analysis results
- detection of the first channel to spread information
- comparison of the results with other projects
- customizable detection parameters: features that allow users to customise detection parameters, tailoring the system to their individual needs
- usage of docker containers for installation and configuration instructions
- in addition to transmission of a channel identifier added by user via MongoDB, `Server 3` will pass it directly to `Server 1` via `Server 3` API, in order to release `Server 1` from constant observation of the MongoDB collection
- asynchrony of all database requests and OpenAI requests
  
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
