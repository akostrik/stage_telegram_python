# Server 1 in python
## Server 1 role
See [there](https://github.com/akostrik/stage_telegram/tree/main#the-same-scheme-of-the-appication-in-english)
  
## Server 1 setup and configuration
See [there](https://github.com/akostrik/stage_telegram/tree/main#setup-and-configuration)

## Server 1 technical details
Python is choosen for the server 1, because:
- it is well adapted to [data science projects](https://en.wikipedia.org/wiki/Data_science) because of its [specilised libraries](https://datascientest.com/top-10-des-librairies-python-pour-un-data-scientist)
- it is a rather easy language, partly because it frees the memory automatically

Every output of an execution is saved in the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log)

Python code has 5 Classes: Group, Message, Prompt_c, Prompt_a, Characteristic

## Server 1 exprerimentations that were not included in the final functionality
<img align="right" width="300" height="300" src="https://github.com/akostrik/stage_telegram/assets/22834202/9176b2d8-a75b-4335-8a97-80e82197579a">

- Extracting of detailed information from a message, like its main subject, the people it deals with, etc, that is "undesrstanding" of the message, because the analysis did not work corectly. Sorry, the example is in Russian, if you translate it, you will see the pour quality of the analysis:

- Comparaison of paires of messages directly via OpenAI (instead of extracting the principal information in the form of affirmations) demands O(N<sup>2</sup>) operations and so is too long (see [log example](https://github.com/akostrik/stage_telegram/blob/main/server1/log/log_2023_09_28_18h08%20ERROR%20LIMITE%20GPT4.txt)).

- Keeping of a part of the data in the application memory, and not in the database, because the application has no acces to the results of the previous executions 

- Extracting of the affirmations with gpt-3 didn't work
