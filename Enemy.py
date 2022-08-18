from random import randint

import pygame as juego
from pygame.sprite import Sprite

from Bullet import Bullet


class Enemy(Sprite):
    def __init__(self, settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.settings = settings
        self.image = juego.image.load(self.settings.alien)
        self.image = juego.transform.scale(self.image, (50, 60))
        self.image = juego.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()

        # Rectángulo d ela pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.cont = 0;
        self.direccion = 1;
        self.screen_rect = self.screen.get_rect()

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def update(self, Vleft, Vright, Vup, Vdown, bullets_enemys, settings, screen, enemi, enemys):
        if self.rect.x > self.screen_rect.right:
            self.rect.x = 0

        if self.rect.x < self.screen_rect.left:
            self.rect.x = self.screen_rect.right

        if self.rect.y > self.screen_rect.bottom:
            self.rect.y = 0

        if self.cont == 10:
            self.cont = 0
            self.direccion = int(randint(0, 3))

        if self.direccion == 0:
            if self.rect.x in range(self.screen_rect.right - 50, self.screen_rect.right):
                self.rect.x -= int(Vleft * 1.45)
                self.rect.y += Vdown
            else:
                self.rect.x -= int(Vleft * 1.10)
                self.rect.y += Vdown
            self.cont += 1

        if self.direccion == 1:
            self.rect.y += Vdown
            self.cont += 1

        if self.direccion == 2:
            if self.rect.x in range(0, 50):
                self.rect.x -= int(Vright * 1.45)
                self.rect.y += Vdown
            else:
                self.rect.x += int(Vright * 1.10)
                self.rect.y += Vdown
            self.cont += 1

        if self.direccion == 3:
            #     self.rect.y-=Vup
            if len(bullets_enemys) < len(enemys):
                bala = Bullet(settings, screen, enemi)
                bala.speed = -bala.speed + 3
                bala.y = enemi.rect.bottom
                bullets_enemys.add(bala)
            self.cont += 10
