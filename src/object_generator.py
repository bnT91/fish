import pygame

from fish import Fish
from iceblock import Iceblock

class ObjectGenerator:
    def __init__(self, screen, player, v_spd):
        self.screen = screen
        self.fishlist = [Fish(self.screen, 10, 10)]
        self.icelist = []

        self.player = player
        self.v_spd = v_spd

    def catch(self):
        pass

    def update(self):
        self.fishlist = [ifish for ifish in self.fishlist if not ifish.move(0, self.v_spd.get())]
        self.icelist = [iice for iice in self.icelist if not iice.move(0, self.v_spd.get())]
        for fish in self.fishlist:
            print(fish.y)

    def draw(self):
        for iceblock in self.icelist:
            iceblock.draw()

        for fish in self.fishlist:
            fish.draw()
