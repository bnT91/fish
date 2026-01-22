import pygame
from itertools import cycle
from settings import *


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()

        self.trying_to_catch = False

        self.sprite = pygame.image.load(self.settings.BASE_DIRECTORY / "sprites/player1.png").convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (44, 64))

        self.anim1 = pygame.transform.scale(
            pygame.image.load(self.settings.BASE_DIRECTORY / "sprites/player1.png").convert_alpha(), (44, 64))
        self.anim2 = pygame.transform.scale(
            pygame.image.load(self.settings.BASE_DIRECTORY / "sprites/player2.png").convert_alpha(), (44, 64))

        self.anim_counter = 0
        self.anims = [self.anim1, self.anim2]
        self.anims_iter = cycle(self.anims)

        self.cooldown = False
        self.cooldown_time = 0
        self.counter = 0

        self.immortality = True
        self.imm_frame = self.settings.fps
        self.const = 2

        self.speed = 5
        self.lives = 3
        self.score = 0
        self.dead = False

        self.death_sfx = pygame.mixer.Sound(self.settings.BASE_DIRECTORY / "sounds/death.mp3")
        self.death_sfx2 = pygame.mixer.Sound(self.settings.BASE_DIRECTORY / "sounds/death2.mp3")
        self.minus_live_sfx = pygame.mixer.Sound(self.settings.BASE_DIRECTORY / 'sounds/minus_live.mp3')

        self.w, self.h = self.screen.get_size()

        self.centerx, self.centery = self.w / 2 - self.sprite.width / 2, self.h - self.sprite.height - 20
        self.rect = pygame.rect.Rect(self.centerx, self.centery, self.sprite.width, self.sprite.height)

    def try_to_catch(self):
        if not self.cooldown:
            self.trying_to_catch = True

    def minus_live(self):
        if not self.immortality:
            self.minus_live_sfx.play()
            self.lives -= 1
            self.rect.x = self.w / 2 - self.sprite.width / 2
            self.immortality = True
            self.imm_frame = self.settings.fps * self.const
            if not self.lives:
                self.dead = True
                pygame.Sound.play(self.death_sfx2, maxtime=5000)
                pygame.time.set_timer(pygame.USEREVENT+2, 5000, loops=1)


    def update(self):
        if self.immortality:
            self.imm_frame -= 1
            if self.imm_frame <= 0:
                self.immortality = False
        self.anim_counter += 1
        self.anim_counter = self.anim_counter % self.settings.ANIMATION_CONSTANT
        if not self.anim_counter:
            self.sprite = next(self.anims_iter)
        if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
            self.rect.x += self.speed
        elif pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
            self.rect.x -= self.speed
        if self.rect.x < 64:
            self.rect.x = 64
            self.minus_live()
        if self.rect.x > self.w - self.rect.width - 64:
            self.rect.x = self.w - self.rect.width - 64
            self.minus_live()
        if self.cooldown:
            self.counter += 1
            if self.counter == self.settings.fps:
                self.cooldown_time -= 1
                if not self.cooldown_time:
                    self.cooldown = False
                    self.cooldown_time = 0
                self.counter = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.cooldown:
                self.try_to_catch()
                return "trying to catch"
        return None

    def draw(self):
        self.screen.blit(self.sprite, self.rect)
