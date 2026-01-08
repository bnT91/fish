import pygame
from settings import *


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()

        self.trying_to_catch = False

        self.sprite = pygame.image.load(self.settings.BASE_DIRECTORY / "sprites/player.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (44, 64))
        self.speed = 5
        self.lives = 3
        self.score = 0
        self.centerx, self.centery = self.screen.width / 2 - self.sprite.width / 2, self.screen.height - self.sprite.height - 20
        self.rect = pygame.rect.Rect(self.centerx, self.centery, self.sprite.width, self.sprite.height)

    def try_to_catch(self):
        self.trying_to_catch = True

    def minus_live(self):
        self.lives -= 1
        # death animation

    def update(self):
        if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            self.rect.x += self.speed
        elif pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
            self.rect.x -= self.speed

        if self.rect.x < 64 or self.rect.x > self.screen.width - self.rect.width - 64:
            self.minus_live()
            self.rect.x = self.screen.width/2-self.sprite.width/2

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.try_to_catch()
            return "trying to catch"
        return None

    def draw(self):
        self.screen.blit(self.sprite, self.rect)
