#import random 
import random

#class for an enemy
class Basaran():
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

    #attack / promotion for basaran
    
    def bpromotion (self,door_open,counterfornights):

        #Make sure the chance to move scales to the difficulty set
        if (self.aggressionlevel > random.randint(0,21)):

            #if theyre at the camera/mode 10 and the door is open then jumpscare
            if (self.mode == 10) and (door_open == True):
                #end the night
                print("REOARR")
                self.mode = 11
                counterfornights = -10
            #Else if the door is already closed
            if (self.mode == 10) and (door_open == False):
                #move enemy back to their spawn position
                print("Back to spawn")
                self.mode = 0
            #the jump/ skip some modes/ camera condition
            if (self.mode == 1 or 4 or 7) and (door_open == False):
                #jump
                print("Leap forward")
                self.mode = self.mode + 3
            #now for the normal promotion.
            else:
                #move forward
                print("run forward")
                self.mode = self.mode + 1
