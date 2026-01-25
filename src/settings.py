from pathlib import Path
import sys


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

    @staticmethod
    def resource_path(relative_path: str) -> Path:
        if hasattr(sys, "_MEIPASS"):
            return Path(sys._MEIPASS) / relative_path
        return Path(__file__).resolve().parent.parent / relative_path

    def set_sc_delta(self, new_value):
        self.SCORE_DELTA = new_value