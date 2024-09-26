#import random 
import random

#class for an enemy
class Malus():
    def __init__(self,thedifficulty,themode):
        #variables
        self.difficulty = thedifficulty
        self.mode = int(themode)
        #the higher the aggression level the more attack chances there are
        self.aggressionlevel = self.difficulty
    
    #setter and getter for aggression level

    def get_aggressionlevel(self):
        return self.aggressionlevel
    def set_aggressionlevel(self,new_aggressionlevel):
        self.aggressionlevel = new_agressionlebel
    
    #setter and getter methods for mode

    def get_mode(self):
        return self.mode
    def set_mode(new_mode):
        self.mode = new_mode

    #attack / promotion for malus

    def mpromotion (self,light_button,counterfornights):
        #if the light button. is false and a movement opportunity then promote 
        if (self.aggressionlevel > random.randint(0,21)) and (light_button == False):
            #if they are already max promoted then jumpscare
            if self.mode == 4:
                #jumpscare using the counter condition
                counterfornights = -10
                print("roar")
            elif (self.mode == 0) or (self.mode == 1) or (self.mode == 2) or (self.mode == 3):
                #increase the promotion
                self.mode = self.mode + 1
                print("walk forward")
            elif self.mode == 4:
                counterfornights = -10
                print("ROUAAAAR")

    def mdemotion(self,light_button):
        #if the light button is true and a movement opportunity arrises
        if (self.aggressionlevel < random.randint(0,21)) and (light_button == True):
            #move back a mode/ demote
            if self.mode != 0:
                self.mode = self.mode - 1
                print("run back")
