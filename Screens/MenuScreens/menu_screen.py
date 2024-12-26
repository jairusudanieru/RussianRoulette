from PyQt5.QtWidgets import *
from Helpers.button_helper import create_button
from Helpers.label_helper import create_label

class MenuScreen(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        self.game_logic = game_logic
        self.setup_ui()
        game_logic.set_background(self, r"Images/table.png")

    def setup_ui(self):
        self.setFixedSize(1280, 720)

        self.title_label = create_label(self, "RUSSIAN ROULETTE", 150, "center", 50, "#660000")

        self.play_button = create_button(self, "Play",100,"center", 300)
        self.guide_button = create_button(self, "Guide",100,"center", 420)
        self.quit_button = create_button(self, "Quit",100,"center", 540)

        self.play_button.clicked.connect(lambda: self.game_logic.go_to_table_pov())
        self.guide_button.clicked.connect(lambda: self.game_logic.go_to_guide_screen())
        self.quit_button.clicked.connect(lambda: QApplication.quit())
