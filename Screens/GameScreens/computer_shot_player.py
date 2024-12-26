from PyQt5.QtWidgets import QWidget
from Helpers.label_helper import create_label

class CSP(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        self.setup_ui()
        game_logic.set_background(self, r"Images/computer_shot_player.png")  # Add your image path

    def setup_ui(self):
        self.resize(1280, 720)

        self.title = create_label(self, "Computer shooting you", 100, "center", 50, "#660000")

