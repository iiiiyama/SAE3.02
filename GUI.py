import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()

        widget.setLayout(grid)

treff