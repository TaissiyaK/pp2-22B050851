import random
import time
import pygame
# основные параметры игры в виде размеров окна, цвета и тд.
pygame.init()
WIDTH, HEIGHT = 800, 800
HEAD_COLOR = (19, 213, 213)
BOARD_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
POISON_COLOR = (255, 0, 0)
FOOD_FOR_FIVE_COLOR = (78, 229, 73)
FOOD_FOR_TEN_COLOR = (83, 253, 202)
FOOD_FOR_FIFTEEN_COLOR = (243, 7, 243)
SNAKE_COLOR = (19, 26, 215)


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
pygame.display.set_caption('Snake 2')


# класс точки, которая имеет х и у
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class EatebleObjects:
    def __init__(self, x, y, color):
        self.location = Point(x, y)
        self.color = color

    @property
    def x(self):
        return self.location.x

    @property
    def y(self):
        return self.location.y

    def update(self):
        pygame.draw.rect(
            SCREEN,
            self.color,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )


# класс еды. которая имеет функции для координат и функция для создания клетки
class FoodForFive(EatebleObjects):
    score_add = 5


class FoodForTen(EatebleObjects):
    score_add = 10


class FoodForFifteen(EatebleObjects):
    score_add = 15


class Poison(EatebleObjects):
    score_add = -10


# класс змейки, которая имеет функции отрисовки тела, функции движения, функции поедания еды и функцию, проверяющая
# на столкновение со своим телеом
class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
        ]

    def update(self):

        head = self.points[0]

        pygame.draw.rect(
            SCREEN,
            HEAD_COLOR,
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
                SNAKE_COLOR,
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

    def check_collision(self, eateble):
        if self.points[0].x != eateble.x:
            return False
        if self.points[0].y != eateble.y:
            return False
        return True

    def touch_snake(self):
        head = self.points[0]
        for item in self.points[1:]:
            if item.x == head.x and item.y == head.y:
                return False
        return True


# функция отрисовки поля
def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (x, 0), (x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, BLACK, (0, y), (WIDTH, y), width=1)


# функция для показа очков, которые получает игрок во время игры
def show_score(score):
    my_font = pygame.font.SysFont('times new roman', 25)
    game_over_surface = my_font.render(f'Your Score is : {score}', True, BLACK)
    SCREEN.blit(game_over_surface, (0, 0))


# функция поражения(косание края поля или тела змейки)
def game_over(score):
    pygame.mixer.music.play()
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(f'Your Score is : {score}', True, BLACK)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 2)
    SCREEN.blit(game_over_surface, game_over_rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()


# главная фунция игры, в которой реализовано направления движения змейки,
# увелечение змейки и очков от съеденной еды, увелечение скорости
def main():
    running = True
    snake = Snake()
    foods = [
        FoodForFive(5, 5, FOOD_FOR_FIVE_COLOR),
        FoodForTen(5, 5, FOOD_FOR_TEN_COLOR),
        FoodForFifteen(5, 5, FOOD_FOR_FIFTEEN_COLOR)
            ]
    food = random.choices(foods, weights=[10, 5, 1])[0]
    poison = Poison(6, 8, POISON_COLOR)
    dx, dy = 0, 0
    fps = 5
    score = 0
    direction = 'UP'
    change_to = direction

    last_food = 0
    food_timer = 15000

    while running:

        SCREEN.fill(BOARD_COLOR)

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

        if len(snake.points) == 1 and snake.check_collision(poison):
            game_over(score)

        if snake.check_collision(food):
            snake.points.append(Point(food.x, food.y))
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            if food.location.x == poison.location.x and food.location.y == poison.location.y:
                food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            score = score + food.score_add
            food = random.choices(foods, weights=[10, 5, 1])[0]

        if snake.check_collision(poison):
            snake.points.pop(-1)
            poison.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            poison.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)

        now = pygame.time.get_ticks()

        if now - last_food >= food_timer:
            food = random.choices(foods, weights=[10, 5, 1])[0]
            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            last_food = now

        food.update()
        poison.update()
        snake.update()
        draw_grid()
        show_score(score)
        pygame.display.flip()

        if score == 50:
            fps = 7
        elif score == 100:
            fps = 9
        elif score == 150:
            fps = 11
        elif score == 200:
            fps = 13
        elif score == 250:
            fps = 15

        clock.tick(fps)


if __name__ == '__main__':
    main()