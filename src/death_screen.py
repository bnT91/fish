import pickle

import pygame
from settings import Settings

from utils import *

class DeathScreen:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

        self.w, self.h = screen.get_size()
        self.settings = Settings()

        self.new_best = False

        self.you_died_font = pygame.font.SysFont("Serif", 70, True)
        self.you_died_label = self.you_died_font.render("You died!", True, (92, 7, 17))
        self.you_died_rect = self.you_died_label.get_rect(topleft=(self.w / 2 - self.you_died_label.get_width() / 2,
                                                                   self.h / 2 - self.you_died_label.get_height() / 2))

        self.restart_font = pygame.font.SysFont("Serif", 36, True)
        self.restart_label = self.restart_font.render("Restart", True, (250, 250, 250))
        self.restart_rect = self.restart_label.get_rect(
            bottomright=(self.screen.get_width() - 10, self.screen.get_height() - 10))
        self.restart_bg_rect = pygame.Rect(self.screen.get_width() - self.restart_label.get_width() - 15,
                                           self.screen.get_height() - self.restart_label.get_height() - 15,
                                           self.restart_rect.width + 10, self.restart_rect.height + 10)

        scpath = get_scoreboard_path()

        if scpath.exists():
            with open(scpath, "rb") as file:
                self.best_score = pickle.load(file)
        else:
            self.best_score = 0

        if self.player.score > self.best_score:
            self.new_best = True
            self.best_score = self.player.score

            self.new_best_grats_font = pygame.font.SysFont("Serif", 90, False, True)
            self.new_best_grats_label = self.new_best_grats_font.render(f"Yaaay! New best!", True, (0, 0, 255))
            self.new_best_grats_rect = self.new_best_grats_label.get_rect(center=(self.w / 2, self.h * 2 / 3))

            with open(scpath, "wb") as file:
                # noinspection PyTypeChecker
                pickle.dump(self.best_score, file)

        self.score_font = pygame.font.SysFont("Serif", 36)
        self.score_label = self.score_font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        self.score_rect = self.score_label.get_rect(topleft=(30, 30))

        self.best_sc_font = pygame.font.SysFont("Serif", 36)
        self.best_sc_label = self.best_sc_font.render(f"Best score: {self.best_score}", True, (60, 255, 0))
        self.best_sc_rect = self.best_sc_label.get_rect(topleft=(self.w - self.best_sc_label.get_width() - 30, 30))

    def update(self):
        pass

    @staticmethod
    def handle_event(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
        return False

    def draw(self):
        self.screen.fill((0, 0, 0))

        pygame.draw.rect(self.screen, (0, 125, 100), self.restart_bg_rect, border_radius=10)
        pygame.draw.rect(self.screen, (255, 255, 255), self.restart_bg_rect, width=2, border_radius=10)

        self.screen.blit(self.restart_label, self.restart_rect)
        self.screen.blit(self.you_died_label, self.you_died_rect)
        self.screen.blit(self.score_label, self.score_rect)
        self.screen.blit(self.best_sc_label, self.best_sc_rect)

        if self.new_best:
            self.screen.blit(self.new_best_grats_label, self.new_best_grats_rect)
