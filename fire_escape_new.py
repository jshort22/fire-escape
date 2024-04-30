import pygame
import random


pygame.init()

pygame.display.set_caption("Fire Escape")


def update_screen(
    screen: pygame.Surface,
    red: tuple[int, int, int],
    blue: tuple[int, int, int],
    fire: pygame.Rect,
    rain: pygame.Rect,
):
    white = (255, 255, 255)
    screen.fill(white)
    pygame.draw.rect(screen, red, fire)
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
    rain: pygame.Rect,
    rain_vel: int,
    screen_width: int,
    screen_height: int,
):

    rain.y += rain_vel
    if rain.y > screen_height:
        rain.x = random.randint(0, screen_width - rain.width)
        rain.y = -rain.height


"""def check_collision(
    rain: pygame.Rect,
    fire: pygame.Rect,
    rain_vel: int,
):
    if rain.colliderect(fire):
        rain.y -= rain_vel"""


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
    rain_vel = 5
    rain = pygame.Rect(
        random.randint(0, random.randint(0, 500)),
        random.randint(0, random.randint(0, 50)),
        rain_width,
        rain_height,
    )

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update_screen(screen, red, blue, fire, rain)
        fire_movement(fire, fire_vel, screen_width, screen_height)
        rain_movement(
            rain,
            rain_vel,
            screen_width,
            screen_height,
        )
        # check_collision(rain, fire, rain_vel)

    pygame.quit()


if __name__ == "__main__":
    main()
