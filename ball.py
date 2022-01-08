import pygame
from random import randint
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):
    # ball sprite
    
    def __init__(self, color, width, height):
        # sprite constructor
        super().__init__()

        # enter ball values
        # add BG and make it transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4,8), randint(-8,8)]

        # get dimensions
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    
    def bounce(self,paddleY):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = (paddleY-self.rect.y)/10
        print(self.velocity[1])
        if randint(0,1) == 1: self.velocity[1] = -self.velocity[1]
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
