#import random 
import random

#class for an enemy
class Malus():
    def __init__(self,thedifficulty,themode):
        #variables
        self.difficulty = thedifficulty
        self.mode = themode
        self.aggressionlevel = self.difficulty
    
    #setter and getter for aggression level

    def get_aggressionlevel():
        return self.aggressionlevel
    def set_aggressionlevel(self,new_aggressionlevel):
        self.aggressionlevel = new_agressionlebel
    
    #setter and getter methods for mode

    def get_mode():
        return self.get_mode
    def set_mode(new_mode):
        self.mode = new_mode

    #attacl / promotion for malus

    def mpromotion (self,light_button,counterfornights):
        #if the light button. is false and a movement opportunity then promote 
        if (self.aggressionlevel > random.randint(0,21)) and (light_button == False):
            #if they are already max promoted then jumpscare
            if self.mode > 2:
                #jumpscare using the counter condition
                counterfornights = -10
                print("roar")
            else:
                #increase the promotion
                self.mode = self.mode + 1
                print("walk forward")

    def mdemotion (self,light_button):
        #if the light button is true and a movement opportunity arrises
        if (self.aggressionlevel < random.randint(0,21)) and (light_button == True):
            #move back a mode/ demote
            if self.mode != 0:
                self.mode = self.mode - 1
                print("run back")
