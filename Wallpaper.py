import pygame


class Wallpaper():

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.moving = True

        self.image = pygame.image.load(settings.fondo)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left
        self.center = float(self.rect.centerx)  # valor con decimales

        self.num_tiles_x = (self.screen.get_width() // self.image.get_width()) + 1  # Más uno para desbordar
        self.num_tiles_y = (self.screen.get_height() // self.image.get_height()) + 1
        self.row = 0

    def blit(self):
        if self.row > self.image.get_height():
            self.rect.top = 0
            self.row = 0
        for i in range(-1, self.num_tiles_y):
            for j in range(0, self.num_tiles_x):
                self.screen.blit(self.image, self.rect)
                self.rect.left = j * self.image.get_width()
            self.rect.top = i * self.image.get_height() + self.row
        self.row = self.row + 1

    def update(self):
        if self.moving == True:
            self.rect.top += 1
        self.rect.centerx = self.center
