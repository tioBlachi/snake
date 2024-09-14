import pygame
from random import randrange
import os

pygame.init()

def main():

    def check_self_eating():
        head = (SNAKE_X, SNAKE_Y)
        return head in SNAKE_BODY[:-1]

    def place_food():
        while True:
            x = randrange(0, WIDTH - TILE_SIZE, TILE_SIZE)
            y = randrange(TILE_SIZE, HEIGHT - TILE_SIZE, TILE_SIZE)
            if (x, y) not in SNAKE_BODY:
                return x, y

    WIDTH, HEIGHT = 800, 800
    TILE_SIZE = 50
    SCORE = 0
    FOOD_SIZE = (48, 48)
    SNAKE_LENGTH = 1
    FPS = 15
    SCREEN_SIZE = (WIDTH, HEIGHT)
    FONT = pygame.font.SysFont('Arial', TILE_SIZE)

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Snake')

    food = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'images', 'mushroom.png')), FOOD_SIZE)
    food_rect = food.get_rect()
    FOOD_X = randrange(0, WIDTH - TILE_SIZE, TILE_SIZE)
    FOOD_Y = randrange(TILE_SIZE, HEIGHT - TILE_SIZE, TILE_SIZE)
    SNAKE_X = randrange(0, WIDTH - TILE_SIZE, TILE_SIZE)
    SNAKE_Y = randrange(TILE_SIZE, HEIGHT - TILE_SIZE, TILE_SIZE)
    SNAKE_BODY = []
    SNAKE_DIR = ""
    snake = pygame.Surface((TILE_SIZE, TILE_SIZE))
    snake.fill('green')
    is_moving = False

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and SNAKE_DIR != "R":
                    SNAKE_DIR = "L"
                    is_moving = True
                if event.key == pygame.K_RIGHT and SNAKE_DIR != "L":
                    SNAKE_DIR = "R"
                    is_moving = True
                if event.key == pygame.K_UP and SNAKE_DIR != "D":
                    SNAKE_DIR = "U"
                    is_moving = True
                if event.key == pygame.K_DOWN and SNAKE_DIR != "U":
                    SNAKE_DIR = "D"
                    is_moving = True

        if SNAKE_DIR == "R":
            SNAKE_X += TILE_SIZE
            if SNAKE_X + TILE_SIZE > WIDTH:
                SNAKE_X = WIDTH - TILE_SIZE
                is_moving = False
        elif SNAKE_DIR == "L":
            SNAKE_X -= TILE_SIZE
            if SNAKE_X < 0:
                SNAKE_X = 0
                is_moving = False
        elif SNAKE_DIR == "D":
            SNAKE_Y += TILE_SIZE
            if SNAKE_Y + TILE_SIZE > HEIGHT:
                SNAKE_Y -= TILE_SIZE
                is_moving = False
        elif SNAKE_DIR == "U":
            SNAKE_Y -= TILE_SIZE
            if SNAKE_Y < TILE_SIZE:
                SNAKE_Y += TILE_SIZE
                is_moving = False

        # Snake eats the food...
        if SNAKE_X == FOOD_X and SNAKE_Y == FOOD_Y:
            SNAKE_LENGTH += 1
            SCORE += 1
            FOOD_X, FOOD_Y = place_food()

        # check to see if snake is moving before popping off index 0
        if is_moving:
            SNAKE_BODY.append((SNAKE_X, SNAKE_Y))
            if SNAKE_LENGTH < len(SNAKE_BODY):
                SNAKE_BODY.pop(0)
        else:
            if SNAKE_BODY:
                SNAKE_BODY[-1] = (SNAKE_X, SNAKE_Y)

        if check_self_eating():
            print("Game Over!")
            running = False

        screen.fill((0, 0, 0))
        SCORE_DISPLAY = FONT.render(f'Score: {SCORE}     Length: {SNAKE_LENGTH}', True, 'white')
        screen.blit(SCORE_DISPLAY, (0,0))
        screen.blit(food, (FOOD_X, FOOD_Y))
        [(screen.blit(snake, location)) for location in SNAKE_BODY]

        clock.tick(FPS)
        pygame.display.update()


if __name__ == '__main__':
    main()