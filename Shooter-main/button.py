import pygame 

#button class
class Button():
	def __init__(self,x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

def handle_event(self, event, player):
        # Handle directional inputs for button navigation
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Move player left
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                # Move player right
                player.move_right()
            elif event.key == pygame.K_UP:
                # Jump
                player.jump()
            elif event.key == pygame.K_DOWN:
                # Sit down
                player.sit_down()
            elif event.key == pygame.K_SPACE:
                # Fire ammo
                player.fire_ammo()