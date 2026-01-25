import pygame


class StartingScreen:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font_title = pygame.font.SysFont("Serif", 72)
        self.font_button = pygame.font.SysFont("Serif", 32)

        self.title_text = self.font_title.render("Royal Ice Rybalka Fish", True, (255, 255, 255))

        self.button_text = self.font_button.render("Click to start", True, (255, 0, 0))
        self.button_rect = pygame.Rect(self.width / 2 - self.button_text.get_width() / 2,
                                       self.height / 2 - self.button_text.get_height() / 2,
                                       self.button_text.get_width() + 10,
                                       self.button_text.get_height() + 10)

        self.finished = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.finished = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.finished = True

    def update(self):
        pass

    def draw(self):
        self.screen.fill((30, 120, 200))
        title_rect = self.title_text.get_rect(center=(self.width / 2, self.height / 3))
        self.screen.blit(self.title_text, title_rect)

        button_outline_rect = pygame.Rect(self.width / 2 - self.button_text.get_width() / 2 - 5,
                                          self.height / 2 - self.button_text.get_height() / 2,
                                          self.button_text.get_width() + 10,
                                          self.button_text.get_height() + 10)
        pygame.draw.rect(self.screen, (240, 240, 240), button_outline_rect, border_radius=10)
        pygame.draw.rect(self.screen, (0, 0, 0), button_outline_rect, 2, border_radius=10)

        self.screen.blit(self.button_text, self.button_rect)
