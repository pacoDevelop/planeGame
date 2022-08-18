import os
import sys
from random import randint

import pygame as juego
from pygame.sprite import Group

from Bullet import Bullet
from Enemy import Enemy

juego.init()

bullets = Group()
enemys = Group()
naveGroup = Group()
bullets_enemys = Group()
global puntacion
puntuacion = 0

global fuente
fuente = juego.font.Font(os.path.join("Resources", "Durian Lovers.otf"), 30)

def create_fleet(settings, screen):
    alien = Enemy(settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height

    available_space_x = settings.screen_width - (alien_width * 2)
    available_space_y = settings.screen_height - (alien_height + 200)

    number_aliens_x = int(available_space_x / (alien_width * 4)) - 1
    number_rows = available_space_y // (alien_height * 2) - 1

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            alien = Enemy(settings, screen)
            alien.x = 2 * alien_width + alien_width * alien_number * 4
            alien.y = 0
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            enemys.add(alien)


def update_bullets():
    global puntuacion
    collisions = juego.sprite.groupcollide(bullets, enemys, True, True)
    if collisions.__len__() != 0:
        puntuacion += 1


def update_bullets_enemis(texto, screen):
    collisions = juego.sprite.groupcollide(bullets_enemys, naveGroup, True, False)
    if collisions.__len__() != 0:
        screen.fill((0, 0, 0))
        texto.mostrar_mensaje(f"Has perdido, tu puntuación {puntuacion}", 5000)
        exit(0)


def update_plane(nave, screen, texto):
    naveGroup.add(nave)
    collisions = juego.sprite.groupcollide(naveGroup, enemys, False, True)
    if collisions.__len__() != 0:
        screen.fill((0, 0, 0))
        texto.mostrar_mensaje(f"Has perdido, tu puntuación {puntuacion}", 5000)
        exit(0)


def mostrar_puntos(screen, puntos):
    global fuente
    label = fuente.render("Aviones derribados:" + str(puntos), True, (0, 0, 0))
    screen.blit(label, (20, 30))

def check_events(nave, screen, settings, disparo):
    for event in juego.event.get():
        if event.type == juego.QUIT:
            sys.exit()
        else:
            if event.type == juego.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if len(bullets) < 3:
                        disparo.play()
                        bullets.add(Bullet(settings, screen, nave))

            if event.type == juego.MOUSEMOTION:
                x = juego.mouse.get_pos()[0]
                y = juego.mouse.get_pos()[1]
                conts = settings.velocidadNave
                if x < nave.rect.centerx:
                    nave.rect.centerx -= conts
                else:
                    nave.rect.centerx += conts

                if y < nave.rect.centery:
                    nave.rect.centery -= conts
                else:
                    nave.rect.centery += conts


def update_screen(settings, screen, nave, fondo, texto):
    screen.fill(settings.bg_color)
    update_bullets_enemis(texto, screen)
    fondo.update()
    fondo.blit()

    bullets.update()
    bullets_enemys.update()
    update_bullets()
    nave.blit()
    enemys.draw(screen)
    mostrar_puntos(screen, puntuacion)
    update_plane(nave, screen, texto)
    if len(enemys) < 3:
        create_fleet(settings, screen)
    for bala in bullets_enemys.sprites():
        bala.dibujar()
        if bala.rect.top >= settings.screen_height:
            bullets_enemys.remove(bala)
    for enemy in enemys.sprites():
        enemy.update(int(randint(1, 3)), int(randint(1, 2)), int(randint(1, 2)), int(randint(1, 3)), bullets_enemys,
                     settings, screen, enemy, enemys)
    for bullet in bullets.sprites():
        bullet.dibujar()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    juego.display.flip()
