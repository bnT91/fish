from pathlib import Path


class Settings:
    def __init__(self):
        self.BASE_DIRECTORY = Path(__file__).resolve().parent.parent
        self.BACKGROUND_COLOR = (63, 208, 212)
        self.ANIMATION_CONSTANT = 30
