import sys

from PyQt6.QtWidgets import QApplication

from model import Model
from view import View
from controller import Controller

def main():
    calc = QApplication(sys.argv)

    view = View()
    view.show()

    model = Model()

    controller = Controller(view, model)

    sys.exit(calc.exec())

if __name__ == '__main__':
    main()