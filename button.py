# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 07:22:04 2019

@author: JUAN DIEGO
"""

import pygame
import random
from pygame.locals import *

FONDO = (32, 30, 32)
BLANCO = (255, 255, 255)
COLOR_TEXTO = (50, 60, 80)

pygame.init()
dimensiones = [600, 460]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Entrada de texto")
imagen_panel = pygame.image.load("badoo.png")
imagen_boton = pygame.image.load("badoo.png")
imagen_boton_pressed = pygame.image.load("badoo.png")
imagen_boton_cuadro = pygame.image.load("badoo.png")
imagen_boton_cuadro_pressed = pygame.image.load("badoo.png")
imagen_text = pygame.image.load("badoo.png")
fuente = pygame.font.SysFont('Courier', 20)
fuente_numero = pygame.font.SysFont('Pacifico Regular', 30)


def dibujar_texto(texto, contenedor_imagen, contenedor_rec, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    centro = text.get_rect()
    diferencia_x = contenedor_imagen.center[0] - centro.center[0]
    diferencia_y = contenedor_imagen.center[1] - centro.center[1]
    pantalla.blit(text, [contenedor_rec.left + diferencia_x, contenedor_rec.top + diferencia_y])


def generar_numero():
    numero = str(random.randint(1, 4)) + str(random.randint(1, 4)) + str(random.randint(1, 4)) + str(random.randint(1, 4))
    return numero


def dibujar_botones_iniciales(lista_botones):
    panel = pygame.transform.scale(imagen_panel, [560, 420])
    pantalla.blit(panel, [20, 20])
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])
        dibujar_texto(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)


def set_text(campo, texto):
    dibujar_texto(texto, campo['imagen'].get_rect(), campo['rect'], fuente_numero, COLOR_TEXTO)


def main():
    game_over = False
    clock = pygame.time.Clock()

    boton_cuadro = pygame.transform.scale(imagen_boton_cuadro, [90, 90])
    boton_cuadro_pressed = pygame.transform.scale(imagen_boton_cuadro_pressed, [90, 90])
    input_text = pygame.transform.scale(imagen_text, [440, 50])

    r_boton_1_1 = imagen_boton.get_rect()
    r_boton_1_2 = imagen_boton.get_rect()
    r_boton_2_1 = boton_cuadro.get_rect()
    r_boton_2_2 = boton_cuadro.get_rect()
    r_boton_2_3 = boton_cuadro.get_rect()
    r_boton_2_4 = boton_cuadro.get_rect()
    input_text_rect = input_text.get_rect()
    input_text_rect.topleft = [80, 360]
    campo_texto = {'imagen': input_text, 'rect': input_text_rect}

    botones = []
    r_boton_1_1.topleft = [80, 80]
    botones.append({'texto': "Nuevo número", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
    r_boton_1_2.topleft = [330, 80]
    botones.append({'texto': "Confirmar", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_2, 'on_click': False})
    r_boton_2_1.topleft = [80, 180]
    botones.append({'texto': "1", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_1, 'on_click': False})
    r_boton_2_2.topleft = [200, 180]
    botones.append({'texto': "2", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_2, 'on_click': False})
    r_boton_2_3.topleft = [320, 180]
    botones.append({'texto': "3", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_3, 'on_click': False})
    r_boton_2_4.topleft = [430, 180]
    botones.append({'texto': "4", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_4, 'on_click': False})

    #dibujar_botones_iniciales(botones)
    click = False
    mostrar_numero = 0
    numero_aleatorio = 0
    texto_entrada = ""
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False

        if botones[0]['on_click'] and click:
            numero_aleatorio = generar_numero()
            texto_entrada = ""
            mostrar_numero = 10
            click = False

        pantalla.fill(FONDO)
        dibujar_botones_iniciales(botones)
        pantalla.blit(input_text, campo_texto['rect'].topleft)

        if click and botones[1]['on_click']:
            if texto_entrada == numero_aleatorio:
                texto_entrada = "Congratulations!"
            else:
                texto_entrada = "Error!"
            click = False
        if click:
            for i in range(2, 6):
                if botones[i]['on_click'] and len(texto_entrada) < 4:
                    texto_entrada += botones[i]['texto']
            click = False
        if mostrar_numero > 0:
            dibujar_texto(numero_aleatorio, pygame.Surface([100, 40]).get_rect(), pygame.Rect([260, 300, 102, 42]), fuente_numero, COLOR_TEXTO)
            mostrar_numero -= 1

        set_text(campo_texto, texto_entrada)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()