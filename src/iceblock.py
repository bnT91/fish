import pygame
import random
import settings

class Iceblock:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y

        self.settings = settings.Settings()

        self.sprites = [pygame.image.load(self.settings.BASE_DIRECTORY / "sprites" / "iceblock1.png").convert_alpha()] # размер спрайта 32х32

        self.sprite = random.choice(self.sprites)
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))

    def move(self, z, t):
        self.x += z
        self.y += t
        if self.x < 0 or self.x > self.screen.get_width() or self.y < 0 or self.y > self.screen.get_height():
            return True
        return False

    def collide(self, sprite):
        pass

    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))