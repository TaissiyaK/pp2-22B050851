import random

import pygame
# основные параметры игры в виде размеров окна, цвета и тд.
pygame.init()
WIDTH, HEIGHT = 400, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Street Racer')
background = pygame.image.load("/Users/macbookpro/Desktop/pp2-22B050851/TSIS8/AnimatedStreet.png")
score_font = pygame.font.SysFont("Verdana", 30)
SCORE = 0
# класс монеты функция отрисовки монеты, функция обновления рандомного местоположения монеты
class Coins(pygame.sprite.Sprite):
    def __init__(self,photo,value):
        super().__init__()
        self.photo = photo
        self.value = value
        self.image = pygame.image.load(self.photo)
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width),
            HEIGHT - self.rect.height,
        )
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width),
            HEIGHT - self.rect.height,
        )


# класс врага, функция отрисовки врага, функция обновления рандомного местоположения машины и увелечения ее скорости
# враг доходит до нижней границы высоты, и новое обновление местоположения сверху
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS8/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(0, WIDTH - self.rect.width),
            self.rect.height // 2,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 2
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
    


# класс игрок, функция отрисовки игрока, функция обновления местоположения игрока по переключению клавиш влево вправо
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('/Users/macbookpro/Desktop/pp2-22B050851/TSIS8/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x >= self.speed:
            self.rect.x -= self.speed
        if pressed[pygame.K_RIGHT] and self.rect.x + self.rect.width + self.speed <= WIDTH:
            self.rect.x += self.speed
        
def new_coin(arr):
    parameters = random.choice(arr)
    return Coins(parameters[0],parameters[1])

def main():
    running = True
    player = Player()
    enemy = Enemy()
    sum_coins = 0
    list_of_coins = [['/Users/macbookpro/Desktop/pp2-22B050851/TSIS9/coinone.png',1],
                     ['/Users/macbookpro/Desktop/pp2-22B050851/TSIS9/cointwo.png',2],
                     ['/Users/macbookpro/Desktop/pp2-22B050851/TSIS9/cointwo.png',3]]
    parameters = random.choice(list_of_coins)
    coin = Coins(parameters[0],parameters[1])
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()

    enemies.add(enemy)
    coins.add(coin)


    while running:
        SCREEN.blit(background, (0, 0))
        player.update()
        enemy.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        score = score_font.render(f" Your Score: {str(SCORE)}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))
        coins_amount = score_font.render(f" Coins: {str(sum_coins)}", True, (0, 0, 0))
        SCREEN.blit(coins_amount, (0, 40))

        # проверка столкновения игрока с врагом
        if pygame.sprite.spritecollideany(player, enemies):
            running = False
        # проверка столкновения игрока с монеткой
        if pygame.sprite.spritecollideany(player, coins):
            sum_coins = sum_coins + coin.value
            coin = new_coin(list_of_coins)
            coin.update()

        player.draw(SCREEN)
        enemy.draw(SCREEN)
        coin.draw(SCREEN)
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()