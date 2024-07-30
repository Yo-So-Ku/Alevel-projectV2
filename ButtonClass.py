import pygame


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
	    #draw button on screen
	    
				#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if (pygame.mouse.get_pressed()[0] == 1) and (self.clicked == False):
				self.clicked = True
				#Action to be returnd if this codeblock is run
				action = True

		if (pygame.mouse.get_pressed()[0] == 0):
			self.clicked = False

        #pastes the button on the screen
		surface.blit(self.image, (self.rect.x, self.rect.y))	
	    # returns true if the button is pressed
		return action 