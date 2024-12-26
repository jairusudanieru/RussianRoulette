import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow

from Screens.GameScreens.computer_shot_computer import CSC
from Screens.GameScreens.computer_shot_player import CSP
from Screens.GameScreens.player_shot_computer import PSC
from Screens.GameScreens.player_shot_player import PSP

from Screens.MenuScreens.guide_screen import GuideScreen
from Screens.MenuScreens.start_screen import StartScreen
from Screens.MenuScreens.menu_screen import MenuScreen

from Screens.ResultScreens.computer_loses import ComputerLoses
from Screens.ResultScreens.computer_survives import ComputerSurvives
from Screens.ResultScreens.computers_turn import ComputersTurn
from Screens.ResultScreens.player_loses import PlayerLoses
from Screens.ResultScreens.player_survives import PlayerSurvives
from Screens.ResultScreens.players_turn import PlayersTurn

from game_logic import GameLogic

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Russian Roulette")
        self.setFixedSize(1280, 720)

        self.stacked_widget = QStackedWidget()

        # Where all things happen
        self.logic = GameLogic(self.stacked_widget, self)

        # Screens with backgrounds
        self.start_screen = StartScreen(self.logic)
        self.menu_screen = MenuScreen(self.logic)
        self.guide_screen = GuideScreen(self.logic)

        self.player_shot_player = PSP(self.logic)
        self.player_shot_computer = PSC(self.logic)
        self.computer_shot_player = CSP(self.logic)
        self.computer_shot_computer = CSC(self.logic)

        self.computer_loses = ComputerLoses(self.logic)
        self.computer_survives = ComputerSurvives(self.logic)
        self.computers_turn = ComputersTurn(self.logic)
        self.player_loses = PlayerLoses(self.logic)
        self.player_survives = PlayerSurvives(self.logic)
        self.players_turn = PlayersTurn(self.logic)

        # Add screens to stacked widget
        self.stacked_widget.addWidget(self.start_screen)
        self.stacked_widget.addWidget(self.menu_screen)
        self.stacked_widget.addWidget(self.guide_screen)

        self.stacked_widget.addWidget(self.computer_shot_computer)
        self.stacked_widget.addWidget(self.computer_shot_player)
        self.stacked_widget.addWidget(self.player_shot_computer)
        self.stacked_widget.addWidget(self.player_shot_player)

        self.stacked_widget.addWidget(self.computer_loses)
        self.stacked_widget.addWidget(self.computer_survives)
        self.stacked_widget.addWidget(self.computers_turn)
        self.stacked_widget.addWidget(self.player_loses)
        self.stacked_widget.addWidget(self.player_survives)
        self.stacked_widget.addWidget(self.players_turn)

        self.setCentralWidget(self.stacked_widget)  # Set stacked widget as central widget
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())