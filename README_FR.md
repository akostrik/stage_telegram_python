# Stage en entreprise réalisé dans le cadre du Master II Sciences et Technologies du Logiciel, Sorbonne Université (Paris)
Le projet présenté a été développé au cours d'un stage de 5 mois (du 3 avril 2023 au 12 septembre 2023) réalisé auprès de deux associations parisiennes exerçant dans le secteur des projets solidaires d’innovation alternative.

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
# Les détails du stage

<!-- TOC --><a name="objectives-of-the-internship"></a>
## Les objectifs du stage
- développement de l’expérience professionnelle par un engagement dans une pratique professionnelle à temps plein ; 
- développement des compétences : cultiver ses compétences en tant qu'ingénieur en développement informatique, en se concentrant sur les applications du monde réel ; 
- objectifs de carrière : étudier les trajectoires de carrière potentielles, notamment dans les sciences informatiques appliquées aux défis sociétaux ; 
- en matière d’apprentissage pratique : immersion dans de nouvelles techniques, méthodologies, outils et leurs applications pratiques ; 
- concernant la dimension éthique du travail des structure d’accueil : saisir les considérations éthiques et les nuances opérationnelles des associations ; 
- en matière d’adaptabilité professionnelle : évaluer la capacité de s'intégrer et de s'adapter dans un environnement professionnel ; 
- en matière de transition sur le marché du travail : se doter des compétences et de l'expérience nécessaires pour entrer en douceur sur le marché du travail.

<!-- TOC --><a name="context-and-motivation"></a>
## Le contexte et la motivation 
La technologie a toujours grandement influencé les relations sociales. De nos jours, le secteur informatique constitue un outil exceptionnel de coopération et de co-réflexion, doté d'un potentiel exceptionnel pour apporter des changements dans l'organisation de la vie quotidienne. 

Ce projet vise à détecter de manière automatique les informations relevant de la propagande, présentes dans les chaînes [Telegram](https://telegram.org/faq?setln=en#q-what-is-telegram-what-do-i-do-here). Autrement dit, il s’agit de détecter les informations pouvant ne pas être objectives, présenter des faits de manière sélective pour encourager une perception particulière, ou utilisant un langage particulièrement marquant pour produire une réponse émotionnelle plutôt que rationnelle à l'information.

<!-- TOC --><a name="presentation-of-projects-of-similar-orientation"></a>
## Présentation de projets d'orientation similaire 
- projet de [détection des communautés ayant des idéologies similaires, par des interactions cross-cheannl](https://medium.com/dfrlab/understanding-telegrams-ecosystem-of-far-right-channels-in-the-us-22e963c09234) par le biais de [DFRLab](https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/) (États-Unis) ;
- projet de [Huan Cao (ru)](https://hightech.fm/2018/08/28/fakenews?is_ajax=1&ysclid=ln2wvj9vsp325940854), ouchant l’exploration de l'activité et de la localisation des utilisateurs etc. (Chine) ; 
- projet d'apprentissage automatique consistant à transmettre de « fausses fausses nouvelles » pour détecter les vraies fausses nouvelles, avec génération de données de formation chargées de propagande [Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation](https://arxiv.org/abs/2203.05386) (États-Unis) ;
- projet d'apprentissage automatique [Botometer](https://botometer.osome.iu.edu/faq#how-does-it-works) (États-Unis) ;
- projet d'apprentissage automatique de [l’Institut des Sciences mathématiques et informatiques](https://cemeai.icmc.usp.br/) (Brésil) ;
- projet d'apprentissage automatique [Buster.ai](https://www.buster.ai/) (France) ;
- Ateliers [Fever](https://fever.ai/workshop.html) (international) ;
- [Auxipresse](https://auxipress.be/) (Belgique).

<!-- TOC --><a name="methodology"></a>
## La méthodologie employée  
Le projet s’est fondé sur les principaux piliers des [méthodes Agile](https://en.wikipedia.org/wiki/Agile_software_development) qui incluent la découverte des exigences et l'amélioration des solutions grâce à des équipes auto-organisées et inter-fonctionnelles avec les utilisateurs. À la nuance près que, dans le cadre du stage réalisé, l'équipe de développeurs et les utilisateurs étaient représentés uniquement par moi-même.

L'approche du développement a suivi les valeurs Scrum fondamentales, à savoir : 
- diviser le travail en objectifs à réaliser au sein d'itérations temporelles appelées sprints. Les sprints étant dédiés à l'étude : du contexte, des [grands modèles de language](https://en.wikipedia.org/wiki/Large_language_model) de l'architecture, de Python et de ses interactions avec l'API concernée, des bases de données et d’elasticsearch1 en node.js, vue.js) ; 
- amener le pouvoir de décision à un niveau opérationnel ; 
- mettre en place une rétroaction continue et flexibilité ; 
- faire évoluer les exigences au fur et à mesure de l'évolution du projet.

<!-- TOC --><a name="acquired-skills"></a>
## Compétences acquises 
Au cours de cette expérience, de nombreuses compétences totalement nouvelles ont été acquises comme : la conception d'une application complète avec plusieurs serveurs, plusieurs API, plusieurs services externes ; l’utilisation de langages de programmation (Python, node.js) ; l’utilisation de frameworks (Vue, express, ...) 

<!-- TOC --><a name="acknowledgements"></a>
## Remerciements 
Ce projet n'aurait pas été possible sans l'encadrement du corps professoral de la Sorbonne Université, les retours des premiers utilisateurs et le soutien continu des associations. 

<!-- TOC --><a name="project-overview"></a>
# Aperçu du projet

<!-- TOC --><a name="application-features"></a>
## Fonctionnalités de l'application 
1. Vérification des messages Telegram en temps réel par le biais de deux méthodes : 
- l’analyse des messages individuels à la recherche de [marqueurs de propagande](https://www.cairn.info/revue-questions-de-communication-2020-2-page-371.html) via [OpenAI API](https://openai.com/product) ;
l’analyse des informations récentes provenant de différents canaux pour identifier et mettre en évidence les similitudes, en veillant à ce que les utilisateurs soient conscients des chambres d'écho potentielles 
2. Apprentissage et amélioration continue 
- Boucle de rétroaction : l'application apprend de ses erreurs. En tirant parti des précédentes réponses fournies par OpenAI, qui sont corrigées par les utilisateurs, le système affine sa précision au fil du temps.

<!-- TOC --><a name="simplified-diagram-of-the-application-except-_learning-service_"></a>
## Schéma simplifié de l'application (hors service Learning) 
![Capture d’écran de 2023-10-14 01-59-09](https://github.com/akostrik/stage_telegram/assets/22834202/5a86cb95-3eb7-4a32-8a0e-5cd67cd9e578)

<!-- TOC --><a name="diagram-of-the-application-in-the-programmer-style"></a>
## Schéma de l'application dans le style du programmeur
![Capture d’écran de 2023-10-13 13-44-03](https://github.com/akostrik/stage_telegram/assets/22834202/dee875cb-3956-4fe6-894c-c82164adebf5)

<!-- TOC --><a name="description-of-the-application"></a>
## Composantes de l'application 

<!-- TOC --><a name="application-components"></a>
### Application components
Le [`server 1`](https://github.com/akostrik/stage_telegram/tree/main/) onctionne sous Python et gère le streaming de données en temps réel, à partir de Telegram. Il traite les messages et interagit avec OpenAI pour l'analyse.

Le [`server 2`](https://github.com/akostrik/stage_telegram/tree/main/server2/server.js) fonctionne sous node.js. Il gère la récupération des données de MongoDB et les sert au frontend. 

Le [`server 3`](https://github.com/akostrik/stage_telegram/tree/main/user_interface/src) fonctionne sous vue.js.Il présente les données analysées aux utilisateurs de manière intuitive et interactive. 

<!-- TOC --><a name="functionality"></a>
### Description de l’application
1) Le `Serveur 3` obtient du navigateur Web, un identifiant du canal Telegram à examiner, via l'API du `Serveur 3`.
1) Le `Serveur 3` ttransmet l'identifiant du canal au `Serveur 2`, via l'API du `serveur 2`.
1) Le `Serveur 2` met l'identifiant du canal dans la base de données _MongoDB Atlas_ database, via l'API MongoDB. 
1) Le `Serveur 1` met à jour en permanence la liste des identifiants de MongoDB Atlas, via l'API MongoDB. 
1) Le `Serveur 1` écoute les chaînes choisies, via l'API Telegram. 
1) Le `Serveur 1` traite chaque nouveau message. Cela signifie que le Serveur 1 : 
- estime les marqueurs de la propagande du message, via OpenAI API ; 
- qu’il calcule, à partir de ces marqueurs de la propagande, le coefficient de confiance du message ; 
- puis qu’il extrait les principales informations du nouveau message, sous forme de plusieurs affirmations, via l'API OpenAI ; 
- ensuite il compare ces affirmations aux affirmations récentes des autres chaînes suivies, et stocke le message lui-même ;
- enfin, le résultat de son analyse met à jour les coefficients de confiance des canaux mais aussi l'indice de similarité des canaux dans la base de données MongoDB Atlas, via l'API MongoDB.
7) Le `Serveur 3` demande en permanence les résultats des calculs du `Serveur 2`, via l'API du `Serveur 2`.
8) Le `Serveur 2` écupère les résultats des calculs dans MongoDB Atlas, via l'API MongoDB, et les renvoie au `Serveur 3`.
9) Le `Serveur 3` transmet les résultats au navigateur web sous la forme d'un graphe des canaux, où chaque sommet contient l'identifiant du canal et son coefficient de confiance. Chaque bord est l'indice de similarité des deux canaux concernés, via l'API du `Serveur 3`.
10) Le navigateur Web affiche le graphique à l'utilisateur. 

Le service Learning fonctionne simultanément. Ce qui signifie que :  
1) Le `Serveur 3` propose à l'utilisateur de corriger les réponses précédentes d'OpenAI dans le navigateur web, via l'API du `Serveur 3`.
1) Dès que l'utilisateur fournit les exemples corrigés, le `Serveur 3` les transmet au `Serveur 2`.
1) Le `Serveur 2` met les exemples corrigés dans la base de données, via l'API MongoDB. 
1) Le `Serveur 1`  attache un nombre limité d'exemples corrigés à chaque nouvelle requête OpenAI.

<!-- TOC --><a name="output-example"></a>
## Un exemple d'exécution 

![output 6](https://github.com/akostrik/stage_telegram/assets/22834202/298cab88-cca6-4585-8982-91c7f060ed7a)

La chaîne 1 se concentre sur les aspects positifs des politiques gouvernementales (par exemple, nouvelle politique fiscale, croissance économique, augmentation du budget de la santé, programme de reforestation, alliances diplomatiques).

La chaîne 2 critique la politique du  government et predicts negative outcomes (e.g., negative view on fiscal policy, economic stagnation, public spending cuts, ineffective reforestation, diplomatic tensions).
prédit des événements négatifs (par exemple, une vision négative de la politique budgétaire, une stagnation économique, des réductions des dépenses publiques, une reforestation inefficace, des tensions diplomatiques).

La chaîne 3 présente une vision équilibrée des réformes gouvernementales (par exemple, réforme fiscale pour tous, reprise économique, financement de l’éducation, plan environnemental positif, renforcement des relations internationales).

La chaîne 4 critique certaines politiques gouvernementales, se montrant préoccupé par la stabilité économique et les plans environnementaux.

La chaîne 5 offre une opinion partagée sur les politiques gouvernementales, mettant en lumière les débats et les points de vue contrastés.

![output 1+](https://github.com/akostrik/stage_telegram/assets/22834202/d88d7f54-ff08-40cc-ae85-b8b15349b44e)

<!-- TOC --><a name="setup-and-usage"></a>
# Configuration et utilisation 
L'utilisateur doit disposer d'un navigateur Web compatible avec [ECMAScript 5](https://www.w3schools.com/js/js_es5.asp) (ainsi, et par exemple, IE8 et ses versions précédentes ne sont pas compatibles avec ECMAScript 5).

<!-- TOC --><a name="mongodb-atlas-configuration"></a>
## Configuration de MongoDB Atlas 

[MondoDB Atlas](https://cloud.mongodb.com/) est une base de données présentée dans le cloud. 

Il faut créer un compte MongoDB.

Sur ce compte, il faut créer une base de données sous le nom de `Telegram`. 

De là, il faut [importer](https://www.mongodb.com/docs/atlas/import/mongoimport/) la collection [`caractéristics`](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/collection_characteristics.json) dans la base de données Telegram.  

Puis, il faut accéder à la section Database Deployments de [l'interface MongoDB](https://cloud.mongodb.com) et ajouter l’adresse IP (`add your current ip address`).

Puis, il faut accéder à [l'interface MongoDB](https://cloud.mongodb.com/), section `Database`, section `Connect`, section `Drives`, pour récupérer le lien de connexion MongoDB (`get you MongoDB connection string`). 

N.B. : Attention à ne pas publier le lien de connexio sur internet et à ne pas le transmettre à des personnes inconnues. 

<!-- TOC --><a name="openai-configuration"></a>
## Configuration d’OpenAI  

[Il faut récupérer le token de connexion OpenAi](https://platform.openai.com/account/api-keys).

Le compte doit avoir accès à gpt-4 (une option payante). 

N.B. : Attention à ne pas publier le token sur internet et à ne pas le transmettre à des personnes inconnues. 

<!-- TOC --><a name="telegram-configuration"></a>
## Configuration du Telegram

[Obtenez les informations d’identification Telegram api_id and api_hash](https://my.telegram.org/auth)

Lors du premier lancement de l'application, saisissez le numéro de téléphone de votre compte Telegram puis saisissez le code de confirmation. 

L'application créera un [session file](https://docs.telethon.dev/en/stable/concepts/sessions.html) `anon.session` dans le dossier `serveur1` afin que vous puissiez vous connecter sans renvoyer le code. 

N.B. Faites très attention à ne pas publier les identifiants du Telegram sur Internet et à ne pas les transmettre à des personnes inconnues. 

<!-- TOC --><a name="env-file-configuration"></a>
## Configuration du fichier `.env`. 
Mettre son token de connexion MongoDB (`MONGO`), puis le token de connexion OpenAI (`OPENAI`) et ses informations d'identification Telegram (`API_ID`, `API_HASH`) dans le fichier `server1/.env.example` : 

```
API_ID=...
API_HASH=...
OPENAI=...
MONGO=...
```
Renommez `server1/.env.example` et `server1/.env`.

Copiez `server1/.env` vers `server2/.env`.

N.B. : Attention à ne pas publier ce fichier sur internet et à ne pas le transmettre à des personnes inconnues.

<!-- TOC --><a name="setup"></a>
## Installation
[Installer python](https://www.python.org/downloads/) de la version au mmoin 3.7.1.

Installer les bibliothèques et modules Python :
```bash
pip3 install telethon
pip install DateTime
pip install requests
pip install pymongo
pip install --upgrade openai
npm install dotenv --save
```
[Installer Node et npm](https://www.mongodb.com/docs/drivers/node/current/quick-start/download-and-install/#std-label-node-quick-start-download-and-install)

[Installer Vue](https://v2.fr.vuejs.org/v2/guide/installation.html)

N.B. : `npm install` doit être exécuté dans le même dossier où se trouve le fichier `package.json`

<!-- TOC --><a name="compile-and-run"></a>
## Compiler et exécuter 

Dans le premier terminal, lancez le `Serveur 1`
```bash
python server1/server1.py
```
Dans le deuxième terminal, lancez le `Serveur 2`
```bash
node server2/server2.js
```
Dans le troisième terminal, lancez le Serveur `Serveur 3`
```bash
cd server3
npm run dev
```

Profitez du service http://localhost:5173/ 

<!-- TOC --><a name="technical-details-of-the-developement"></a>
#  Détails techniques du développement 

Pour comprendre cette section, le lecteur doit avoir des connaissances de base en terminologie informatique. 

La séparation du traitement des données fourni par le Serveur 1 et de la fonctionnalité de présentation fournie par le Serveur 2 et le Serveur 1 s'inscrit dans le [Model-View-ViewModel (MVVM)](https://ru.wikipedia.org/wiki/Model-View-ViewModel).

Le `Serveur 1` et le `Serveur 2` r représentent la fonctionnalité backend, tandis que le `Serveur 3` ssure celle du frontend. 

Le `Serveur 1` crée [un socket d'écoute](https://superuser.com/questions/837933/how-do-web-servers-listen-to-ip-addresses-interrupt-or-polling#:~:text=Essentially%2C%20they%20use%20blocking%20I,state%20and%20runs%20other%20processes) osur l'API Telegram, puis se bloque en attendant de nouvelles connexions, cela signifie que le noyau met le processus dans un état de veille interruptible, et exécute d'autres processus. 

De la même manière, le `Serveur 2` écoute l'API du `Serveur 2` et le `Serveur 3` écoute l'API du `Serveur 3`.

<!-- TOC --><a name="the-parameters-of-the-application"></a>
## Paramètres de l'application 
- les caractéristiques de la propagande (`characteristics`) ;
- [Characteristics prompt](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20request%20characteristics) ;
- [Affirmations prompt](https://github.com/akostrik/stage_telegram/blob/main/subsidiary%20files/example%20reauest%20affirmations) ;
- [OpenAI modèle](https://platform.openai.com/docs/models) pour une demande de caractéristiques ; 
- [OpenAI modèle OpenAI](https://platform.openai.com/docs/models) pour une demande d'affirmations ;
- choix de la [température](https://platform.openai.com/docs/api-reference/audio/createTranscription#audio/createTranscription-temperature) d’OpenAI, entre 0 et 1 : des valeurs plus élevées comme 0,8 rendront la sortie plus aléatoire, tandis que des valeurs plus faibles comme 0,2 la rendront plus déterministe (si elle est définie sur 0, le modèle utilisera la probabilité logarithmique pour augmenter automatiquement la température jusqu'à ce que certains seuils soient atteints) ;
- , between 0 and 1: higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more deterministic (if set to 0, the model will use log probability to automatically increase the temperature until certain thresholds are hit)
- longueur maximale de la requête OpenAI (en tokens [^1])
- longueur maximale du message sur Telegram (en nombre de caractères) ; 
- 'heure à laquelle un message est considéré comme récent (en heures). 

<!-- TOC --><a name="computation-details"></a>
## Détails du calcul 

_Le coefficient de confiance d’un message_ est la somme de points attribués par OpenAI pour chaque charactéristique ;

_Le coefficient de confiance d’une chaîne_ est la somme des coefficients de ses messages. 

_Le coefficient de confiance d’un groupe de chaînes_ est la somme normalilisée, dans l'intervalle [0 … 100], des coefficients de ses chaînes. 

_L’indice de similarité de deux canaux_ est la nombre d’affirmations similaires, delaquelle on déduit le nombre d’affirmations contraires contenues dans les deux chaînes. 

L'application exécute 2 requêtes OpenAI par message, et O(K) requêtes MongoDB par message (ici, K est le nombre de canaux suivis). 

De plus, elle exécute en permanence des requêtes MongoDB afin d'intégrer immédiatement un nouveau canal ajouté par l'utilisateur. 

<!-- TOC --><a name="server-1-python-details"></a>
## Détails du Serveur 1 (Python) 
Python est bien adapté aux [projets de science des données](https://en.wikipedia.org/wiki/Data_science) grâce à ses [bibliothèques spécialisées](https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist) comme par exemple  `telethon`, `DateTime`, `requests`, `pymongo`, `openai`.
Python représente un langage plutôt simple (en partie à cause de sa syntaxe simple). 

<!-- TOC --><a name="server-2-nodejs-details"></a>
## `Server 2` (node.js) details
[Node.js](https://nodejs.org/en/about), an asynchronous event-driven JavaScript runtime environment and library, runs the application outside of the client’s web browser. No function in node.js directly performs I/O, so the process never blocks. Besides, the MongoDB site provides [detailed examples](https://www.mongodb.com/docs/drivers/node/current/usage-examples/
) of node.js usage. So node.js matches well to deal with MongoDB, though there are also many [other possibilities](https://www.mongodb.com/docs/drivers/) to do it.

`Server 2` uses [Express](https://expressjs.com/) framework in order to:
- set up write handlers for requests : thus, the Express framework defines how the application’s endpoint respond to client requests (the routing);
- set the port to use and the location of templates rendering the response.

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
