from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QFontDatabase

def create_button(parent, text, font_size, x, y):
    """
    Create a button with custom styling, shadow, and positioning.
    """
    # Load the custom font
    font_id = QFontDatabase.addApplicationFont(r"Fonts/creepster.ttf")
    if font_id == -1:
        print("Failed to load font!")

    # Create the button
    button = QPushButton(text, parent)
    button.setStyleSheet(f"""
        QPushButton {{
            text-align: center;
            color: red;                     
            font-size: {font_size}px;
            font-weight: bold;
            border-radius: 10px;
            font-family: 'Creepster';
            background: transparent;
        }}
        QPushButton:hover {{
            color: #660000;
        }}
    """)

    button.adjustSize()

    # button.resize(width, height)

    if x == "center":
        x = (parent.width() - button.width()) // 2

    if y == "center":
        y = (parent.height() - button.height()) // 2

    button.move(x, y)

    # Drop shadow effect
    shadow = QGraphicsDropShadowEffect(parent)
    shadow.setOffset(2, 2)
    shadow.setBlurRadius(10)
    shadow.setColor(QColor(0, 0, 0))  # Black shadow
    button.setGraphicsEffect(shadow)

    return button
