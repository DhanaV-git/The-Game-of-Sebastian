# Automatic Sebastian game player
# B551 Fall 2020
# @bkavuri  @nvveer  @srichala
#
# Based on skeleton code by D. Crandall
#
#
# This is the file you should modify to create your new smart player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#

from SebastianState import Dice
from SebastianState import Scorecard
import random
class SebastianAutoPlayer:

      def __init__(self):
            pass

      def score(self,dice,scorecard):
            #instead of straight up implementing greedy search, we can also measure the possibility of wasting a category and choosing a category     (Ended up going with maximizing the score)
            #check all the categories and end up with a max score and the category (Done)
            max_score=0
            sum=0
            dice=list(dice)
            sorted_dice=sorted(dice)
            #The below process to calculate scores from Primis to Sextus
            #can be iterated
            #for i in range(1,7):
            #      sum=0
            #      for j in dice:
            #            if j==i:
            #                  sum+=1
            #      if(max_score<sum*i):
            #            max_score=sum*i              (ended up going with non iteration version)
            counts = [dice.count(i) for i in range(1,7)]
            category=''
            lst=list(set(Scorecard.Categories) - set(scorecard.scorecard.keys()))               #To get the list of available categories
            #Primis
            if("primis" in lst):                                                                #Checking if this particular category is available
                  for i in dice:
                        if i==1:
                              sum=sum+1
                  if(max_score<sum*1):
                        max_score=sum*1                                                         #storing the score in max_score variable if its the highest score as well as the name of the category
                        category="primis"
                  sum=0
            #Secundus
            if("secundus" in lst):
                  for i in dice:
                        if i==2:
                              sum=sum+1
                  if(max_score<sum*2):
                        max_score=sum*2
                        category="secundus"
                  sum=0
            #Tertium
            if("tertium" in lst):
                  for i in dice:
                        if i==3:
                              sum=sum+1
                  if(max_score<sum*3):
                        max_score=sum*3
                        category="tertium"
                  sum=0
            #Quartus
            if("quartus" in lst):
                  for i in dice:
                        if i==4:
                              sum+=1
                  if(max_score<sum*4):
                        max_score=sum*4
                        category="quartus"
                  sum=0
            #Quintus
            if("quintus" in lst):
                  for i in dice:
                        if i==5:
                              sum+=1
                  if(max_score<sum*5):
                        max_score=sum*5
                        category="quintus"
                  sum=0
            #Sextus
            if("sextus" in lst):
                  for i in dice:
                        if i==6:
                              sum+=1
                  if(max_score<sum*6):
                        max_score=sum*6
                        category="sextus"
                  sum=0

            #Company
            if("company" in lst):
                  if(sorted(dice)==[1,2,3,4,5] or sorted(dice)==[2,3,4,5,6]):
                        if(max_score<40):
                              max_score=40
                              category="company"
            
            #Prattle
            if("prattle" in lst):
                  if (len(set([1,2,3,4]) - set(dice)) == 0 or len(set([2,3,4,5]) - set(dice)) == 0 or len(set([3,4,5,6]) - set(dice)) == 0):
                        if(max_score<30):
                              max_score=30
                              category="prattle"
            #add a sorted dice variable to reduce the compute time (ended up not really using it)

            #Squadron
            if("squadron" in lst):
                  if (2 in counts) and (3 in counts) and max_score<25:
                        max_score=25
                        category="squadron"
            #Triplex
            if("triplex" in lst):
                  if max(counts) >= 3:
                        total=0
                        for i in dice:
                              total+=i
                              if(max_score<total):
                                    max_score=total
                                    category="triplex"
            #Quadrupla
            if("quadrupla" in lst):
                  if max(counts) >= 4:
                        total=0
                        for i in dice:
                              total+=i
                              if(max_score<total):
                                    max_score=total
                                    category="quadrupla"
            #Quintuplicatam
            if("quintuplicatam" in lst):
                  if(sorted_dice[0]==sorted_dice[4]):                         #used sorted dice here
                        if(max_score<50):
                              max_score=50
                              category="quintuplicatam"
            #Pandemonium
            if("pandemonium" in lst):
                  total=0
                  for i in dice:
                        total+=i
                  if(max_score<total):
                        max_socre=total
                        category="pandemonium"
            return max_score,category
            #Have to implement checking algo that checks if the category is available(DONE)
            
      
      def expected_mag(self,dice,rolls,scorecard):
            dice=dice.dice
            outcome_count=0
            exp_total=0
            for dice_1 in ((dice[0],) if not rolls[0] else range(1,7)):                                                                   #This fucntion goes through every possibility of the re-roll and returns a max possible value that could be obtainted with the re-roll
                  for dice_2 in ((dice[1],) if not rolls[1] else range(1,7)):
                        for dice_3 in ((dice[2],) if not rolls[2] else range(1,7)):
                              for dice_4 in ((dice[3],) if not rolls[3] else range(1,7)):
                                    for dice_5 in ((dice[4],) if not rolls[4] else range(1,7)):
                                          #greedy search the non-empty categories?
                                          exp,cat=self.score((dice_1,dice_2,dice_3,dice_4,dice_5),scorecard)
                                          exp_total+=exp
                                          outcome_count+=1
            return exp_total/outcome_count

      def first_roll(self, dice, scorecard):
            #check evaluation and decide which dice to roll
            max_exp=(0,0)
            for dice_1 in (True, False):
                  for dice_2 in (True, False):                                                                                            #followed Prof. Crandall's walkthrough on week 8 and came up with a loop for 5 dice instead of 3
                        for dice_3 in (True, False):                                                                                      #This loop allows the program to know which dice to re-roll
                              for dice_4 in (True, False):                                                                                #At the end we return a list containing the numbers of dice that need to be re rolled
                                    for dice_5 in (True, False):                                                                          #each loop iterates over Boolean values True or False indicating if we should reroll the dice or not
                                          exp_iter=self.expected_mag(dice,(dice_1,dice_2,dice_3,dice_4,dice_5),scorecard)
                                          #print(exp_iter)
                                          if exp_iter > max_exp[0]:
                                                max_exp=(exp_iter,(dice_1,dice_2,dice_3,dice_4,dice_5))                                   #we call the expected_mag fucntion to know the maximum score we could get with that re-roll
            #create an if statement if the die should be re rerolled or not

            #if it has to be rerolled add the numbers to an empty list so that even if no numbers are added we can return an empty list
            roll=[]
            for i in range(len(max_exp[1])):                                                                                              #create a empty list and append which dice had True in the result
                  if(max_exp[1][i]==True):
                        roll.append(i)
            return roll                                                                                                                   #return the numbers of the dice that need to be re-rolled

      def second_roll(self, dice, scorecard):
            max_exp=(0,0)
            for dice_1 in (True, False):
                  for dice_2 in (True, False):
                        for dice_3 in (True, False):
                              for dice_4 in (True, False):
                                    for dice_5 in (True, False):
                                          exp_iter=self.expected_mag(dice,(dice_1,dice_2,dice_3,dice_4,dice_5),scorecard)
                                          if exp_iter > max_exp[0]:
                                                max_exp=(exp_iter,(dice_1,dice_2,dice_3,dice_4,dice_5))
            #create an if statement if the die should be re rerolled or not

            #if it has to be rerolled add the numbers to an empty list so that even if no numbers are added we can return an empty list
            roll=[]
            for i in range(len(max_exp[1])):
                  if(max_exp[1][i]==True):
                        roll.append(i)
            return roll
            #return [1, 2] # always re-roll second and third dice (blindly)
      
      def third_roll(self, dice, scorecard):
            dice=dice.dice
            # stupidly just randomly choose a category to put this in
            max_score,category=self.score(dice,scorecard)
            print(category)
            if(category==''):
                  return random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )                         #if the score function did not return any category we randomly assign a category to not end up with a 0 for that round and also the program breaks if no category
            return category                                                                                                         #is returned by the end of third roll
            
            #better way is to return the category along with the max_score and calculate that score
            #or maybe even better return a list of values covering all categories
            #and when a category is unavailable it will resort to the next best thing (ended up using random function because it felt like hard coding the whole thing at this point)