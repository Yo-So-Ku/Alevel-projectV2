#importing pygame to gain acces to its functions.
import pygame

#import ButtonClass
import ButtonClass

#Importing exit from sys to be used to close the window
from sys import exit

#initialise the pygame module
pygame.init()

#Variables:
running = True
mainMenuOpen = True
nightOpen = False
OptionOpen = False
unlockEverythingCheck = False

#frame limit
clock = pygame.time.Clock()

#title
pygame.display.set_caption("a Malicous Nights")

#create the screen/window to be viewed
screen = pygame.display.set_mode((1000,600))


# Load main menu images

Start_button_image = pygame.image.load("Images/startButton.png").convert_alpha()
Exit_button_image = pygame.image.load("Images/ExitButton.png").convert_alpha()
Option_button_image = pygame.image.load("Images/OptionButton.png").convert_alpha()

# load options menu images

optback_button_image = pygame.image.load("Images/BackButton.jpeg").convert_alpha()
unlockEverything1_image = pygame.image.load("Images/UnlockEverything1.png").convert_alpha()
unlockEverything2_image = pygame.image.load("Images/UnlockEverything2.png").convert_alpha()

# load play menu images

NightButton1_image = pygame.image.load("Images/NightButton1.png").convert_alpha()
NightButton2_image = pygame.image.load("Images/NightButton2.png").convert_alpha()
NightButton3_image = pygame.image.load("Images/NightButton3.png").convert_alpha()
NightButton4_image = pygame.image.load("Images/NightButton4.png").convert_alpha()
NightButton5_image = pygame.image.load("Images/NightButton5.png").convert_alpha()
NightButton6_image = pygame.image.load("Images/NightButton6.png").convert_alpha()

#create main menu buttons

Start_button = ButtonClass.Button(350,400,Start_button_image,0.04)
Exit_button = ButtonClass.Button(650,400,Exit_button_image,0.4)
Option_button = ButtonClass.Button(20,400,Option_button_image,0.4)

#create options menu buttons
optback_button = ButtonClass.Button(0,0,optback_button_image,0.4)
unlockEverything1_button = ButtonClass.Button(50,100,unlockEverything1_image,1)
unlockEverything2_button = ButtonClass.Button(50,100,unlockEverything2_image,1)

#create play menu buttons

NightButton1 = ButtonClass.Button(90,0,NightButton1_image,1)
NightButton2 = ButtonClass.Button(50,100,NightButton2_image,1)
NightButton3 = ButtonClass.Button(50,200,NightButton3_image,1)
NightButton4 = ButtonClass.Button(50,300,NightButton4_image,1)
NightButton5 = ButtonClass.Button(50,400,NightButton5_image,1)
NightButton6 = ButtonClass.Button(50,500,NightButton6_image,1)


while running:

    #  condition for main menu buttons to open
    if mainMenuOpen == True:
        screen.fill((220,230,240))
        #start button
        if Start_button.draw(screen):
                print("Start")
                #if pressed then the condition for the main game will start
                nightOpen = True
        #options button
        if Option_button.draw(screen):
                print("Options")
                #if pressed then the condition for options will start
                OptionOpen = True
        #exit button
        if Exit_button.draw(screen):
                print("Exit")
                #this would end the loop and close the game.
                running = False

    # options menu
    if OptionOpen == True:
        #cover the screen to remove the old buttons
        screen.fill((250,150,10))

        #create the exit back to homescreen button
        if optback_button.draw(screen):
            print("back")
            #go back 
            OptionOpen = False
        
        #the unlock everything button
        if unlockEverythingCheck = False:
            if unlockEverything1_button.draw(screen):
               print("unlock everything")
               unlockEverythingCheck = True

        #the relock everything button
        if unlockEverythingCheck = True:
            if unlockEverything2_button.draw(screen):
               print("relock everything")
               unlockEverythingCheck = False
    #Play menu
    if nightOpen == True:
        #cover the screen to remove the old buttons
        screen.fill((120,110,150))

        #create back button to homescreen
        if optback_button.draw(screen):
            print("back")
            #return to main menu
            nightOpen = False
        
        #create the level select/night buttons
        if NightButton1.draw(screen):
            print("night 1")
        if NightButton2.draw(screen):
            print("night 2")
        if NightButton3.draw(screen):
            print("night 3")
        if NightButton4.draw(screen):
            print("night 4")
        if NightButton5.draw(screen):
            print("night 5")
        #check if everything is unlocked
        if unlockEverythingCheck == True:
            if NightButton6.draw(screen):
                print("night 6")

        

    #Creating the "X" button
    #looping through all buttons to see wich had been pressed.
    for event in pygame.event.get():
        #if the button pressed matched the "X" button then
        if event.type == pygame.QUIT:
            #close the window
            running = False

    #Update the screen
    pygame.display.update()

    #Limit fps to 30
    clock.tick(30)