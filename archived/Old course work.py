#importing pygame to gain acces to its functions.
import pygame

#Importing exit from sys to be used to close the window
from sys import exit

#initialise the pygame module
pygame.init()

#frame limit
clock = pygame.time.Clock()


#title
pygame.display.set_caption("a Malicous Nights")

#create the screen/window to be viewed
screen = pygame.display.set_mode((1000,600))

#class button
#thefont
main_font = pygame.font.SysFont("cambria",50)
class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
                #stores the image used as a button
		self.image = image
		#the x position of the button
		self.x_pos = x_pos
		#the y pos of the button
		self.y_pos = y_pos
		#makes the center of the rext the x and y pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		#store text
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

        #updates the image of the button
	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

        #chekcs if the button is pressed
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

        #if the mouse hoevers over the nutton the colour changes
	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "red")
		else:
			self.text = main_font.render(self.text_input, True, "white")

#buttons

button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))
button = Button(button_surface, 400, 300, "Click this!")



# keeping the screen open
while True:

    #Creating the "X" button
    #looping through all buttons to see wich had been pressed.
    for event in pygame.event.get():
        #if the button pressed matched the "X" button then
        if event.type == pygame.QUIT:
            #close the window
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            button.checkForInput(pygame.mouse.get_pos())



    
    screen.fill("white")
    #update the button
    button.update()
    button.changeColor(pygame.mouse.get_pos())
    #Update the screen
    pygame.display.update()

    #Limit fps to 30
    clock.tick(30)
    

