# The-Game-of-Sebastian
Artificial Intelligence Game

## 1 Formulation:
Followed Prof. Crandall's walkthrough and got key insights to solve the problem and made appropriate design decisions for implementing a 5-dice game and with 13 different categories.

Implemented score function which contains code to compute the scores of all 13 different categories and give out the maximum score that the current roll could obtain and its category as well. I recycled the score function to calculate estimated scores in the chance layer of the ExpectiMiniMax, which prevented the redundancy of writing all the 13 categories again.

## 2 Working of my problem:
The program SebastianAutoPlayer.py doesn't modify much of the structure and design of the original skeleton code. The score function calculates the score of all the categories that are currently available and stores the maximum score as well as the category where we obtained the max score.

Using the category list to keep track of available categories helped me to reuse the same function to calculate the chance nodes and it further allowed me to maximize the score even further because I only create chance nodes of the categories that are available. Created the expected_mag function to calculate the maximum magnitude that a roll can obtain and help us choose the next move. The first_roll and second_roll take the dice as inputs and return if any of the dice should be rolled as a list containing the dice numbers. They utilize the expected_mag function to decide which dice to roll and return the said list. The third_roll however decides the best category to assign the role and returns the name of the category.

## 3 Difficulties faced:
I struggled to understand how to access dice values and later realized that it's a class and I can get it as a list using dice=dice.dice.

Got the names of categories wrong caused the program to end prematurely as there was no category being passed in the third roll. Corrected the names and still, the same problem persisted.

Figured that this was because some categories' condition didn't go through and the score function ended up returning an empty string as the category for third_roll function and then I reused the random category assigner line from the skeleton code to overcome this issue.
