from game import Game
import pygame


class App:
    def __init__(self):
        self.game = Game()

    def run(self):
        self.game.run()


if __name__ == '__main__':
    pygame.init()
    app = App()
    app.run()
