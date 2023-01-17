# pygame template
   
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT

pygame.init()
pygame.mixer.init()

WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)

pygame.font.get_fonts()

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

circle_x = 200
circle_y = 200
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    # movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        circle_y += -10
    if keys[pygame.K_a]:
        circle_x += -10
    if keys[pygame.K_s]:
        circle_y += 10
    if keys[pygame.K_d]:
        circle_x += 10
    if keys[pygame.K_SPACE]:
        pass


    # GAME STATE UPDATES
    # All game math and comparisons happen here
    

    # DRAWING
    screen.fill(WHITE)  # always the first drawing command

    pygame.draw.circle(screen, (0, 0, 0), (circle_x, circle_y), 30)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()