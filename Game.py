from Musica import Musica
from Settings import Settings
from Ship import Ship
from Texto import Texto
from Wallpaper import Wallpaper
from game_functions import *


class Game:
    def __init__(self):
        juego.init()
        self.settings = Settings()
        self.screen = juego.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.nave = Ship(self.screen, self.settings.nave)
        self.fondo = Wallpaper(self.settings, self.screen)
        self.texto = Texto(self.screen, self.settings)
        self.musicaFondo = Musica("fondo.wav")
        self.musicaDisparo = Musica("disparo.wav")
    def run_game(self):
        self.musicaFondo.play()
        juego.display.set_caption(self.settings.titulo)
        icon = juego.image.load(self.settings.icono)
        juego.display.set_icon(icon)
        self.texto.mostrar_mensaje("PlaneGame", 2000)
        create_fleet(self.settings, self.screen)
        run=True
        while run:
            # Capturamos los eventos que se han producido
            for event in juego.event.get():
                # Si el evento es salir de la ventana, terminamos
                if event.type == juego.QUIT: run = False
            juego.time.delay(self.settings.speed_game)
            update_screen(self.settings, self.screen, self.nave, self.fondo, self.texto)
            check_events(self.nave, self.screen, self.settings, self.musicaDisparo)
        # Salgo de pygame
        juego.quit()