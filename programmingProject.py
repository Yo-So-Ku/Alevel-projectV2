#importing pygame to gain acces to its functions.
import pygame

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

Start_button = Button(200,300,Start_button_image,1)
Exit__button = Button(400,300,Exit_button_image,1)
Option_button = Button(600,300,Option_button_image,1)

#Classes

#Class button

#button class
class Button():

	def __init__(self, x, y, image, scale):
		#This is to get the width and the hight of the image being made into a button so it can be scaled
		width = image.get_width()
		height = image.get_height()
		#Using the width and hight of the image it is then multiplied by the imputted scale factor
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		#The postion on the screen where the button would be
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if (pygame.mouse.get_pressed()[0] == 1) and (self.clicked == False):
				self.clicked = True
				#Action to be returnd if this codeblock is run
				action = True
		#to stop it from repeating itself check the moment its nolonger pressed			
        if (pygame.mouse.get_pressed()[0] == 0) and (self.clicked == True):
	         self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

	     return action 





#work please