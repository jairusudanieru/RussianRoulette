from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from Helpers.label_helper import create_label

class StartScreen(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        self.game_logic = game_logic  # Store a reference to MainApp
        self.setup_ui()
        game_logic.set_background(self, r"Images/table.png")

    def setup_ui(self):
        self.setFixedSize(1280, 720)

        self.title_label = create_label(self, "RUSSIAN ROULETTE", 175, "center", 250, "#660000")
        self.creator_label = create_label(self, "Created by: Christian Ivan Cerbolles", 50, "center", 460, "#660000")

        QTimer.singleShot(2000, self.game_logic.go_to_menu_screen)

