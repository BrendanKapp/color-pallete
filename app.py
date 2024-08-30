#!/usr/bin/env python3

"""
@Author: Brendan Kapp
@Date: 30 August 2024
@License: MIT License
@Description:
The following is a simple QT5 GUI that will display a color pallete of hex codes.
When a color in the pallete is clicked, the hex value will be copied to the users clipboard.
It is recommended to dock the color pallete at the top of the window list for maximum usability.
"""

import sys
import logging
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QColor, QClipboard
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect, pyqtProperty, QTimer

logger = logging.getLogger(__name__)

class ColorSquare(QWidget):
    def __init__(self, color, clipboard):
        super().__init__()
        self.color = color
        self.clipboard = clipboard
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(32, 32)
        self.setStyleSheet(f"background-color: {self.color};")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setCursor(Qt.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clipboard.setText(self.color)

            # Start animation
            self.setStyleSheet("background-color: white;")
            QTimer.singleShot(150, self.reset_color) 

    def reset_color(self):
        self.setStyleSheet(f"background-color: {self.color};")

class ColorSquaresApp(QWidget):
    def __init__(self, colors):
        super().__init__()
        self.clipboard = QApplication.clipboard()
        self.init_ui(colors)

    def init_ui(self, colors):
        layout = QHBoxLayout()
        for color in colors:
            square = ColorSquare(color, self.clipboard)
            layout.addWidget(square)
        self.setLayout(layout)
        self.setWindowTitle('Color Squares')
        self.show()

def import_pallete(filename):
    try:
        file = open(filename)
        colors = list()
        for line in file:
            colors.append(line.strip())
        file.close()
        return colors
    except Exception as e:
        logger.error("Error loading pallete: " + filename)
        logger.error(e)
        exit()

def import_config():
    try:
        file = open("app.config")
        config = dict()
        for line in file:
            setting, value = line.split("=")
            config[setting] = value
        file.close()
        # config cleanup
        config["pallete"] = config["pallete"].replace(".md", "")
        return config
    except Exception as e:
        logger.error("Error loading app.config")
        logger.error(e)
        exit()

def main():
    logging.basicConfig(filename='pallete.log', level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

    app = QApplication(sys.argv)

    config = import_config()
    
    colors = import_pallete("palletes/" + config["pallete"] + ".md")
    
    window = ColorSquaresApp(colors)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
