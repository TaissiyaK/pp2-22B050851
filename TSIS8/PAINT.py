import pygame
import math
pygame.init()
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
image_of_circle = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS8/circle.png')
image_of_rectangle = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS8/rectangle.png')
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
font = pygame.font.SysFont("Verdana", 15)
color = BLACK
isPressed = False
image_of_rectangle = pygame.transform.scale(image_of_rectangle, (60, 60))
image_of_circle = pygame.transform.scale(image_of_circle, (60, 60))


def draw_circle(screen, points):
    pygame.draw.circle(screen, color, (points[0][0],points[0][1]), abs(points[0][0]-points[1][0]))

running = True
while running:
    (x, y) = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_r]:
        color = RED
    if pressed[pygame.K_b]:
        color = BLUE
    if pressed[pygame.K_g]:
        color = GREEN
    if pressed[pygame.K_l]:
        color = BLACK
    if pressed[pygame.K_e]:
        color = WHITE

    for event in pygame.event.get():
        (x, y) = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
        if event.type == pygame.MOUSEBUTTONDOWN and isPressed == True and 0 < x < 200 and 0 < y < 60:
            points = []
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                points.append((x,y))
           
            draw_circle(screen,points)
        elif event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
       


    screen.blit(image_of_rectangle, (0, 0))
    screen.blit(image_of_circle, (100, 0))

    pygame.display.flip()