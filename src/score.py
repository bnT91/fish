import pygame

class Score:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

        self.score_font = pygame.font.SysFont("Serif", 36)
        self.lives_font = pygame.font.SysFont("Serif", 36)

        self.score_label = self.score_font.render(f"Score: {self.player.score}", True, (0, 0, 0))
        self.lives_label = self.lives_font.render(f"Lives: {self.player.lives}", True, (0, 0, 0))

        self.variable = self.lives_label.get_width() + 115

        self.sc_rect = self.score_label.get_rect(topleft=(100, 30))
        self.lvs_rect = self.lives_label.get_rect(topleft=(self.screen.get_width() - self.lives_label.get_width() - 115, 30))

    def update(self):
        self.score_label = self.score_font.render(
            f"Score: {self.player.score}", True, (0, 0, 0))
        self.sc_rect = self.score_label.get_rect(topleft=(100, 30))

        self.lives_label = self.lives_font.render(
            f"Lives: {self.player.lives*"♥"}", True, (255, 0, 0))
        self.lvs_rect = self.lives_label.get_rect(
            topleft=(self.screen.get_width() - self.variable, 30))

    def draw(self):
        self.screen.blit(self.score_label, self.sc_rect)
        self.screen.blit(self.lives_label, self.lvs_rect)
