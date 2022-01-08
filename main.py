# initialize
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# sprites list 
allSprites = pygame.sprite.Group()
 
# add the sprites to the list of sprites
allSprites.add(paddleA)
allSprites.add(paddleB)
allSprites.add(ball)

# run until this is false
run = True
 
# clock
clock = pygame.time.Clock()
 
# game loop
while run:
    # --- event loop
    for event in pygame.event.get(): # event
        if event.type == pygame.QUIT: # event is close event
              run = False # exit loop
 
    # --- handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      paddleA.moveUp(5)
    if keys[pygame.K_s]:
      paddleA.moveDown(5)
    if keys[pygame.K_UP]:
      paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
      paddleB.moveDown(5)


    # --- game
    allSprites.update()
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 

    # check ball collisions
    if pygame.sprite.collide_mask(ball,paddleA):
      ball.bounce(paddleY=paddleA.rect.y+(paddleA.rect.height/2))
    elif pygame.sprite.collide_mask(ball,paddleB):
      ball.bounce(paddleY=paddleB.rect.y+(paddleB.rect.height/2))

    # --- render
    # clear screen
    screen.fill(BLACK)
    # draw the net
    pygame.draw.line(screen, (50,50,50), [349, 0], [349, 500], 15)
    pygame.draw.line(screen, (100,100,100), [349, 0], [349, 500], 7)

    # draw all sprites
    allSprites.draw(screen)

    # --- update screen
    pygame.display.flip()
     
    # --- tick fps
    clock.tick(60)
 
# stop engine
pygame.quit()
