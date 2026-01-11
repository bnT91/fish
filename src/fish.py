import pygame

class Fish:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y

    def move(self, z, t):
        self.x += z
        self.y += t
        if self.x < 0 or self.x > self.screen.get_width() or self.y < 0 or self.y > self.screen.get_height():
            return True
        return False

    def update(self):
        pass

    def draw(self):
        pass