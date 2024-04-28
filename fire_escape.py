import pygame
import random
import os

pygame.init()
pygame.font.init()

# Screen Dimenstions
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fire Escape")
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (32, 10, 70)

# Fire Dimensions
FIRE_WIDTH, FIRE_HEIGHT = 35, 70
FIRE = pygame.Rect(
    SCREEN_WIDTH // 2 - FIRE_WIDTH // 2,
    SCREEN_HEIGHT - FIRE_HEIGHT,
    FIRE_WIDTH,
    FIRE_HEIGHT,
)
FIRE_VEL = 5

# Fire cartoon
FIRE_CARTOON_IMAGE = pygame.image.load(os.path.join("media", "fire_cartoon.png"))
FIRE_CARTOON = pygame.transform.scale(FIRE_CARTOON_IMAGE, (FIRE_WIDTH, FIRE_HEIGHT))

# Score
SCORE_TOTAL = 0
SCORE_FONT = pygame.font.SysFont("Roboto", 30)

# Game Over Message
MESSAGE_FONT = pygame.font.SysFont("arial", 50)
GAME_OVER_MESSAGE = MESSAGE_FONT.render("GAME OVER", 1, BLACK)
GAME_OVER_DIMENSIONS = (
    (SCREEN_WIDTH - GAME_OVER_MESSAGE.get_width()) // 2,
    (SCREEN_HEIGHT - GAME_OVER_MESSAGE.get_height()) // 2,
)

# Raindrop Dimensions
RAINDROP_WIDTH = 10
RAINDROP_HEIGHT = 10
RAINDROPS = [
    pygame.Rect(
        random.randint(0, 601) - RAINDROP_WIDTH,
        random.randint(0, 51) - RAINDROP_HEIGHT,
        RAINDROP_WIDTH,
        RAINDROP_HEIGHT,
    )
    for _ in range(10)
]
RAINDROP_VEL = 2
RAIN_COUNTER = 0

# Rain cartoon
RAIN_CARTOON_IMAGE = pygame.image.load(os.path.join("media", "rain_cartoon.png"))
RAIN_CARTOON = pygame.transform.scale(
    RAIN_CARTOON_IMAGE, (RAINDROP_WIDTH, RAINDROP_HEIGHT)
)


# Raindrop Container
RAINDROP_CONTAINER_WIDTH, RAINDROP_CONTAINER_HEIGHT = SCREEN_WIDTH, 50
RAINDROP_CONTAINER = pygame.Rect(
    0, 0, RAINDROP_CONTAINER_WIDTH, RAINDROP_CONTAINER_HEIGHT
)


def raindrop_movement():
    global RAINDROPS, RAINDROP_VEL, RAIN_COUNTER, SCORE_TOTAL
    for raindrop in RAINDROPS:
        raindrop.y += RAINDROP_VEL
        if raindrop.y > SCREEN_HEIGHT:
            RAIN_COUNTER += 1
            SCORE_TOTAL += 1
            raindrop.x = random.randint(0, RAINDROP_CONTAINER_WIDTH)
            raindrop.y = random.randint(0, RAINDROP_CONTAINER_HEIGHT)
        if RAIN_COUNTER == 25:
            RAINDROP_VEL += 1
            RAIN_COUNTER += 1
        if RAIN_COUNTER == 50:
            RAINDROP_VEL += 1
            RAIN_COUNTER += 1
        if RAIN_COUNTER == 75:
            RAINDROP_VEL += 1
            RAIN_COUNTER += 1


def fire_movement():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and FIRE.left > 0:  # LEFT
        FIRE.x -= FIRE_VEL
    if keys_pressed[pygame.K_RIGHT] and FIRE.right < SCREEN_WIDTH:  # RIGHT
        FIRE.x += FIRE_VEL
    if keys_pressed[pygame.K_UP] and FIRE.top > 0:  # UP
        FIRE.y -= FIRE_VEL
    if keys_pressed[pygame.K_DOWN] and FIRE.bottom < SCREEN_HEIGHT:  # DOWN
        FIRE.y += FIRE_VEL


def check_collision(raindrops: list[pygame.Rect]):
    global FIRE, run
    for raindrop in raindrops:
        if raindrop.colliderect(FIRE):
            SCREEN.blit(GAME_OVER_MESSAGE, GAME_OVER_DIMENSIONS)
            pygame.display.update()
            pygame.time.delay(3000)
            run = False


def update_screen(raindrops: list[pygame.Rect]):
    global RAINDROPS, raindrop
    SCREEN.fill(WHITE)
    SCREEN.blit(FIRE_CARTOON, (FIRE.x, FIRE.y))

    pygame.draw.rect(SCREEN, WHITE, RAINDROP_CONTAINER)

    SCORE = SCORE_FONT.render("Score: " + str(SCORE_TOTAL), 1, BLACK)
    SCREEN.blit(SCORE, (20, 20))

    for raindrop in RAINDROPS:
        pygame.draw.rect(SCREEN, BLUE, raindrop)
        SCREEN.blit(RAIN_CARTOON, (raindrop.x, raindrop.y))

    pygame.display.update()


def main():
    global SCORE_TOTAL
    clock = pygame.time.Clock()

    raindrops = [
        pygame.Rect(
            random.randint(0, 601) - RAINDROP_WIDTH,
            random.randint(0, 51) - RAINDROP_HEIGHT,
            RAINDROP_WIDTH,
            RAINDROP_HEIGHT,
        )
        for each in range(10)
    ]

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        raindrop_movement()
        fire_movement()
        check_collision(raindrops)
        update_screen(raindrops)

    pygame.quit()


if __name__ == "__main__":
    main()
