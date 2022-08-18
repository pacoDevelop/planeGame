import os

import pygame


class Musica:

    def __init__(self, pista):
        self.pista = os.path.join("Resources", pista)
        self.mixer = pygame.mixer
        self.mixer.init()
        self.mixer = pygame.mixer.Sound(self.pista)


    def play(self):
        self.mixer.play()

    def stop(self):
        self.mixer.stop()
        self.mixer.quit()
