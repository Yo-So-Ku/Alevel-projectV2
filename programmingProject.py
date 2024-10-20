#importing pygame to gain acces to its functions.
import pygame
from pygame.locals import *

#import ButtonClass
import ButtonClass

#Import Malus class
import MalusClass

#Import BasaranClass
import BasaranClass

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
doorOpen = True
camera_open = False
currentcamera = 0

#frame limit
clock = pygame.time.Clock()

#title
pygame.display.set_caption("a Malicous Nights")

#create the screen/window to be viewed
screen = pygame.display.set_mode((1000,600))

#time
counterfornight = 6000


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

officebehindv0 = pygame.image.load("mainBackgrounds/Officebehindv0.png").convert_alpha()
officebehindv1 = pygame.image.load("mainBackgrounds/Officebehindv1.jpeg").convert_alpha()
officebehindv2 = pygame.image.load("mainBackgrounds/Officebehindv2.jpeg").convert_alpha()
officebehindv3 = pygame.image.load("mainBackgrounds/Officebehindv3.jpeg").convert_alpha()
officebehindv4 = pygame.image.load("mainBackgrounds/Officebehindv4.jpeg").convert_alpha()

officescreenv1 = pygame.image.load("mainBackgrounds/Officescreen.png").convert_alpha()
officescreenv2 = pygame.image.load("mainBackgrounds/Officescreenv2.png").convert_alpha()

Cameranormal = pygame.image.load("mainBackgrounds/Camera.jpeg").convert_alpha()
Camerabad = pygame.image.load("mainBackgrounds/camerabad.jpeg").convert_alpha()
Cameravision = pygame.image.load("mainBackgrounds/Cameravision.png").convert_alpha()


#scaleing the main game images
thewon6am_image = pygame.transform.scale(won6am_image,(1000,600))
thelost6am_image = pygame.transform.scale(lost6am_image,(1000,600))

theofficebehindv0 = pygame.transform.scale(officebehindv0,(1000,600))
theofficebehindv1 = pygame.transform.scale(officebehindv1,(1000,600))
theofficebehindv2 = pygame.transform.scale(officebehindv2,(1000,600))
theofficebehindv3 = pygame.transform.scale(officebehindv3,(1000,600))
theofficebehindv4 = pygame.transform.scale(officebehindv4,(1000,600))

theofficescreenv1 = pygame.transform.scale(officescreenv1,(1000,600))
theofficescreenv2 = pygame.transform.scale(officescreenv2,(1000,600))

Cameranormal = pygame.transform.scale(Cameranormal,(1000,600))
Camerabad = pygame.transform.scale(Camerabad,(1000,600))
Cameravision = pygame.transform.scale(Cameravision,(200,90))

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
thistick = 0


#Subprogram 

#Draw test on the screen.

thisfont = pygame.font.SysFont("Arial", 30)

def write(text,font,colour,x,y):
    img = font.render(text, True, colour)
    screen.blit(img,(x,y))
#Subprogram
def Switchcamera(thecurrentcam):
    #check its not at camera 10
    if thecurrentcam != 10:
        #add to it
        return thecurrentcam + 1
    else:
        return 0



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
            #ENEMIES
            Monster1 = MalusClass.Malus(3,0)
            Monster2 = BasaranClass.Basaran(8,0)
            nightOpen = False
            mainlevel = True
        if NightButton2.draw(screen):
            print("night 2")
            #ENEMIES
            Monster1 = MalusClass.Malus(6,0)
            Monster2 = BasaranClass.Basaran(10,0)
            nightOpen = False
            mainlevel = True
        if NightButton3.draw(screen):
            print("night 3")
            #ENEMIES
            Monster1 = MalusClass.Malus(7,0)
            Monster2 = BasaranClass.Basaran(12,0)
            nightOpen = False
            mainlevel = True
        if NightButton4.draw(screen):
            print("night 4")
            #ENEMIES
            Monster1 = MalusClass.Malus(10,0)
            Monster2 = BasaranClass.Basaran(15,0)
            nightOpen = False
            mainlevel = True
        if NightButton5.draw(screen):
            print("night 5")
            #ENEMIES
            Monster1 = MalusClass.Malus(14,0)
            Monster2 = BasaranClass.Basaran(17,0)
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

        #Show the main screens 0 to 2
        if currentScreen == 0:
            #fill the screen to show the difference visually
            screen.fill((0,0,230))
            #show the office screen
            screen.blit(theofficescreenv1,(0,0))
            #show the door closed in tha case that the door is closed
            if doorOpen == False:
                #print the image onto the screen
                screen.blit(theofficescreenv2,(0,0))

            #Now for the camera.
            if camera_open == True:
                #cover the screen to test for a visual difference.
                screen.fill((0,0,230))
                screen.blit(Cameranormal,(0,0))
                screen.blit(Cameravision,(700,510))
                write(f"camera, {currentcamera}",thisfont, (0,200,200), 360,550)
                #check if the monster needs to be displayed.
                if Monster2.get_mode() == currentcamera:
                    #show the monster
                    screen.blit(Camerabad,(0,0))
                    screen.blit(Cameravision,(700,510))
                    write(f"camera, {currentcamera}",thisfont, (200,0,0), 360,550)
                


        if currentScreen == 1:
            #fill screen to show difference
            screen.fill((0,0,250))
            screen.blit(theofficebehindv0,(0,0))

            #Light button
            if (lightOn == True) and (Monster1.get_mode() == 0):
                screen.blit(theofficebehindv1,(0,0))
            if (lightOn == True) and (Monster1.get_mode() == 1):
                screen.blit(theofficebehindv2,(0,0))
            if (lightOn == True) and (Monster1.get_mode() == 2):
                screen.blit(theofficebehindv3,(0,0))
            if (lightOn == True) and (Monster1.get_mode() == 3):
                screen.blit(theofficebehindv4,(0,0))

        #####################################################
        #####################################################
        ## ## ##                                     ########
        # ####                                  #############
        # # # # #    monsters       ##  ##################### 
        # ####                                  #############
        ## ## ##                                     ########
        #####################################################
        #####################################################


        #make the promotion time more longer than 30 a second
        if (counterfornight % 120 == 0):
            Monster1.mpromotion(lightOn,counterfornight)
            Monster2.bpromotion(doorOpen,counterfornight)
            #jUMPSCARE VALUE
            if (Monster1.get_mode() == 4) or (Monster2.get_mode() == 11):
                counterfornight = -10
            if Monster2.get_mode() > 10:
                counterfornight = -10
            
        if (counterfornight % 20 == 0):
            Monster1.mdemotion(lightOn)



        # turn on light button
        # with space button
        keys = pygame.key.get_pressed()
        #checks if it was the space button
        if keys[K_SPACE] and (currentScreen == 1):
            #switch the lights
            #In order to stop the button from excessively repeating in one millisecond when the button has been pressed once.
            if pygame.time.get_ticks() - lastClicked > 150:
                lightOn = not lightOn
                print("lights been switched")
                lastClicked = pygame.time.get_ticks()
        # to switch to the left screen
        if keys[K_LEFT] and (currentScreen ==1):
            #change the current screen but not make the button spammable
            if pygame.time.get_ticks() - lastClicked > 150:
                #switch the screen
                print("screen left")
                currentScreen = 0
        # to switch to the middle screen
        if keys[K_RIGHT] and (currentScreen ==0):
            #change the current screen but not make the button spammable
            if pygame.time.get_ticks() - lastClicked > 150:
                #switch the screen
                print("screen middle")
                currentScreen = 1
        #close the door on the left screen
        if keys[K_SPACE] and (currentScreen ==0):
            if thistick > 5:
                #close the door
                thistick = 0
                print("pressed door button")
                doorOpen = not doorOpen
        if keys[K_c]:
            #open the camera
            camera_open = True
        if keys[K_v]:
            #close the camera
            camera_open = False
        thistick = thistick + 1
        if keys[K_x]:
            if thistick > 9:
                #move to the next camera
                currentcamera = Switchcamera(currentcamera)
                thistick = 0


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