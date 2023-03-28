import pygame, random

pygame.init()
WEIGHT, WIDTH = 600, 600
screen = pygame.display.set_mode((WEIGHT,WIDTH))
pygame.display.set_caption('CIRCLE')
x = 300
y = 300
step = 20
dx, dy = 0, 0
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
            pygame.quit()
 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT] and x >= 25:
        dx, dy = -1, 0
    elif pressed[pygame.K_RIGHT] and x <= 575:
        dx, dy = +1, 0
    elif pressed[pygame.K_UP] and y>= 25:
        dx, dy = 0, -1
    elif pressed[pygame.K_DOWN] and y<=575:
        dx, dy = 0, +1
    elif pressed[pygame.K_q]:
        running = False
    else:
        dx, dy = 0, 0

    x = x + dx*step
    y = y + dy*step
        
    pygame.draw.circle(
        screen,
        color=(255,0,0),
        center=(x,y),
        radius = 25,
    )
    pygame.display.flip()
    clock.tick(60)