import pygame
import random

from settings import Settings

class Fish:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y

        self.settings = Settings()

        self.sprites = [pygame.image.load(self.settings.BASE_DIRECTORY / "sprites" / "fish1.png").convert_alpha(),
                        pygame.image.load(self.settings.BASE_DIRECTORY / "sprites" / "fish2.png").convert_alpha(),
                        pygame.transform.flip(pygame.image.load(self.settings.BASE_DIRECTORY / "sprites" / "fish1.png").convert_alpha(), True, False),
                        pygame.transform.flip(pygame.image.load(self.settings.BASE_DIRECTORY / "sprites" / "fish2.png").convert_alpha(), True, False)]

        self.sprite = random.choice(self.sprites)
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))

    def move(self, z, t):
        self.x += z
        self.y += t
        if self.x < 0 or self.x > self.screen.get_width() or self.y < 0 or self.y > self.screen.get_height():
            return True
        return False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))