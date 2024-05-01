import pygame
import random


pygame.init()

pygame.display.set_caption("Fire Escape")


def update_screen(
    screen: pygame.Surface,
    red: tuple[int, int, int],
    blue: tuple[int, int, int],
    fire: pygame.Rect,
    rain_drops: list[pygame.Rect],
    rain_counter: list[int],
):
    white = (255, 255, 255)
    screen.fill(white)
    pygame.draw.rect(screen, red, fire)
    for rain in rain_drops:
        pygame.draw.rect(screen, blue, rain)
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
        print(rain_counter)
        if rain_counter[0] % 10 == 0 and rain_counter[0] != 0:
            rain_vel[0] += 1
            rain_counter[0] += 1


def main():
    clock = pygame.time.Clock()

    # COLORS
    red = (255, 0, 0)
    blue = (0, 0, 255)

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
                run = False
                print("GAME OVER")
                pygame.time.delay(5000)
        if timer % 1000 == 0:
            new_rain_drop = pygame.Rect(
                random.randint(0, random.randint(0, screen_width - rain_width)),
                -rain_height,
                rain_width,
                rain_height,
            )
            rain_drops.append(new_rain_drop)

        update_screen(screen, red, blue, fire, rain_drops, rain_counter)
        fire_movement(fire, fire_vel, screen_width, screen_height)
        rain_movement(rain_drops, rain_vel, screen_width, screen_height, rain_counter)

    pygame.quit()


if __name__ == "__main__":
    main()
