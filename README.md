# Progueker

This project is a practice in code design. I have no other plans for it other than to experiment with different design 
patterns.

"Progueker" is a poortmanteau (poor portmanteau) of Poker and Rogue. Alternatives could be:

* Pokerogue
* Proguer
* Prokuer

Or some other combination. I am partial to the Puh-rogue-ker pronunciation, but I'm not sure those sounds actually hold
together or that the spelling of the word provides even the barest suggestion what shape to make your mouth. There is 
something about the jumble of 'p's and 'r's and 'o's and 'u's and 'g's and 'k's all mushed together that defies 
comprehension.

Just as it's mushy terrible name implies: this application has two parts.

1. This is a simulation of poker. Meaning it comprises a deck of cards and a set of rules for interpreting 
   combinations of those cards into traditionally understood 'hands'. Players take actions in turns, manipulating the shared state of the game.
   
2. This is a variation on the rogue-like genre. Meaning all aspects of the game are open to modification while maintaining coherence.

## Why?

This project presents two unique challenges.

1. Poker represents a clean balance of complexity and simplicity. As a system to model, its components are minimalistic and 
vulnerable to many different design approaches. I want to explore the advantages and disadvantages of multiple techniques 
without having to exhaust myself simulating a complex environment.
   
2. The rogue-like genre has always fascinated me and I want to learn more about the coding paradigms behind it. There is
a flexibility to the rules of a rogue-like game that imply an astonishingly dynamic backend. I want to explore what an 
   application looks like when its very foundation is modifiable during runtime.
