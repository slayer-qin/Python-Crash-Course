
import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # init game and create a screen
    pygame.init()
    AISET = Settings()
    screen = pygame.display.set_mode((AISET.screen_width, AISET.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # game loop
    while True:
        # check the actions og keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # redraw screen
        screen.fill(AISET.bg_color)
        ship.blitme()
        # refresh the display, make the screen be seen
        pygame.display.flip()


if __name__ == "__main__":
    run_game()