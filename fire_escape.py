import pygame
import random
import os


pygame.init()

pygame.display.set_caption("Fire Escape")


def update_screen(
    screen: pygame.Surface,
    red: tuple[int, int, int],
    blue: tuple[int, int, int],
    black: tuple[int, int, int],
    fire: pygame.Rect,
    rain_drops: list[pygame.Rect],
    timer: int,
    rain_counter: list[int],
    fire_width: int,
    fire_height: int,
    rain_width: int,
    rain_height: int,
):
    fire_cartoon_image = pygame.image.load(os.path.join("media", "fire_cartoon.png"))
    rain_cartoon_image = pygame.image.load(os.path.join("media", "rain_cartoon.png"))

    fire_cartoon = pygame.transform.scale(fire_cartoon_image, (fire_width, fire_height))
    rain_cartoon = pygame.transform.scale(rain_cartoon_image, (rain_width, rain_height))

    message_font = pygame.font.SysFont("Roboto", 20)
    white = (255, 255, 255)
    screen.fill(white)
    score = message_font.render("Score " + str(rain_counter), 1, black)
    screen.blit(score, (20, 40))
    level = message_font.render("Level " + str(len(rain_drops)), 1, black)
    screen.blit(level, (20, 20))
    screen.blit(fire_cartoon, (fire.x, fire.y))
    # pygame.draw.rect(screen, red, fire)
    for rain in rain_drops:
        screen.blit(rain_cartoon, (rain.x, rain.y))
    pygame.display.update()


def fire_movement(
    fire: pygame.Rect, fire_vel: int, screen_width: int, screen_height: int
):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] and fire.left > 0:  # LEFT
        fire.x -= fire_vel
    if keys_pressed[pygame.K_RIGHT] and fire.right < screen_width:  # RIGHT
        fire.x += fire_vel
    if keys_pressed[pygame.K_UP] and fire.top > 0:  # UP
        fire.y -= fire_vel
    if keys_pressed[pygame.K_DOWN] and fire.bottom < screen_height:  # DOWN
        fire.y += fire_vel


def rain_movement(
    rain_drops: list[pygame.Rect],
    rain_vel: list[int],
    screen_width: int,
    screen_height: int,
    rain_counter: list[int],
):
    for rain in rain_drops:
        rain.y += rain_vel[0]
        if rain.y > screen_height:
            rain.x = random.randint(0, screen_width - rain.width)
            rain.y = -rain.height
            rain_counter[0] += 1
        if rain_counter[0] % 10 == 0 and rain_counter[0] != 0 and rain_vel[0] <= 5:
            rain_vel[0] += 1
            rain_counter[0] += 1


def main():
    clock = pygame.time.Clock()

    # COLORS
    red = (255, 0, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)

    # SCREEN
    screen_width = 500
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))

    # FIRE
    fire_width = 30
    fire_height = 70
    fire_vel = 5
    fire = pygame.Rect(
        screen_width // 2 - fire_width // 2,
        screen_height - fire_height,
        fire_width,
        fire_height,
    )

    # RAIN
    rain_width = 10
    rain_height = 10
    rain_vel = [2]
    rain_counter = [0]

    timer = 0
    message_font = pygame.font.SysFont("Roboto", 20)

    rain_drops = [
        pygame.Rect(
            random.randint(0, random.randint(0, screen_width - rain_width)),
            -rain_height,
            rain_width,
            rain_height,
        )
        for _ in range(1)
    ]
    run = True
    while run:
        timer += 1
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for rain in rain_drops:
            if rain.colliderect(fire):
                game_over_message = message_font.render("GAME OVER", 1, black)
                screen.blit(
                    game_over_message,
                    (
                        screen_width // 2 - game_over_message.get_width() // 2,
                        screen_height // 2,
                    ),
                )
                pygame.display.update()
                pygame.time.delay(5000)
                run = False
        if timer % 1000 == 0:
            new_rain_drop = pygame.Rect(
                random.randint(0, random.randint(0, screen_width - rain_width)),
                -rain_height,
                rain_width,
                rain_height,
            )
            rain_drops.append(new_rain_drop)
            print(len(rain_drops))

        update_screen(
            screen,
            red,
            blue,
            black,
            fire,
            rain_drops,
            timer,
            rain_counter,
            fire_width,
            fire_height,
            rain_width,
            rain_height,
        )
        fire_movement(fire, fire_vel, screen_width, screen_height)
        rain_movement(rain_drops, rain_vel, screen_width, screen_height, rain_counter)

    pygame.quit()


if __name__ == "__main__":
    main()
