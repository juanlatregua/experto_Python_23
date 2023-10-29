import sys
import functools
import random

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton

def say_hi(name):
    hello_label.setText(f'Hello... {name} {random.randint(0,100)}')

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Hello World')
window.setGeometry(0, 0, 250, 100)
window.move(200, 200)

layout = QVBoxLayout()
window.setLayout(layout)

hello_label = QLabel('')
layout.addWidget(hello_label)

button = QPushButton('Hello')
button.clicked.connect(functools.partial(say_hi, "Pepe"))
layout.addWidget(button)

window.show()

sys.exit(app.exec())
