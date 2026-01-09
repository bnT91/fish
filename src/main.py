import os
os.environ["SDL_VIDEODRIVER"] = "windows"  # заставляем использовать Windows driver

import pygame
pygame.init()

from game import Game


class App:
    def __init__(self):
        self.game = Game()

    def run(self):
        self.game.run()


if __name__ == '__main__':
    print(pygame.display.get_driver())
    app = App()
    app.run()
