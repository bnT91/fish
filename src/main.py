from game import Game


class App:
    def __init__(self):
        self.game = Game()

    def run(self):
        self.game.run()


if __name__ == '__main__':
    app = App()
    app.run()
