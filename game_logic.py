from PyQt5.QtWidgets import QLabel, QStackedWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import random

from Transitions.black_transition_helper import BlackTransitionHelper
from Transitions.red_transition_helper import RedTransitionHelper
from Transitions.white_transition_helper import WhiteTransitionHelper

class GameLogic:
    def __init__(self, stacked_widget: QStackedWidget, main_app):
        self.stacked_widget = stacked_widget
        self.main_app = main_app

        # Initialize Transition Helpers
        self.black_transition_helper = BlackTransitionHelper(main_app, self.stacked_widget)
        self.red_transition_helper = RedTransitionHelper(main_app, self.stacked_widget)
        self.white_transition_helper = WhiteTransitionHelper(main_app, self.stacked_widget)

    def change_screen(self, screen_index):
        """Switches between screens."""
        self.stacked_widget.setCurrentIndex(screen_index)

    def set_background(self, widget, image_path):
        # Create a QLabel to hold the background image
        background_label = QLabel(widget)
        background_label.setPixmap(QPixmap(image_path))  # Load the image
        background_label.setGeometry(0, 0, widget.width(), widget.height())  # Set position and size
        background_label.setScaledContents(True)  # Scale image to fit the label size

        # Place the QLabel in the background
        background_label.lower()  # Move the background label behind other widgets
        widget.background_label = background_label  # Keep reference to prevent garbage collection\

    # Computer Turn
    def start_computers_turn(self):
        if random.randint(1, 2) == 1:
            QTimer.singleShot(2000, lambda: self.go_to_csp())
        else:
            QTimer.singleShot(2000, lambda: self.go_to_csc())


    # Menu Screens
    def go_to_start_screen(self):
        self.black_transition_helper.fade_and_switch(self.main_app.start_screen)

    def go_to_menu_screen(self):
        self.black_transition_helper.fade_and_switch(self.main_app.menu_screen)

    def go_to_guide_screen(self):
        self.black_transition_helper.fade_and_switch(self.main_app.guide_screen)

    def go_to_table_pov(self):
        self.black_transition_helper.fade_and_switch(self.main_app.players_turn)

    def get_bullets(self):
        return random.randint(1, 5)

    # Game Screens
    def go_to_psp(self):
        self.black_transition_helper.fade_and_switch(self.main_app.player_shot_player)

        if self.get_bullets() == 1:
            QTimer.singleShot(3000, lambda: self.red_transition_helper.fade_and_switch(self.main_app.player_loses))
        else:
            QTimer.singleShot(2000, lambda: self.white_transition_helper.fade_and_switch(self.main_app.player_survives))
            QTimer.singleShot(3000, lambda: self.black_transition_helper.fade_and_switch(self.main_app.computers_turn))
            QTimer.singleShot(5000, lambda: self.start_computers_turn())

    def go_to_psc(self):
        self.black_transition_helper.fade_and_switch(self.main_app.player_shot_computer)

        if self.get_bullets() == 1:
            QTimer.singleShot(3000, lambda: self.red_transition_helper.fade_and_switch(self.main_app.computer_loses))
        else:
            QTimer.singleShot(2000, lambda: self.white_transition_helper.fade_and_switch(self.main_app.computer_survives))
            QTimer.singleShot(3000, lambda: self.black_transition_helper.fade_and_switch(self.main_app.computers_turn))
            QTimer.singleShot(5000, lambda: self.start_computers_turn())

    def go_to_csp(self):
        self.black_transition_helper.fade_and_switch(self.main_app.computer_shot_player)

        if self.get_bullets() == 1:
            QTimer.singleShot(3000, lambda: self.red_transition_helper.fade_and_switch(self.main_app.player_loses))
        else:
            QTimer.singleShot(2000, lambda: self.white_transition_helper.fade_and_switch(self.main_app.player_survives))
            QTimer.singleShot(3000, lambda: self.black_transition_helper.fade_and_switch(self.main_app.players_turn))

    def go_to_csc(self):
        self.black_transition_helper.fade_and_switch(self.main_app.computer_shot_computer)

        if self.get_bullets() == 1:
            QTimer.singleShot(3000, lambda: self.red_transition_helper.fade_and_switch(self.main_app.computer_loses))
        else:
            QTimer.singleShot(2000, lambda: self.white_transition_helper.fade_and_switch(self.main_app.computer_survives))
            QTimer.singleShot(3000, lambda: self.black_transition_helper.fade_and_switch(self.main_app.players_turn))


