"""
A rectangular box before the text label appears when a QCheckBox ojbect is added to the
parent window.
"""
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class checkdemo(QWidget):
    def __init__(self, parent=None):
        super(checkdemo, self).__init__(parent)

        layout = QHBoxLayout()

        self.b1 = QCheckBox("Button1")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QCheckBox("Button2")
        self.b2.toggled.connect(lambda:self.btnstate(self.b2))
        layout.addWidget(self.b2)

        self.setLayout(layout)
        self.setWindowTitle("checkbox demo")

    def btnstate(self, b):
        print(b.text() + " is " + ("selected" if b.isChecked() else "deselected"))

def main():
    app = QApplication(sys.argv)
    ex = checkdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
