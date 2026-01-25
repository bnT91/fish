import pygame
import random
import settings


class Iceblock:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y

        self.settings = settings.Settings()

        self.sprites = [pygame.transform.scale(
            pygame.image.load(self.settings.resource_path("sprites/iceblock1.png")).convert_alpha(), (64, 64)),
                        pygame.transform.scale(
                            pygame.image.load(self.settings.resource_path("sprites/iceblock2.png")).convert_alpha(),
                            (64, 64))]  # размер спрайта 32х32

        self.sprite = random.choice(self.sprites)
        self.rect = self.sprite.get_rect(topleft=(self.x, self.y))

    def move(self, z, t):
        self.x += z
        self.y += t
        if self.x < 0 or self.x > self.screen.get_width() or self.y < 0 or self.y > self.screen.get_height():
            return True
        return False

    def collide(self, player):
        if self.rect.colliderect(player):
            return True
        return False

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.sprite, (self.x, self.y))
