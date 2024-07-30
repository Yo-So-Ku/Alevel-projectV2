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


# Load images

Start_button_image = pygame.image.load("Images/StartButton.png").convert_alpha()
Exit_button_image = pygame.image.load("Images/ExitButton.png").convert_alpha()
Option_button_image = pygame.image.load("Images/OptionButton.png").convert_alpha()

#create buttons

Start_button = ButtonClass.Button(200,300,Start_button_image,0.5)
Exit_button = ButtonClass.Button(400,300,Exit_button_image,0.5)
Option_button = ButtonClass.Button(600,300,Option_button_image,0.5)

#work please

while running:

    #Creating the "X" button
    #looping through all buttons to see wich had been pressed.
    for event in pygame.event.get():
        #if the button pressed matched the "X" button then
        if event.type == pygame.QUIT:
            #close the window
            pygame.quit() 

    screen.fill((220,230,240))

    #if its on the main menu then
    while mainMenuOpen:
        #backround
        screen.fill((220,230,240))
        #start button
        if Start_button.draw(screen):
            print("Start")
        if Exit_button.draw(screen):
            print("Exit")
        if Option_button.draw(screen):
            print("Options")