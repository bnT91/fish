import random

import pygame

from fish import Fish
from iceblock import Iceblock
from settings import Settings


class ObjectGenerator:
    def __init__(self, screen, player, v_spd):
        self.screen = screen
        self.fishlist = []
        self.icelist = []

        self.DELTA = 64
        self.X = 5
        self.frame = 1
        self.FREQUENCY = 30

        self.settings = Settings()

        self.cought_sound = pygame.mixer.Sound(self.settings.BASE_DIRECTORY / 'sounds/cought.mp3')

        self.player = player
        self.v_spd = v_spd

    def spawn(self):
        genx, geny = random.randint(64, self.screen.get_width() - 97), random.randint(200, self.screen.get_height() - 100)
        for i in range(self.X):
            genx, geny = random.randint(64, self.screen.get_width() - 97), random.randint(100, self.screen.get_height() - 100)
            for piece in self.fishlist + self.icelist:
                if abs(piece.y - geny) <= self.DELTA or abs(piece.x - genx) <= self.DELTA:
                    break
            else:
                break
        else:
            return None
        _type = random.randint(0, 2)
        if _type:
            self.fishlist.append(Fish(self.screen, x=genx, y=geny))
            return "F"
        else:
            self.icelist.append(Iceblock(self.screen, x=genx, y=geny))
            return "I"

    def catch(self):
        flaggy = False
        for fishy in self.fishlist:
            if self.player.rect.colliderect(fishy):
                flaggy = True
        if flaggy:
            self.player.score += 1
            self.cought_sound.play()

    def minus_live(self):
        self.player.minus_live()

    def update(self):
        self.fishlist = [ifish for ifish in self.fishlist if not ifish.move(0, self.v_spd.get())]
        self.icelist = [iice for iice in self.icelist if not iice.move(0, self.v_spd.get())]
        for piece in self.fishlist + self.icelist:
            piece.update()
        for iceblock in self.icelist:
            if iceblock.collide(self.player):
                self.minus_live()
        self.frame += 1
        self.frame = self.frame % self.FREQUENCY
        if not self.frame:
            self.spawn()

    def draw(self):
        for iceblock in self.icelist:
            iceblock.draw()

        for fish in self.fishlist:
            fish.draw()
