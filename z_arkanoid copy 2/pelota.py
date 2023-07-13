import pygame
from colores import*


class Pelota(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = 395
        self.rect.y = 200
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > 800:
            self.speed_x *= -1
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.speed_y *= -1       
