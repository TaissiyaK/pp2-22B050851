import pygame
from pygame import mixer

def next(music,index):
    if index < 2:
        index = index+1
    pygame.mixer.music.load(music[index])
    pygame.mixer.music.play()
def previous(music,index):
    if index > 0:
        index = index - 1
    pygame.mixer.music.load(music[index])
    pygame.mixer.music.play()


pygame.init()
mixer.init()

WEIGHT, WIDTH = 600, 600
screen = pygame.display.set_mode((WEIGHT,WIDTH))
pygame.display.set_caption('MUSIC')
clock = pygame.time.Clock()
running = True
music = ['/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/m0.mp3',
         '/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/m1.mp3',
         '/Users/macbookpro/Desktop/pp2-22B050851/TSIS7/m2.mp3']

while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT: #previous
            previous(music,index)
            if 0 < index <= 2:
                index -= 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT: #next
            next(music,index)
            if 0 <= index < 2:
                index += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP: #play
            pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN: #stop
            pygame.mixer.music.stop()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            pygame.mixer.music.load(music[0])
            index = 0
            pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            pygame.mixer.music.load(music[1])
            index = 1
            pygame.mixer.music.play()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            pygame.mixer.music.load(music[2])
            index = 2
            pygame.mixer.music.play()
        else:
            running = True

     
    pygame.display.flip()
    clock.tick(60)