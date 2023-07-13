import pygame
from bloque import Bloque
from paleta import Paleta
from pelota import Pelota
import random
from colores import*
import funciones_sql
import menu
from pantalla_nombre_jugador import *
#import sqlite3


# Inicializamos pygame
pygame.init()

estado_juego = menu.dibujar_menu() 
if estado_juego == 1:
    #Inicializamos musica
    pygame.mixer.init()
    pygame.mixer.music.load("z_arkanoid\musica_de_fondo.ogg")
    pygame.mixer.music.set_volume(0.2) 
    pygame.mixer.music.play(-1)  # Reproducir en bucle

    # Creamos la superficie de juego
    ANCHO = 800
    ALTO = 600
    pantalla_ppal = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Arkanoid")

    reloj = pygame.time.Clock()
    tiempo_inicial = pygame.time.get_ticks()
    FPS = 200
    VIDAS = 3
    puntuacion = 0


    paddle = Paleta()
    ball = Pelota()
    blocks = pygame.sprite.Group()

    # Creamos el grupo de sprites
    bloques = Bloque.crear_bloques(50, 68, 20)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(paddle, ball,bloques)


    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizamos los objetos del juego
        all_sprites.update()

        # Verificamos las colisiones con la paleta
        if pygame.sprite.collide_rect(ball, paddle):
            ball.speed_y *= -1

        # Verificamos las colisiones con los bloques
        block_hit_list = pygame.sprite.spritecollide(ball, bloques, True)
        if len(block_hit_list) > 0:
            ball.speed_y *= -1
            puntuacion += 50
        
        # Cuando se pierde la pelota la traemos a la pantalla
        if ball.rect.bottom > ALTO:
            VIDAS -= 1
            ball.rect.x = ANCHO // 2
            ball.rect.y = ALTO // 2
            ball.speed_x = random.choice([-2, 2])
            ball.speed_y = -2
        
        #Cuando ya no quedan mas vidas 
        if VIDAS == 0:
            fuente = pygame.font.Font(None, 36)
            texto = fuente.render("Game Over", True, (255, 255, 255))
            texto_rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
            pantalla_ppal.blit(texto, texto_rect)
            pygame.display.flip()
            pygame.time.wait(3000)


            
            #funciones_sql.guardar_puntuacion(nombre_jugador, puntuacion)
            #puntuaciones = funciones_sql.obtener_puntuaciones()

            mostrar_pantalla_nombre(puntuacion)
            
            

            running = False
        
        
        
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - tiempo_inicial
        segundos = int(tiempo_transcurrido / 1000)
        minutos = segundos // 60
        segundos = segundos % 60

        
        # Dibujamos los objetos en la pantalla
        pantalla_ppal.fill((0, 0, 0))
        #VIDAS
        fuente = pygame.font.Font(None, 36)
        texto_vidas = fuente.render("Vidas: " + str(VIDAS), True, BLANCO)
        pantalla_ppal.blit(texto_vidas, (10, 10))
        #TIEMPO
        fuente = pygame.font.Font(None, 36)
        texto_tiempo = fuente.render("Tiempo: {:02d}:{:02d}".format(minutos, segundos), True, BLANCO)
        pantalla_ppal.blit(texto_tiempo, (ANCHO - texto_tiempo.get_width() - 10, 10))
        fuente = pygame.font.Font(None, 36)
        #PUNTUACION
        texto_puntuacion = fuente.render("Puntuación: {}".format(puntuacion), True, BLANCO)
        posicion_texto = (ANCHO // 2 - texto_puntuacion.get_width() // 2, 10)
        pantalla_ppal.blit(texto_puntuacion, posicion_texto)
        all_sprites.draw(pantalla_ppal)
        pygame.display.flip()

        # Limitamos la velocidad de actualización
        reloj.tick(FPS)

    # Salimos del juego
    pygame.quit()

elif estado_juego == 2:
    
    def mostrar_ranking():
        resultado = funciones_sql.obtener_puntuaciones()
    
        pantalla = pygame.display.set_mode((800, 600))
        fuente = pygame.font.Font(None, 36)
        puntaje_titulo = fuente.render("TOP PUNTAJES", True, BLANCO)
        pantalla.blit(puntaje_titulo, (800 // 2 - 160, 600 // 2 -250))
        columna_nombre = fuente.render("NOMBRE", True, BLANCO)
        columna_puntos = fuente.render("PUNTAJE", True, BLANCO)
        pantalla.blit(columna_nombre, (600 // 2 - 135, 140))
        pantalla.blit(columna_puntos, (600 // 2 + 70, 140))
    
        y = -120
        for nombre, puntuacion in resultado:
            fuente = pygame.font.Font(None, 36)
            nombre_texto = fuente.render(nombre, True, BLANCO)
            puntaje_texto = fuente.render(str(puntuacion), True, BLANCO)
            pantalla.blit(nombre_texto, (800 //2 -235, 600//2 + y))                                     
            pantalla.blit(puntaje_texto, (800 // 2 - 20, 600 // 2 + y))
            y += 30

    mostrar_ranking()
    pygame.display.flip()
    pygame.time.wait(3000)
