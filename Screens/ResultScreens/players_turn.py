from PyQt5.QtWidgets import QWidget
from Helpers.button_helper import create_button
from Helpers.label_helper import create_label

class PlayersTurn(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        self.game_logic = game_logic
        self.setup_ui(game_logic)
        game_logic.set_background(self, r"Images/table.png")  # Set the initial background

    def setup_ui(self, game_logic):
        self.setFixedSize(1280, 720)

        self.title_label = create_label(self, "Your Turn", 80, "center", 50, "red")

        self.shot_yourself = create_button(self, "Shot Yourself", 120, "center", 250)
        self.shot_computer = create_button(self, "Shot Computer", 120, "center", 400)

        self.shot_yourself.clicked.connect(lambda: self.game_logic.go_to_psp())
        self.shot_computer.clicked.connect(lambda: self.game_logic.go_to_psc())
