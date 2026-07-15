from pathlib import Path

# Assets Pfad
ASSETS_PATH = Path(__file__).joinpath("..", "..", "assets").resolve()
# Fenstergröße festlegen
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
# Framerate Limit
FRAMERATE = 60

# API Adresse
API_BASE_URL = "http://localhost:8000"
