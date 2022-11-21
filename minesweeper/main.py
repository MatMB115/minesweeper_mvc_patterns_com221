import sys

from PyQt5.QtWidgets import QApplication

from view import View
from controller import Controller, ControllerObserver
from model import Model, Historic

if __name__ == '__main__':
    game = QApplication(sys.argv)

    model = Model()
    historic = Historic()
    controller = Controller(model)
    controllerHist = ControllerObserver(historic)
    window = View(controller, controllerHist)

    window.show()
    sys.exit(game.exec_())
