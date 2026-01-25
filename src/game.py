import sys
print(sys.executable)
print(sys.version)

import pygame
import math

from object_generator import ObjectGenerator
from player import Player
from starting_screen import StartingScreen
from death_screen import DeathScreen
from score import Score
from background import Background

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
        self.last_state = "st_scr"
        self.death_screen_counter = 0
        self.flaggg = True
        self.restart_or_not = False

        self.clock = pygame.time.Clock()
        self.vertical_speed = VerticalSpeed()
        self.V_SPD_SCORE_INCREASE_const = 5

        self.starting_screen = StartingScreen(screen=self.screen)
        self.player = Player(screen=self.screen)
        self.generator = ObjectGenerator(screen=self.screen, v_spd=self.vertical_speed, player=self.player)
        self.red_spikes = Background(screen=self.screen, v_spd=self.vertical_speed)
        self.score = Score(screen=self.screen, player=self.player)
        self.death_screen = DeathScreen(screen=self.screen, player=self.player)

    def manage_consts(self):
        self.vertical_speed.update(5+math.floor(self.player.score/self.V_SPD_SCORE_INCREASE_const))

        if self.player.score >= 6:
            self.settings.set_cldwn_const(2)
        if self.player.score >= 11:
            self.settings.set_cldwn_const(1)
        if self.player.score >= 20:
            self.settings.set_cldwn_const(0)

        if self.player.score <= 20:
            self.generator.set_freq(30 - math.floor(self.player.score/2.5))
            self.settings.set_sc_delta(2)
        if self.player.score == 25:
            self.generator.set_freq(17)
        if self.player.score == 30:
            self.settings.set_sc_delta(3)
        if self.player.score == 35:
            self.generator.set_freq(10)
        if self.player.score == 50:
            self.generator.set_freq(7)
            self.settings.set_sc_delta(5)
        if self.player.score == 100:
            self.generator.set_freq(4)
            self.settings.set_sc_delta(10)

    def update(self):  # updating all positions, variables etc
        if self.state == "st_scr":
            self.starting_screen.update()
            if self.starting_screen.finished:
                self.state = "game"
        elif self.state == "game":
            self.player.update()
            self.red_spikes.update()
            self.generator.update()
            self.score.update()
            if self.player.dead:
                self.state = "dth_scr"
        elif self.state == "dth_scr":
            self.death_screen_counter += 1
            if self.death_screen_counter >= 5 and self.flaggg:
                self.flaggg = False
                self.death_screen = DeathScreen(screen=self.screen, player=self.player)
            self.death_screen.update()

        self.manage_consts()
    def draw(self):  # blitting everything
        self.screen.fill(self.settings.BACKGROUND_COLOR)

        if self.state == "st_scr":
            self.starting_screen.draw()
        elif self.state == "game":
            self.red_spikes.draw()
            self.generator.draw()
            self.player.draw()
            self.score.draw()
        elif self.state == "dth_scr":
            self.death_screen.draw()


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
                        self.player.cooldown = True
                        self.player.cooldown_time = self.settings.COOLDOWN_CONSTANT
                        self.player.trying_to_catch = False
                        self.generator.catch()
                elif self.state == "dth_scr":
                    self.restart_or_not = self.death_screen.handle_event(event)
                    if self.restart_or_not:
                        self.player.death_sfx.stop()
                        self.player.death_sfx2.stop()
                        self.__init__()
                if event.type == pygame.USEREVENT + 2 and self.state == "dth_scr":
                    pygame.Sound.play(self.player.death_sfx)
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            self.clock.tick(self.settings.fps)
        pygame.quit()
