from PyQt5.QtWidgets import (QApplication, QMainWindow)


class View(QMainWindow):
    def __init__(self):
        super().__init__()
        self.createMainUI()

    def createMainUI(self):
        self.setGeometry(400, 200, 500, 300)
        self.setWindowTitle("test")

