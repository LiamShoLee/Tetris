import pygame

class Button:
	def __init__(self, name, x, y, image, scale):
		self.name = name
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)

	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))


class surfaceButton(Button):
	def __init__(self,x,y,Surface):
		self.image = Surface
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
	

def buttonPoller(button,isAlreadyPressed):
		if button.rect.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0] == 1 and isAlreadyPressed == False:
				return True
		else: return False
