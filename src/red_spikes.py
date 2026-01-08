import pygame
from settings import Settings

class RedSpikes:
    def __init__(self, screen, v_spd):
        self.settings = Settings()

        self.screen = screen
        self.sprite = pygame.image.load(self.settings.BASE_DIRECTORY / "sprites/red_spikes.png").convert_alpha()

        self.v_spd = v_spd
        self.rect_1, self.rect_2 = self.sprite.get_rect(topleft=(0, 0)), self.sprite.get_rect(topleft=(0, -self.screen.height))

    def update(self):
        self.rect_1.y += self.v_spd.get()
        self.rect_2.y += self.v_spd.get()
        if self.rect_1.topleft[1] > self.screen.height:
            self.rect_1.y = -self.screen.height
        if self.rect_2.topleft[1] > self.screen.height:
            self.rect_2.y = -self.screen.height
        if abs(self.rect_1.topleft[1]-self.rect_2.topleft[1]) != 700:
            if self.rect_1.topleft[1] > self.rect_2.topleft[1]:
                self.rect_2.y = self.rect_1.y - 700
            elif self.rect_1.topleft[1] < self.rect_2.topleft[1]:
                self.rect_1.y = self.rect_2.y - 700

    def draw(self):
        self.screen.blit(self.sprite, self.rect_1)
        self.screen.blit(self.sprite, self.rect_2)