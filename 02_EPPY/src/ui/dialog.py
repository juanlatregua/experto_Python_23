import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QDialogButtonBox
from PyQt6.QtWidgets import QFormLayout
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QVBoxLayout

class Dialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Dialog')
        dlg_layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow('Name:', QLineEdit())
        form_layout.addRow('Age:', QLineEdit())
        form_layout.addRow('Job:', QLineEdit())
        form_layout.addRow('Hobbies:', QLineEdit())
        dlg_layout.addLayout(form_layout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        dlg_layout.addWidget(buttons)
        self.setLayout(dlg_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec())