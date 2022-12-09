import sys
import socket
import threading
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QLabel, QLineEdit, QComboBox, QPushButton, QGridLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont


class fonction(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.conn = socket.socket()
        self.__lab = QLabel("message")
        self.__text = QLineEdit("taper votre message ici")
        self.__rep = QLabel("")
        ok = QPushButton("envoyer ")
        quit = QPushButton("Déconnexion")
        self.fenetre = QTabWidget()
        self.fenetre.resize(600, 500)
        self.fenetre.setTabEnabled(1, False)
        self.fen1 = QWidget()
        self.fen2 = QWidget()
        self.fenetre.addTab(self.fen1, "serveur")
        self.fenetre.addTab(self.fen2, "client")

        grid.addWidget(self.__lab)
        grid.addWidget(self.__text)
        grid.addWidget(ok)
        grid.addWidget(self.__rep)

        grid.addWidget(quit)

        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)
        self.setWindowTitle("welcome")

    def __actionOk(self):
        self.__rep.setText(f"bonjour {self.__text.text()}")

    def __actionQuitter(self):
        QCoreApplication.exit(0)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QTabWidget()
        self.setCentralWidget(widget)

        self.layout = QVBoxLayout()

        widget.setLayout(self.layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

