import pygame


class Ship():

    def __init__(self, screen):
        self.screen = screen

        self.img = pygame.image.load(r"images\ship.bmp")
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.img, self.rect)

