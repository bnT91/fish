from pathlib import Path


class Settings:
    def __init__(self):
        self.fps = 60
        self.COOLDOWN_CONSTANT = 5
        self.BASE_DIRECTORY = Path(__file__).resolve().parent.parent
        self.BACKGROUND_COLOR = (21, 147, 175)
        self.ANIMATION_CONSTANT = 30
