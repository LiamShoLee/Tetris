import pygame

class Button:
	def __init__(self, name, x, y, image, scale):
		self.name = name
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.top_left = (x, y)
		self.is_pressed = False
		self.debounce = 420

	def draw(self, surface):
		surface.blit(self.image, (self.rect.x, self.rect.y))

	def button_poller(self):
		if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and self.is_pressed == False and self.debounce>=400:
			self.is_pressed = True
			self.debounce = 0
			return True
		else:
			if self.debounce <= 420:
				self.debounce += 1
			self.is_pressed = False 
			return False

class SurfaceButton(Button):
	def __init__(self,name,x,y,surface):
		self.name = name
		self.image = surface
		self.rect = self.image.get_rect()
		self.rect.top_left = (x, y)
		self.is_pressed = False
		self.debounce = 420

