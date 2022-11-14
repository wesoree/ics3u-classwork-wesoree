def main():
    import pygame
    from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
    import time
    import random

    pygame.init()

    WIDTH = 1920
    HEIGHT = 1080
    SIZE = (WIDTH,HEIGHT)

    screen = pygame.display.set_mode(SIZE)
    clock = pygame.time.Clock()

    running = True
    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        screen.fill((255,255,255))

        redxbegin=random.randrange(1,1919)
        redxend=random.randrange(1,1919)
        redybegin=random.randrange(1,1079)
        redyend=random.randrange(1,1079)
        bluexbegin=random.randrange(1,1919)
        bluexend=random.randrange(1,1919)
        blueybegin=random.randrange(1,1079)
        blueyend=random.randrange(1,1079)
    
        pygame.draw.rect(screen, (0,0,255), (bluexbegin,blueybegin ,bluexend, blueyend))
        pygame.draw.rect(screen, (255,0,0), (redxbegin,redybegin ,redxend, redyend))

        
        pygame.display.flip()

        time.sleep(1)
        
        clock.tick(30)

    pygame.quit()

