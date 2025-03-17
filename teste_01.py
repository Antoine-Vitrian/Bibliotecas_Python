import pygame

pygame.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


player = pygame.Rect(300, 250, 50, 50)
clockobject = pygame.time.Clock()

def cenario():
    pygame.draw.rect(screen, (0, 0, 255), (100, 750, 1200, 10))

run = True
while run:
    
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player, border_radius= 50)
    clockobject.tick(300)
    cenario()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_UP] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN] == True:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()