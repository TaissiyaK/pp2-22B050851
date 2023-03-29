import pygame, datetime
pygame.init()


def rotate(image, center_of_image, ang_of_image):
    widht, height = image.get_size()
    surface_for_image = pygame.Surface((widht * 2, height * 2), pygame.SRCALPHA)
    surface_for_image.blit(image, (widht - center_of_image[0], height - center_of_image[1]))
    return pygame.transform.rotate(surface_for_image, ang_of_image * -1)

body = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/main-clock.png')
WIDHT, HEIGHT = body.get_size()
screen = pygame.display.set_mode((WIDHT,HEIGHT))
pygame.display.set_caption('clock')
clock = pygame.time.Clock()
running = True


rh_image = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/right-hand.png')  #minutes
lh_image = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/left-hand.png')   #seconds
rh_image = pygame.transform.rotate(rh_image, 90)
lh_image = pygame.transform.rotate(lh_image, 90)

current_time = datetime.datetime.now()
sec = current_time.second
min = current_time.minute
angle = 0
ang_for_lh = sec*6
ang_for_rh = min*6


center_of_image = (float(WIDHT)/2,float(HEIGHT)/2)
center_image_of_rh = (float(rh_image.get_size()[0])/2,float(rh_image.get_size()[1])/2)
center_image_of_lh = (float(lh_image.get_size()[0])/2,float(lh_image.get_size()[1])/2)


while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
            pygame.quit()


    current_time = datetime.datetime.now()
    sec = current_time.second
    min = current_time.minute

    image_for_lh = rotate(lh_image, center_image_of_lh, ang_for_lh)
    image_for_rh = rotate(rh_image, center_image_of_rh, ang_for_rh)
    rect_lh = image_for_lh.get_rect()
    rect_rh = image_for_rh.get_rect()
    rect_lh.center = center_of_image
    rect_rh.center = center_of_image
    screen.blit(body,(0,0))
    screen.blit(image_for_lh, rect_lh)
    screen.blit(image_for_rh, rect_rh)
    ang_for_lh = sec*6
    ang_for_rh = min*6


    pygame.display.update()
    clock.tick(60)