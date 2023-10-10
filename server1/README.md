# Server 1 in python
## Its role
See [there](https://github.com/akostrik/stage_telegram/tree/main#the-same-scheme-of-the-appication-in-english)
  
## Setup and configuration
See [there](https://github.com/akostrik/stage_telegram/tree/main#setup-and-configuration)

## Technical details
- Every execution output is saved in the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log)

## Exprerimentations
- Extracting of information from a message 
- Comparaison of paires of messages directly via OpenAI (instead of extracting the principal information in the form of affirmations) demands O(N<sup>2</sup>) operations and so is too long (see [log example](https://github.com/akostrik/stage_telegram/blob/main/server1/log/log_2023_09_28_18h08%20ERROR%20LIMITE%20GPT4.txt)).
