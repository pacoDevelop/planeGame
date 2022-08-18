import os

import pygame


class Texto:

    def __init__(self, screen="", setting=""):
        self.texto = ""
        self.font = pygame.font.Font(os.path.join("Resources", "Durian Lovers.otf"), 60)
        self.screen = screen
        self.setting = setting

    def mostrar_mensaje(self, texto, tiempo):
        # render text
        label = self.font.render(texto, True, (255, 255, 255))
        self.screen.blit(label, (self.setting.screen_width / 2 - (label.get_rect().width / 2),
                                 self.setting.screen_height / 2 - (label.get_rect().height / 2)))
        pygame.display.update()
        pygame.time.wait(tiempo)
