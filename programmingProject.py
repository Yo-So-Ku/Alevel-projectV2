#importing pygame to gain acces to its functions.
import pygame
from pygame.locals import *

#import ButtonClass
import ButtonClass

#Import Malus class
import MalusClass

#Importing exit from sys to be used to close the window
from sys import exit

#initialise the pygame module
pygame.init()
######################################################################################################################
######################################################################################################################
#############    Variables:
######################################################################################################################
######################################################################################################################
running = True
mainMenuOpen = True
nightOpen = False
OptionOpen = False
unlockEverythingCheck = False
mainlevel = False
nightbeaten = False
nightlost = False
currentScreen = 1
lightOn = False

#frame limit
clock = pygame.time.Clock()

#title
pygame.display.set_caption("a Malicous Nights")

#create the screen/window to be viewed
screen = pygame.display.set_mode((1000,600))

#time
counterfornight = 600


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

#load main game images

won6am_image = pygame.image.load("Images/6am_won.jpeg").convert_alpha()
lost6am_image = pygame.image.load("Images/dead_lost.jpeg").convert_alpha()

officebehindv0 = pygame.image.load("mainBackrounds/Officebehind screen.png").convert_alpha()
officebehindv1 = pygame.image.load("mainBackrounds/Officebehindv1.jpg").convert_alpha()
officebehindv2 = pygame.image.load("mainBackrounds/Officebehindv2.jpg").convert_alpha()
officebehindv3 = pygame.image.load("mainBackrounds/Officebehindv3.jpg").convert_alpha()
officebehindv4 = pygame.image.load("mainBackrounds/Officebehindv4.jpg").convert_alpha()

#scaleing the main game images
thewon6am_image = pygame.transform.scale(won6am_image,(1000,600))
thelost6am_image = pygame.transform.scale(lost6am_image,(1000,600))

theofficebehindv0 = pygame.transform.scale(officebehindv0,(1000,600))
theofficebehindv1 = pygame.transform.scale(officebehindv1,(1000,600))
theofficebehindv2 = pygame.transform.scale(officebehindv2,(1000,600))
theofficebehindv3 = pygame.transform.scale(officebehindv3,(1000,600))
theofficebehindv4 = pygame.transform.scale(officebehindv4,(1000,600))

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

lastClicked = 0



###################################################################################################################
###################################################################################################################
###################################################################################################################
###
##             MAIN looop
###
##################################################################################################################
###################################################################################################################
###################################################################################################################

while running:

    #  condition for main menu buttons to open
    if mainMenuOpen == True:
        screen.fill((220,230,240))
        #start button
        if Start_button.draw(screen):
                print("Start")
                #if pressed then the condition for the main game will start
                nightOpen = True
                mainMenuOpen = False
        #options button
        if Option_button.draw(screen):
                print("Options")
                #if pressed then the condition for options will start
                OptionOpen = True
                mainMenuOpen = False
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
            mainMenuOpen = True
        
        #the unlock everything button
        if unlockEverythingCheck == False:
            if unlockEverything1_button.draw(screen):
               print("unlock everything")
               unlockEverythingCheck = True

        #the relock everything button
        if unlockEverythingCheck == True:
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
            mainMenuOpen = True
        
        #create the level select/night buttons
        if NightButton1.draw(screen):
            print("night 1")
            nightOpen = False
            mainlevel = True
        if NightButton2.draw(screen):
            print("night 2")
            nightOpen = False
            mainlevel = True
        if NightButton3.draw(screen):
            print("night 3")
            nightOpen = False
            mainlevel = True
        if NightButton4.draw(screen):
            print("night 4")
            nightOpen = False
            mainlevel = True
        if NightButton5.draw(screen):
            print("night 5")
            #ENEMIES
            Monster1 = MalusClass.Malus(30,0)
            nightOpen = False
            mainlevel = True
        #check if everything is unlocked
        if unlockEverythingCheck == True:
            if NightButton6.draw(screen):
                print("night 6")

    #won screen 
    if nightbeaten == True:
        screen.fill((100,100,100))
        #show the won screen
        screen.blit(thewon6am_image,(0,0))

        #create back button to homescreen
        if optback_button.draw(screen):
            print("back")
            #return to main menu
            nightbeaten = False
            mainMenuOpen = True
    
    #loose screen
    if nightlost == True:
        screen.fill((110,110,110))
        # show the lost screen
        screen.blit(thelost6am_image,(0,0))

        #create back button to homescreen
        if optback_button.draw(screen):
            print("back")
            #return to main menu
            nightlost = False
            mainMenuOpen = True

    ######################
    #main game
    ######################

    if mainlevel == True:
        screen.fill((200,200,200))

        #start a timer
        counterfornight = counterfornight - 1

        #Show the main screen

        if currentScreen == 1:
            #fill screen to show difference
            screen.fill((0,0,250))
            screen.blit(theofficebehindv0,(0,0))


            #make the promotion time more lenthier than 30 a second
            if (counterfornight % 100 == 0):
                Monster1.mpromotion(lightOn,counterfornight)
                #jUMPSCARE VALUE
                if Monster1.get_mode() == 4:
                    counterfornight = -10

            if (counterfornight % 60 == 0):
                Monster1.mdemotion(lightOn)

            #Light button
            if (lightOn == True) and (Monster1.get_mode() == 0):
                screen.blit(theofficebehindv1,(0,0))
            if (lightOn == True) and (Monster1.get_mode() == 1):
                screen.blit(theofficebehindv2,(0,0))
            if (lightOn == True) and (Monster1.get_mode() == 2):
                screen.blit(theofficebehindv3,(0,0))
            if (lightOn == True) and (Monster1.get_mode() == 3):
                screen.blit(theofficebehindv4,(0,0))

        # turn on light button
        # with space button
        keys = pygame.key.get_pressed()
        #checks if it was the space button
        if keys[K_SPACE]:
            #switch the lights
            #In order to stop the button from excessively repeating in one millisecond when the button has been pressed once.
            if pygame.time.get_ticks() - lastClicked > 110:
                lightOn = not lightOn
                print("lights been switched")
                lastClicked = pygame.time.get_ticks()


            


        #if the counter is finished end game
        if counterfornight == -1:
            print("night beaten")
            mainlevel = False
            nightbeaten = True
            counterfornight = 600
        
        #jumpscare condition
        elif counterfornight == -10:
            print("night lost")
            nightlost = True
            mainlevel = False



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