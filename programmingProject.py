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

#create main menu buttons

Start_button = ButtonClass.Button(350,400,Start_button_image,0.04)
Exit_button = ButtonClass.Button(650,400,Exit_button_image,0.4)
Option_button = ButtonClass.Button(20,400,Option_button_image,0.4)

#create options menu buttons
optback_button = ButtonClass.Button(0,0,optback_button_image,0.4)


while running:
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

    #options menu
    if OptionOpen == True:
        #cover the screen to remove the old buttons
        screen.fill((250,150,10))

        #create the exit back to homescreen button
        if optback_button.draw(screen):
            print("back")
            #go back 
            OptionOpen = False
        

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