from PyQt5.QtWidgets import QWidget
from Helpers.label_helper import create_label

class ComputersTurn(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        self.game_logic = game_logic
        self.setup_ui()
        game_logic.set_background(self, r"Images/table.png")  # Add your image path

    def setup_ui(self):
        self.resize(1280, 720)

        self.title = create_label(self, "Computer's Turn", 150, "center", "center", "red")

