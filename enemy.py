import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.position = pygame.Vector2(x,y)
        self.image = pygame.Surface((40,60))
        self.image.fill((200,50,50))
        self.rect = self.image.get_rect(center=self.position)
