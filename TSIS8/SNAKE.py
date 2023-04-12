import random
import time
import pygame
# основные параметры игры в виде размеров окна, цвета и тд.
pygame.init()

WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
pygame.display.set_caption('Snake')


# класс точки, которая имеет координаты х и у
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# класс еды. которая имеет функцию для координат и функцию обновления положения 
class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


# класс змея, которая имеет функцию отрисовки тела, функцию перемещения, функцию на поедание точки
# функцию проверяющую координаты тела и следующее движение
class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
        ]

    def update(self):
        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y

        self.points[0].x += dx
        self.points[0].y += dy

        head = self.points[0]
        if head.x >= WIDTH // BLOCK_SIZE or head.x < 0:
            return False
        elif head.y >= HEIGHT // BLOCK_SIZE or head.y < 0:
            return False
        else:
            return True

    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True

    def touch_snake(self):
        head = self.points[0]
        for idx in self.points[1:]:
            if idx.x == head.x and idx.y == head.y:
                return False
        return True


# функция отрисовки поля
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, (0, y), (WIDTH, y), width=1)


# функция для показа очков и уровня
def show_score_level(score,level):
    my_font1 = pygame.font.SysFont('Verdana', 30)
    show_sc_lvl1 = my_font1.render(f'Your Score is : {score}', True, RED)
    my_font2 = pygame.font.SysFont('Verdana', 30)
    show_sc_lvl2 = my_font2.render(f'Your level is: {level}', True, RED)
    SCREEN.blit(show_sc_lvl1, (0, 0))
    SCREEN.blit(show_sc_lvl2, (0, 40))


# функция показывающая количество набранных очков после проигрыша
def game_over(score):
    my_font = pygame.font.SysFont('Verdana', 50)
    game_over = my_font.render(f'Your Score is : {score}', True, RED)
    SCREEN.blit(game_over, (WIDTH//3, HEIGHT//2))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()


# главная фунция игры, в которой принимаются нажатия клавиш для смены направления движения змейки,
# проверка хода движения змейки
# при соблюдении условий повышение очков, уровня, скорости
def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    dx, dy = 0, 0
    fps = 2
    score = 0
    level = 0
    direction = 'UP'
    change_to = direction

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            dx, dy = 0, -1
        if direction == 'DOWN':
            dx, dy = 0, +1
        if direction == 'LEFT':
            dx, dy = -1, 0
        if direction == 'RIGHT':
            dx, dy = +1, 0

        if snake.move(dx, dy):
            pass
        else:
            game_over(score)

        if snake.touch_snake():
            pass
        else:
            game_over(score)

        if snake.check_collision(food):
            snake.points.append(Point(food.x, food.y))
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            score += 1

        food.update()
        snake.update()
        draw_grid()
        show_score_level(score, level)
        pygame.display.flip()

        if score == 3:
            level = 1
            fps = 4
        elif score == 6:
            level = 2
            fps = 6
        elif score == 9:
            level = 3
            fps = 8
        elif score == 12:
            level = 4
            fps = 10
        elif score == 15:
            level = 5
            fps = 12

        clock.tick(fps)


if __name__ == '__main__':
    main()