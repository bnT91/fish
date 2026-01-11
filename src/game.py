# todo: pause screen, restart button at death screen

import sys
print(sys.executable)
print(sys.version)

import pygame

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

        self.clock = pygame.time.Clock()
        self.vertical_speed = VerticalSpeed()

        self.starting_screen = StartingScreen(screen=self.screen)
        self.player = Player(screen=self.screen)
        self.generator = ObjectGenerator(screen=self.screen, v_spd=self.vertical_speed, player=self.player)
        self.red_spikes = Background(screen=self.screen, v_spd=self.vertical_speed)
        self.score = Score(screen=self.screen, player=self.player)
        self.death_screen = DeathScreen(screen=self.screen, player=self.player)

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
            self.death_screen.update()
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
                        self.generator.catch()
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
