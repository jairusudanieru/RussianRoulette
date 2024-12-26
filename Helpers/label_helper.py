from PyQt5.QtWidgets import QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QFontDatabase
from PyQt5.QtCore import Qt

def create_label(parent, text, font_size, x, y, color):
    """
    Create a label with custom styling, shadow, and positioning.
    """
    # Load custom font
    font_id = QFontDatabase.addApplicationFont(r"Fonts/creepster.ttf")
    if font_id == -1:
        print("Failed to load font!")

    label = QLabel(text, parent)
    label.setStyleSheet(f"""
        QLabel {{
            color: {color};  /* Dark red */
            font-size: {font_size}px;
            font-weight: bold;
            font-family: 'Creepster';
            background: transparent;
        }}
    """)
    label.adjustSize()
    label.setAlignment(Qt.AlignCenter)

    if x == "center":
        x = (parent.width() - label.width()) // 2

    if y == "center":
        y = (parent.height() - label.height()) // 2

    label.move(x, y)

    # Drop shadow effect
    shadow = QGraphicsDropShadowEffect(parent)
    shadow.setOffset(2, 2)
    shadow.setBlurRadius(10)
    shadow.setColor(QColor(0, 0, 0))  # Semi-transparent shadow
    label.setGraphicsEffect(shadow)

    return label
