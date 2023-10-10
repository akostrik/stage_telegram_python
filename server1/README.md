# Server 1 (python)
1) Listens to the Telegram channels
2) Treats a new message :
- estimates the marks of the propaganda of the message via OpenAI, basing on them calculates the trust coefficient of the message 
- so the server updates the trust coefficient of the channels
- extracts the principal information of the new message, in the form of several affirmations, via OpenAI
- compares these affirmations to the recent affirmations of the other followed channels
- so the server updates the measure of similarity of the channels
- constructs the graph of the channels, where every summit contains the id of the channel and its trust coefficient, and every edge is the measure of similarity of two channels 
  
## Setup and configuration
See the homepage of this repository

## Technical details
