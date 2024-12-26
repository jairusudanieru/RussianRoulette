from PyQt5.QtCore import QPropertyAnimation, Qt
from PyQt5.QtWidgets import QWidget, QGraphicsOpacityEffect

class WhiteTransitionHelper:
    def __init__(self, parent, stacked_widget):
        """
        Initialize the transition helper.
        :param parent: The main application window or widget (should be a QWidget or subclass).
        :param stacked_widget: QStackedWidget managing the screens.
        """
        self.parent = parent  # This should be a QWidget or subclass (QMainWindow works)
        self.stacked_widget = stacked_widget

        # Ensure parent is of type QWidget or subclass (QMainWindow is also a QWidget)
        if not isinstance(self.parent, QWidget):
            print(f"Parent type: {type(self.parent)}")  # Debugging output
            raise TypeError("Parent must be a QWidget or subclass.")

        # Black overlay for transition effect
        self.white_overlay = QWidget(self.parent)  # Here we pass the parent QWidget
        self.white_overlay.setGeometry(0, 0, 1280, 720)
        self.white_overlay.setStyleSheet("background-color: white;")
        self.white_overlay.raise_()
        self.white_overlay.setAttribute(Qt.WA_TransparentForMouseEvents)

        # Opacity effect for fading in/out
        self.overlay_effect = QGraphicsOpacityEffect(self.white_overlay)
        self.white_overlay.setGraphicsEffect(self.overlay_effect)
        self.overlay_effect.setOpacity(0.0)

    def fade_and_switch(self, target_screen):
        """
        Initiates a fade-in transition, switches the screen, and fades out.
        :param target_screen: The QWidget to switch to.
        """
        # Hide mouse cursor and disable mouse interaction
        self.parent.setCursor(Qt.BlankCursor)
        self.white_overlay.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.white_overlay.raise_()

        # Fade in the overlay
        self.fade_in_animation = self.create_fade_animation(self.overlay_effect, 0.0, 1.0, duration=100)
        self.fade_in_animation.finished.connect(lambda: self.switch_and_fade_out(target_screen))
        self.fade_in_animation.start()

    def switch_and_fade_out(self, target_screen):
        """
        Switches to the target screen and starts the fade-out effect.
        :param target_screen: The QWidget to switch to.
        """
        # Switch the current screen in the stacked widget
        self.stacked_widget.setCurrentWidget(target_screen)

        # Fade out the overlay
        self.fade_out_animation = self.create_fade_animation(self.overlay_effect, 1.0, 0.0, duration=100)
        self.fade_out_animation.finished.connect(self.restore_mouse)
        self.fade_out_animation.start()

    def restore_mouse(self):
        """
        Restores mouse visibility and re-enables mouse events after transition.
        """
        self.parent.setCursor(Qt.ArrowCursor)
        self.white_overlay.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    def create_fade_animation(self, target, start_opacity, end_opacity, duration):
        """
        Creates a QPropertyAnimation for opacity transitions.
        :param target: The graphics effect target (e.g., QGraphicsOpacityEffect).
        :param start_opacity: Starting opacity value (0.0 to 1.0).
        :param end_opacity: Ending opacity value (0.0 to 1.0).
        :param duration: Duration of the animation in milliseconds.
        :return: QPropertyAnimation object.
        """
        animation = QPropertyAnimation(target, b"opacity")
        animation.setDuration(duration)
        animation.setStartValue(start_opacity)
        animation.setEndValue(end_opacity)
        return animation
