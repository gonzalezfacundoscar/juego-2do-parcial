import pygame
from colores import*

def dibujar_menu():
    
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menú")

    
    fuente_titulo = pygame.font.Font(None, 40)
    fuente_opciones = pygame.font.Font(None, 30)

    while True:
        pantalla.fill((0, 0, 0)) 

        titulo = fuente_titulo.render("Menú", True, BLANCO)
        opcion_jugar = fuente_opciones.render("1. Jugar", True, BLANCO)
        opcion_mostrar_menu = fuente_opciones.render("2. Mostrar puntuaciones", True, BLANCO)

        pantalla.blit(titulo, (50, 50))
        pantalla.blit(opcion_jugar, (50, 150))
        pantalla.blit(opcion_mostrar_menu, (50, 200))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1                    
                elif event.key == pygame.K_2:
                    return 2
                    
            


                        
                    