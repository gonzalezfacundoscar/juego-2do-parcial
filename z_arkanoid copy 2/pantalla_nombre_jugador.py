import pygame
import funciones_sql
import funciones
import tkinter
from tkinter import messagebox
from colores import *
#from main import puntuaciones

root = tkinter.Tk()
root.withdraw()

ANCHO = 800
ALTO = 600

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))

input_box = pygame.Rect(ANCHO //2 - 100, ALTO //2, 200, 30)
fuente = pygame.font.Font(None, 36)

def mostrar_pantalla_nombre(puntuacion):
    nombre = ''
    pantalla_inicial = True

    while pantalla_inicial:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pantalla_inicial = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    #messagebox.showinfo("nombre", "El nombre igresado no es valido")
                    if funciones.validar_letras_regex(nombre):
                        pantalla_inicial = False
                        funciones_sql.crear_base_de_datos(nombre.capitalize(), puntuacion)
                        nombre = ''                        
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif event.unicode:
                    nombre += event.unicode
        
        pantalla.fill(NEGRO)

        pygame.draw.rect(pantalla, ROJO, input_box, 2)
        txt_surface = fuente.render(nombre, True, BLANCO)
        pantalla.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        ingresar_nombre = fuente.render("ingresa tu nombre", True, BLANCO)
        pantalla.blit(ingresar_nombre, (ANCHO//2 - 85, ALTO//2 - 40))

        presionar_enter = fuente.render("Presiona ENTER para continuar", True, BLANCO)
        pantalla.blit(presionar_enter, (ANCHO//2 - 145, ALTO//2 - 100))

        pygame.display.flip()




