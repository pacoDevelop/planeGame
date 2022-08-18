import pygame as juego
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, ImageNave):
        super(Ship, self).__init__()
        self.screen = screen

        self.image = juego.image.load(ImageNave)
        self.image = juego.transform.scale(self.image, (60, 70))
        self.rect = self.image.get_rect()

        # Rectángulo d ela pantalla
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx

        self.rect.bottom = self.screen_rect.bottom

    def blit(self):
        self.screen.blit(self.image, self.rect)