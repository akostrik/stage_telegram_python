# Server 1 (python)
1) Listens to the Telegram channels
2) Treats a new message :
- estimates the marks of the propaganda of the message via OpenAI, basing on them calculates the trust coefficient of the message 
- extracts the principal information of the new message, in the form of several affirmations, via OpenAI
- compares these affirmations to the recent affirmations of the other followed channels
- updates the trust coefficients of the channels and the measure of similarity of the channels
  
## Setup and configuration
See the homepage of this repository

## Technical details

## Exprerimentations
- Comparaison of paires of messages directly via OpenAI (instead of extrcacting the principal information as affirmations) demands O(N<sup>2</sup>) operations and so is too long (see [log example](https://github.com/akostrik/stage_telegram/blob/main/server1/log/log_2023_09_28_18h08%20ERROR%20LIMITE%20GPT4.txt)).
- Every execution output is saved in the [logs](https://github.com/akostrik/stage_telegram/tree/main/server1/log) 
