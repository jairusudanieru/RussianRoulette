from PyQt5.QtWidgets import QWidget
from Helpers.label_helper import create_label
from Helpers.button_helper import create_button

class GuideScreen(QWidget):
    def __init__(self, game_logic):
        super().__init__()
        self.game_logic = game_logic
        self.setup_ui()
        game_logic.set_background(self, r"Images/black.jpg")

    def setup_ui(self):
        self.setFixedSize(1280, 720)

        self.title_label = create_label(self, "How To Play", 70, "center", 10, "red")
        self.guide_label = create_label(self, "Click \"Play\" in the main menu to begin.\n\nPlayer's Turn:\n\nYou have two options:\nShoot Yourself: Risk firing the bullet at yourself.\nShoot Computer: Pass the turn and fire at the computer.\n\nGame Flow:\n\n- Player Turn:\nWhen you choose \"Shoot Yourself,\" there are 20% chance that the bullet will be a live bullet and you'll kill yourself.\n- Computer Turn:\nThe computer automatically pulls the trigger, either shot you or shot itself.\n- Safety Check:\nIf the shot is empty, the turn passes to the next player.\nIf the bullet fires, the game ends.", 20, "center", "center", "red")

        self.back_button = create_button(self, "Back to Menu", 30, "center", 650)

        self.back_button.clicked.connect(lambda: self.game_logic.go_to_menu_screen())