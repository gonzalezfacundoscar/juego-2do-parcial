import pygame
import random

class Bloque(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, color):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    @staticmethod
    def crear_bloques(cantidad, ancho, alto):
        block_width = ancho
        block_height = alto
        block_rows = 5
        block_cols = cantidad // block_rows

        blocks = pygame.sprite.Group()

        for row in range(block_rows):
            for col in range(block_cols):
                x = col * (block_width + 10) + 20
                y = row * (block_height + 10) + 55
                color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
                block = Bloque(x, y, block_width, block_height, color)
                blocks.add(block)

        return blocks