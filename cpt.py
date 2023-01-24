# pygame template
   
import pygame
from paddle import Paddle
from ball import Ball
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()
pygame.mixer.init()

WIDTH = 700
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)

pygame.font.get_fonts()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('pong')


# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.y = 200
paddleB.rect.x = 670

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
#-------------------------------
# main loop 
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveU(5)
    if keys[pygame.K_s]:
        paddleA.moveD(5)
    if keys[pygame.K_UP]:
        paddleB.moveU(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveD(5)
    # Game logic goes here  
    all_sprites_list.update()
    # GAME STATE UPDATES
    # All game math and comparisons happen here
    if ball.rect.x>=690:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1] 
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()
    # DRAWING
    screen.fill(BLACK)  # always the first drawing command

    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen) 
    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(60)
    #---------------------------


pygame.quit()