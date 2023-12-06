# Stage en entreprise réalisé dans le cadre du Master II Sciences et Technologies du Logiciel, Sorbonne Université (Paris)
Le projet présenté a été développé au cours d'un stage de 5 mois (du 3 avril 2023 au 12 septembre 2023) réalisé auprès de deux associations parisiennes exerçant dans le secteur des projets solidaires.

# Table of contents 
<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->
- [L'organisation du stage](#internship-details)
   * [Les objectifs du stage](#objectives-of-the-internship)
   * [Le contexte et la motivation ](#context-and-motivation)
   * [Présentation de projets d'orientation similaire](#presentation-of-projects-of-similar-orientation)
   * [La méthodologie employée](#methodology)
   * [Compétences acquises](#acquired-skills)
   * [Remerciements](#acknowledgements)
- [Aperçu du projet](#project-overview)
   * [Fonctionnalités de l'application](#application-features)
   * [Schéma simplifié de l'application (hors service Apprentissage)](#simplified-diagram-of-the-application-except-_learning-service_)
   * [Schéma de l'application dans le style du programmeur](#diagram-of-the-application-in-the-programmer-style)
   * [Description de l'application](#description-of-the-application)
      + [Composantes](#application-components)
      + [Fonctionnement](#functionality)
   * [Output example](#output-example)
- [Configuration et utilisation](#setup-and-usage)
   * [Configuration de MongoDB Atlas](#mongodb-atlas-configuration)
   * [Configuration d’OpenAI](#openai-configuration)
   * [Configuration de Telegram](#telegram-configuration)
   * [Configuration du fichier .env.](#env-file-configuration)
   * [Installation](#setup)
   * [Compiler et exécuter](#compile-and-run)
- [Détails techniques du développement](#technical-details-of-the-developement)
   * [Paramètres de l'application](#the-parameters-of-the-application)
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
# L'organisation du stage

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
- l’analyse des informations récentes provenant de différents canaux pour identifier et mettre en évidence les similitudes, en veillant à ce que les utilisateurs soient conscients des chambres d'écho potentielles 
2. Apprentissage et amélioration continue 
- Boucle de rétroaction : l'application apprend de ses erreurs. En tirant parti des précédentes réponses fournies par OpenAI, qui sont corrigées par les utilisateurs, le système affine sa précision au fil du temps.

<!-- TOC --><a name="simplified-diagram-of-the-application-except-_learning-service_"></a>
## Schéma simplifié de l'application (hors service Learning) 
![Capture d’écran de 2023-10-14 01-59-09](https://github.com/akostrik/stage_telegram/assets/22834202/5a86cb95-3eb7-4a32-8a0e-5cd67cd9e578)

<!-- TOC --><a name="diagram-of-the-application-in-the-programmer-style"></a>
## Schéma de l'application dans le style du programmeur
![Capture d’écran de 2023-10-13 13-44-03](https://github.com/akostrik/stage_telegram/assets/22834202/dee875cb-3956-4fe6-894c-c82164adebf5)

<!-- TOC --><a name="description-of-the-application"></a>
## Description de l'application

<!-- TOC --><a name="application-components"></a>
### Composantes

Le [`Serveur 1`](https://github.com/akostrik/stage_telegram/tree/main/) fonctionne sous Python et gère le streaming de données en temps réel, à partir de Telegram. Il traite les messages et interagit avec OpenAI pour l'analyse.

Le [`Serveur 2`](https://github.com/akostrik/stage_telegram/tree/main/server2/server.js) fonctionne sous node.js. Il gère la récupération des données de MongoDB et les sert au frontend. 

Le [`Serveur 3`](https://github.com/akostrik/stage_telegram/tree/main/user_interface/src) fonctionne sous vue.js.Il présente les données analysées aux utilisateurs de manière intuitive et interactive. 

<!-- TOC --><a name="functionality"></a>
### Fonctionnement

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
- [OpenAI modèle](https://platform.openai.com/docs/models) pour une demande d'affirmations ;
- choix de la [température](https://platform.openai.com/docs/api-reference/audio/createTranscription#audio/createTranscription-temperature) d’OpenAI, entre 0 et 1 : des valeurs plus élevées comme 0,8 rendront la sortie plus aléatoire, tandis que des valeurs plus faibles comme 0,2 la rendront plus déterministe (si elle est définie sur 0, le modèle utilisera la probabilité logarithmique pour augmenter automatiquement la température jusqu'à ce que certains seuils soient atteints) ;
- longueur maximale de la requête OpenAI (en tokens [^1])
- longueur maximale du message sur Telegram (en nombre de caractères) ; 
- heure à laquelle un message est considéré comme récent (en heures). 

<!-- TOC --><a name="computation-details"></a>
## Détails du calcul 

_Le coefficient de confiance d’un message_ est la somme de points attribués par OpenAI pour chaque charactéristique ;

_Le coefficient de confiance d’une chaîne_ est la somme des coefficients de ses messages. 

_Le coefficient de confiance d’un groupe de chaînes_ est la somme normalilisée, dans l'intervalle [0 … 100], des coefficients de ses chaînes. 

_L’indice de similarité de deux canaux_ est la nombre d’affirmations similaires, delaquelle on déduit le nombre d’affirmations contraires contenues dans les deux chaînes. 

L'application exécute 2 requêtes OpenAI par message, et `O(K)` requêtes MongoDB par message (ici, `K` est le nombre de canaux suivis). 

De plus, elle exécute en permanence des requêtes MongoDB afin d'intégrer immédiatement un nouveau canal ajouté par l'utilisateur. 

<!-- TOC --><a name="server-1-python-details"></a>
## Détails du Serveur 1 (Python) 
Python est bien adapté aux [projets de science des données](https://en.wikipedia.org/wiki/Data_science) grâce à ses [bibliothèques spécialisées](https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist) comme par exemple  `telethon`, `DateTime`, `requests`, `pymongo`, `openai`.
Python représente un langage plutôt simple (en partie à cause de sa syntaxe simple). 

<!-- TOC --><a name="server-2-nodejs-details"></a>
## Détails du Serveur 2 (node.js)
[Node.js](https://nodejs.org/en/about), un environnement d'exécution JavaScript asynchrones piloté par événements, exécute l'application en dehors du navigateur Web du client. Aucune fonction dans node.js n'effectue directement les  opérations d'entrée et sortie, donc le processus n'en bloque jamais. De plus, le site MongoDB fournit des [exemples détaillés](https://www.mongodb.com/docs/drivers/node/current/usage-examples/) d'utilisation de node.js. Node.js convient donc bien à MongoDB, bien qu'il existe également de nombreuses [autres possibilités](https://www.mongodb.com/docs/drivers/) pour le faire.

Le `Serveur 2` utilise le framework [Express](https://expressjs.com/) pour  mettre en place des gestionnaires des requêtes, notamment définir le port à utiliser et l'emplacement des templates rendant la réponse.

<!-- TOC --><a name="server-3-vue-details"></a>
## Détails du Serveur 3 (Vue)

Le choix de [`Vue`](https://vuejs.org/) comme framework pour manipuler le DOM côté utilisateur (en considérant Angular et React comme des alternatives), s'explique par la syntaxe simple de Vue, sa documentation intuitive et sa pertinence pour les petits projets et les développeurs novices. [^7] [^9]

Vue utilise [Vite](https://vitejs.dev/), un serveur qui surveille les fichiers au fur et à mesure de leur modification. Un [axios HTTP client](https://v2.fr.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html) fournit des requêtes du navigateur Web à l'API du `Serveur 3`. Lors de l'enregistrement du fichier, le navigateur Web recharge le code en cours d'édition (uniquement le fichier spécifique en cours de modification) via un processus appelé [Hot Module Replacement](https://webpack.js.org/concepts/hot-module-replacement/). 

La visualisation est assurée par la bibliothèque de visualisation graphique [Cytoscape](https://cytoscape.org/).

<!-- TOC --><a name="asynchrony-details"></a>
## Détails de l'asynchronie 

[L'asynchrony](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) fait référence aux actions déclenchées par un programme qui se déroulent simultanément à l'exécution du programme, sans que le programme ne bloque pour attendre les résultats. 

Dans cette application, de nombreuses requêtes peuvent être concernées (voir les flèches en pointillés sur le schéma de l'application). 

<!-- TOC --><a name="database-details"></a>
## Détails de la base de données 

L’utilisation d'une base de données noSql s'explique principalement par l'évolution du nombre de caractéristiques, ainsi que par l'évolution des caractéristiques elles-mêmes, lors de l'ajustement de l'application. Les caractéristiques sont conservées dans les collections `caractéristics` et `messages`. 

L'utilisation de MongoDB s'explique par son service de base de données cloud MongoDB Atlas et par sa popularité. Les opérations touchant la base de données de ce projet sont simples. De ce fait, une autre base de données noSql fournirait probablement à peu près les mêmes fonctionnalités et ce, à la même vitesse. 

À noter que MongoDB Atlas fournit un sauvegarde automatique pour éviter la perte de données. 

<!-- TOC --><a name="limitations-and-challenges"></a>
# Limites, défis et améliorations futures 

## Limitations liées au système d'exploitation
L'application est développée uniquement pour Linux. 

<!-- TOC --><a name="the-limitations-related-to-openai"></a>
## Limitations liées à OpenAI 

Gpt-4 : 
- traite environ 5 requêtes par minute et représente la partie la plus lente de l'application ; 
- ne fournit pas toujours une analyse de haute qualité ; 
- est payant. 

Cependant, l'analyse par un [grand modèle de langage](https://fr.wikipedia.org/wiki/Grand_mod%C3%A8le_de_langage) peut être améliorée par le recours à des outils tels que :

                 
| outils                            | rapidité       | qualité        | investissement | le coût d'une requête ** |
|-----------------------------------|----------------|----------------|----------------|--------------------------|
| nombreuses machines puissantes    | meilleure      | égale          | oui            | 0                        |
| nombreux comptes LLM              | meilleure      | égale          | non            | égale                    |
| analyse croisée par plusieurs LLM | pire           | meilleure      | non            | plus grand               |
| prompt design                     | égale          | meilleure      | non            | égale                    |
| apprentissage                     | égale          | meilleure      | non            | égale                    |
| fine-tuning *                     | bien meilleure | bien meilleure | oui            | 0                        |

(*) par exemple, pour entraîner un modèle auto-hébergé (comme LLama2) sur un corpus relu par des humains, car il a été prouvé que des modèles plus petits peuvent être bien plus performants que des modèles plus grands [^12]

(**) en considératnt que tous les LLM sont payants, sauf ceux auto-hébergé

Les limitations d'OpenAI obligent à limiter le service Apprentissage de l'application (5 exemples ou moins par requête) et la longueur d'un message examiné (un message est coupé au-delà de cette longueur). 

<!-- TOC --><a name="the-limitations-related-to-mongodb"></a>
## Limitations liées à MongoDB 

Les instructions d'installation sont fournies dans ce document uniquement pour la version cloud MongoDB Atlas. Cependant l'utilisateur peut [installer MongoDB localement](https://www.mongodb.com/docs/manual/administration/install-on-linux/). 

La vitesse des requêtes MongoDB n'est pas un point de critique dans ce projet, car elles sont beaucoup plus rapides que les requêtes OpenAI. Cependant, es requêtes de base de données peuvent être accélérées en installant MongoDB localement. 

Un document BSON dans MongoDB ne peut pas dépasser 16 Mo et une base de données MongoDB ne peut pas dépasser 64 To.

<!-- TOC --><a name="the-limitations-related-to-telegram"></a>
## Limitations liées à Telegram 
L'application n'a pas pu lire  [cette chaîne](https://t.me/generallsvr).

<!-- TOC --><a name="the-limitations-related-to-vue"></a>
## Limitations liées à _Vue_ 

_Vue_ prend en charge les navigateurs Web compatibles avec [ECMAScript 5](https://www.w3schools.com/js/js_es5.asp) (ainsi, et par exemple, IE8 et ses versions précédentes ne sont pas compatibles avec ECMAScript 5).

<!-- TOC --><a name="other-technical-limitations"></a>
## Autres limitations techniques 

L'application serait plus performante, si le `Serveur 3` transmettait l'identificateur d'une chaîne nouvellement ajoutée, directement au `Serveur 1`, afin de libérer le `Serveur 1` de l'observation constante de la collection MongoDB. 

L'asynchronie de toutes les requêtes MongoDB et OpenAI n'a pas été implémentée. 

Les instructions d'installation et de configuration peuvent être simplifiées par l'utilisation de conteineurs Docker.

<!-- TOC --><a name="conceptual-limitations"></a>
## Limites conceptuelles  

L'apprentissage et le choix des caractéristiques sont fondés sur une opinion humaine subjective. De ce fait, il existe une marge d'erreur. 

Ainsi, l'application peut aider des « malfaiteurs » à ajuster leurs messages de propagande pour les faire passer inaperçus. 

Enfin, l'application ne vise pas les causes profondes de la propagande. 

<!-- TOC --><a name="experimentations-evolution-future-enhancements"></a>
# Expérimentations, évolution, itérations 

<!-- TOC --><a name="prototype-phase"></a>
## Phase prototype 

Le prototype initial reposait sur la correspondance de mots clés pour signaler les messages de propagande potentiels. Il s’agissait d’une approche simpliste qui servait de preuve de concept.

<!-- TOC --><a name="version-10"></a>
## Version 1.0

<img align="right" width="300" height="300" src="https://github.com/akostrik/stage_telegram/assets/22834202/9176b2d8-a75b-4335-8a97-80e82197579a">

L'intégration de LLM pour analyser le contexte des messages a considérablement amélioré la précision de la détection. 

Cette version présente son propre ensemble de défis, notamment les faux positifs. En effet, l'extraction d'informations détaillées (comme le sujet principal, les personnes auxquelles il s'adresse, etc.) d'un message, qui touche donc la « compréhension » du sens d'un message, ne fonctionnait pas correctement en raison de la mauvaise qualité de l'analyse. 

Un essay de poser directement à OpenAIles les question de type : « Y a-t-il des marques de propagande dans ce message ? » n'a pas abouti.

Le mécanisme de retour d'information des utilisateurs, grâce auquel l'utilisateur peut signaler les détections incorrectes, constitue la première étape vers un système d'auto-amélioration. 

En outre, conserver les données uniquement dans la mémoire de l'application, et non dans la base de données, empêche l'application d'avoir accès aux résultats des exécutions précédentes. Les identifiants des chaînes ont été gardés directement dans le code. 

Ces expérimentations étaient importantes pour comprendre les défis à relever.

<!-- TOC --><a name="version-20"></a>
## Version 2.0

Gpt-4 a amélioré la qualité de l'analyse par caractéristiques, bien que l'extraction des affirmations via Extraction via Gpt-3, ainsi que via Gpt-4 sans apprentissage (les exemples joints au prompt), n’ait pas fonctionné correctement. 

La comparaison de paires de messages directement sur OpenAI (au lieu d'extraire les informations principales sous forme d'affirmations) nécessite des O(N<sup>2</sup>) opérations et s'avère trop longue. 

L’analyse d’un paquet de messages, au lieu d’analyser les messages un par un, n’a pas donné de résultats acceptables. 

La détection du sujet du contenu d'une chaîne a été testée, afin d'aider l'utilisateur à choisir les chaînes à suivre. 

Le [regroupement des chaînes](https://en.wikipedia.org/wiki/Cluster_analysis) selon leur sujet a été reporté, car il ne s'agissait pas d'une tâche prioritaire. 

L'idée de définition d'un _indice de similarité_ des canaux par le biais de [la distance Euclidienne](https://en.wikipedia.org/wiki/Euclidean_distance), de la [distance Levenshtein](https://en.wikipedia.org/wiki/Levenshtein_distance), de la [distance Damerau–Levenshtein](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance), [conefficient similarité Jaccard](https://en.wikipedia.org/wiki/Jaccard_index), [la similarité cosinus](https://en.wikipedia.org/wiki/Cosine_similarity), etc a été reportée à un temps futur où l'application sera devenue suffisamment rapide pour tester toutes ces approches. 

N.B. : Les termes « métrique » ou « distance » concernant une paire de canaux ne doivent pas être impliqués, car [l'axiome de positivité](https://en.wikipedia.org/wiki/Metric_space) n'est pas valable sur l'ensemble des canaux.

<!-- TOC --><a name="version-30-current"></a>
## Version 3.0 (actuelle) 

Analyse des messages en temps réel, donnant aux utilisateurs un retour instantané sur le contenu qu'ils consomment. 

Détection des chambres d'écho : l'une des fonctionnalités remarquables de la version actuelle est la capacité de détecter les chambres d'écho, où plusieurs canaux promeuvent le même récit, indiquant potentiellement des efforts de propagande coordonnés. 

Les tests lancés sur deux groupes de chaînes, un groupe propagandiste et un groupe non propagandiste (selon l'intuition personnelle), montrent la différence des coefficients de confiance moyens des groupes entre 3 et 8 points :

![test](https://github.com/akostrik/stage_telegram/assets/22834202/dbc311e8-38f4-46f5-a31d-c060e9f28c1e)

Deux tests sur les valeurs du coefficient de confiance en fonction du paramètre température, chacun des tests lancés sur les deux groupes de voies, montrent une tendance à une meilleure distinction entre les deux groupes lorsque le paramètre température est plus élevé.

Two tests on the values of the confidence coefficient depending on the temperature parameter, every of the tests launched on the two groups of channels, show a tendency of better distinction between the two groups while the temperature parameter is higher:    
| Température         | 0.0 | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| difference (test 1) |  2  |  2  |  2  |  2  |  3  |  4  |  3  |  3  |  5  |  5  |  5  |
| difference (test 2) |  1  |  1  |  2  |  3  |  1  |  1  |  3  |  4  |  2  |  4  |  4  |

La sortie du Serveur 1 est écrite dans les [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log), pour garder une trace de toutes les expérimentations.

<!-- TOC --><a name="future-enhancements"></a>
## Améliorations futures 

À mesure que la technologie et les tactiques de désinformation évoluent, cette application peut évoluer également. 

Les futures versions auront pour objectif de : 
- s'intégrer à d'autres plates-formes de messagerie au-delà de Telegram ; 
- fournir des alertes en temps réel aux utilisateurs sur les résultats d'analyse exceptionnels ; 
- détecter le premier canal de diffusion de l'information ; 
- comparer les résultats avec ceux d’autres projets ; 
- trouver des paramètres personnalisables de détection – avec des fonctionnalités permettant aux utilisateurs de personnaliser les paramètres de détection, en adaptant le système à leurs besoins individuels. 
    
  
<!-- TOC --><a name="welcome-to-the-app"></a>
# Bienvenue 

<img align="right" width="60" height="60" src="https://github.com/akostrik/stage_telegram/assets/22834202/9d78c9d6-c4c6-4566-9e83-3dcbc02e311e"> 

[Toutes les questions sont les bienvenues](mailto:stage.mongodb@gmail.com)

[Obtenir de l’aide pour installer l’application ](mailto:stage.mongodb@gmail.com) 

[^1]: in English 1 token ≈ 3/4 of a word https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them 
[^3]: [https://www.scalablepath.com/front-end/vue-vs-react](https://vuejs.org/guide/introduction.html#what-is-vue)https://vuejs.org/guide/introduction.html#what-is-vue 
[^5]: https://en.wikipedia.org/wiki/Vite_(software)
[^6]: https://www.britannica.com/topic/propaganda
[^7]: https://skillbox.ru/media/code/vuejs-chto-takoe-kak-on-ustroen-i-chem-otlichaetsya-ot-react/ 
[^9]: https://www.codeinwp.com/blog/angular-vs-vue-vs-react/#gref
[^12]: https://deepgram.com/learn/the-underdog-revolution-how-smaller-language-models-outperform-llms  
