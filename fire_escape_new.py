import pygame
import random

pygame.init()

pygame.display.set_caption("Fire Escape")


def update_screen(screen: pygame.Surface, red: tuple[int, int, int], fire: pygame.Rect):
    white = (255, 255, 255)
    screen.fill(white)
    pygame.draw.rect(screen, red, fire)
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


# def raindrop_movement():


def main():
    clock = pygame.time.Clock()

    # COLORS
    red = (255, 0, 0)

    # SCREEN
    screen_width = 500
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 10)

    # FIRE
    fire_width = 30
    fire_height = 70
    fire = pygame.Rect(
        screen_width // 2 - fire_width // 2,
        screen_height - fire_height,
        fire_width,
        fire_height,
    )
    fire_vel = 5

    # RAIN
    rain_width = 10
    rain_height = 10
    rain = [
        pygame.Rect(
            random.randint(0, 601) - rain_width,
            random.randint(0, 51) - rain_height,
            rain_width,
            rain_height,
        )
        for _ in range(10)
    ]
    rain_vel = 10

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update_screen(screen, red, fire)
        fire_movement(fire, fire_vel, screen_width, screen_height)

    pygame.quit()


if __name__ == "__main__":
    main()
