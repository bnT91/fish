# TODO
#   1) сделать слева и справа экрана красные полоски, касаясь которых, игрок будет терять жизнь / умирать (отдельный объект)
#   2) сделать объект PauseScreen
#   3) реализовать Score
#
#
#
#

import pygame

from fish_generator import FishGenerator
from player import Player
from iceblocks import Iceblocks
from starting_screen import StartingScreen
from death_screen import DeathScreen
from score import Score
from red_spikes import RedSpikes

from settings import Settings


class VerticalSpeed:
    def __init__(self):
        self.vert_speed = 5

    def get(self):
        return self.vert_speed

    def update(self, new_vert_speed):
        self.vert_speed = new_vert_speed

class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Royal Ice Rybalka Fish")
        pygame.display.set_icon(pygame.image.load(self.settings.BASE_DIRECTORY / "sprites/icon.png").convert_alpha())
        self.states = ["st_scr", "game", "dth_scr"]
        self.state = "st_scr"
        self.running = True

        self.clock = pygame.time.Clock()
        self.vertical_speed = VerticalSpeed()

        self.starting_screen = StartingScreen(screen=self.screen)
        self.player = Player(screen=self.screen)
        self.iceblocks = Iceblocks(screen=self.screen, v_spd=self.vertical_speed)
        self.fish_generator = FishGenerator(screen=self.screen, player=self.player, iceblocks=self.iceblocks, v_spd=self.vertical_speed)
        self.red_spikes = RedSpikes(screen=self.screen, v_spd=self.vertical_speed)
        self.score = Score(screen=self.screen, player=self.player)

    def update(self):  # updating all positions, variables etc
        pygame.display.update()

        if self.state == "st_scr":
            self.starting_screen.update()
            if self.starting_screen.finished:
                self.state = "game"
        elif self.state == "game":
            self.player.update()
            self.red_spikes.update()
            self.score.update()

    def draw(self):  # blitting everything
        self.screen.fill(self.settings.BACKGROUND_COLOR)

        if self.state == "st_scr":
            self.starting_screen.draw()
        elif self.state == "game":
            self.fish_generator.draw()
            self.iceblocks.draw()
            self.player.draw()
            self.red_spikes.draw()
            self.score.draw()

    def run(self):
        running = True
        while running:
            self.update()
            self.draw()
            for event in pygame.event.get():
                if self.state == "st_scr":
                    self.starting_screen.handle_event(event)
                elif self.state == "game":
                    player_state = self.player.handle_event(event)
                    if player_state == "trying to catch":
                        self.fish_generator.catch()
                if event.type == pygame.QUIT:
                    running = False
            self.clock.tick(60)
        self.running = False
        pygame.quit()
