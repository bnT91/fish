from pathlib import Path
import os

def get_appdata_dir():
    base = Path(os.getenv("APPDATA")) / "RoyalIceRybalka"
    base.mkdir(exist_ok=True)
    return base

def get_scoreboard_path():
    path = get_appdata_dir() / "scoreboard"
    path.mkdir(exist_ok=True)
    return path / "best.pkl"
