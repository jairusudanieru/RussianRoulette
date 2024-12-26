from PyQt5.QtWidgets import QWidget
from Helpers.label_helper import create_label
from Helpers.button_helper import create_button

class ComputerLoses(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        self.game_logic = game_logic
        self.setup_ui()
        game_logic.set_background(self, r"Images/black.jpg")  # Add your image path

    def setup_ui(self):
        self.resize(1280, 720)

        self.title = create_label(self, "YOU WON", 200, "center", "center", "red")

        self.back_button = create_button(self, "Back to Menu", 30, "center", 650)

        self.back_button.clicked.connect(lambda: self.game_logic.go_to_menu_screen())

