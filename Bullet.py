import pygame as juego
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.settings = settings
        self.screen = screen
        self.ship = ship

        self.rect = juego.Rect(0, 0, self.settings.bullet_width, self.settings.height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = self.settings.bullet_color
        self.speed = self.settings.bullet_speed

    def update(self):
        self.y = self.y - self.speed

        self.rect.y = self.y

    def dibujar(self):
        juego.draw.rect(self.screen, self.color, self.rect)
