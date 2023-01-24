import pygame
BLACK = (0, 0, 0)
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, w, h):
        super().__init__()

        self.image = pygame.Surface([w, h])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.rect(self.image, color, [0, 0, w, h])

        self.rect = self.image.get_rect()
    
    def moveU(self, pixels):
        self.rect.y -= pixels
		#Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
    def moveD(self, pixels):
        self.rect.y += pixels
	#Check that you are not going too far (off the screen)
        if self.rect.y > 400:
          self.rect.y = 400