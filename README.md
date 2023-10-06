# python-project
Verification of the Telegram messages veracity by two methods:
1) Looking for the marks of the propaganda in a separate message
2) Comparison of the information diffused by several channels   

## Project Setup

Create file named ".env":
```sh
API_ID=... (Telegram connection)
API_HASH=... (Telegram connection)
OPENAI=... (OpenAI key)
MONGO=... (MonogDB connection string like mongodb+srv: ... @cluster0.fnbrrzu.mongodb.net/?retryWrites=true&w=majority
```

Acces to API MongoDB:
- go to https://cloud.mongodb.com 
- sign in 
- go to Database Deployments
- presse "add current ip adresse"

Create database 'telegram'

Import collection 'characteristics' from the file characteristics.json :

```sh
sudo mongoimport --db telegram --collection characteristics --file characteristics.json
```

During the first Telegram connection enter your phone and then the confirmation code.

### Compile and Run
```sh
python main.py
```
