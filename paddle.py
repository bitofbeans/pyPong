import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    # paddle sprite
    
    def __init__(self, color, width, height):
        # sprite constructor
        super().__init__()
        
        # enter paddle values
        # add BG and make it transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # get dimensions
        self.rect = self.image.get_rect()

    def moveUp(self,pixels):
      self.rect.y -= pixels
      # don't go past border
      if self.rect.y < 0: self.rect.y = 0
    
    def moveDown(self,pixels):
      self.rect.y += pixels
      # don't go past border
      if self.rect.y > 400: self.rect.y = 400
