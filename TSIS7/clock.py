import pygame, datetime

pygame.init()


WEIGHT, WIDTH = 600, 600
screen = pygame.display.set_mode((WEIGHT,WIDTH))
pygame.display.set_caption('clock')
clock = pygame.time.Clock()
running = True
rh = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/right-hand.png')
lh = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/left-hand.png')
body = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/main-clock.png')
body = pygame.transform.scale(body, (600,600))
angle = 0
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
            pygame.quit()
    current_time = datetime.datetime.now()
    sec = current_time.second
    min = current_time.minute

    rotated_rh = pygame.transform.rotate(rh,angle+sec*6)
  


    
    
    
   
    screen.blit(body,(0,0))
    screen.blit(lh,(40,240))
  
    pygame.display.flip()
    clock.tick(60)