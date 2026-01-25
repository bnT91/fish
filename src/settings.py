from pathlib import Path


class Settings:
    def __init__(self):
        self.fps = 60
        self.COOLDOWN_CONSTANT = 3
        self.BASE_DIRECTORY = Path(__file__).resolve().parent.parent
        self.BACKGROUND_COLOR = (21, 147, 175)
        self.ANIMATION_CONSTANT = 30
        self.SCORE_DELTA = 1

    def set_cldwn_const(self, new_value):
        self.COOLDOWN_CONSTANT = new_value

    def set_sc_delta(self, new_value):
        self.SCORE_DELTA = new_value