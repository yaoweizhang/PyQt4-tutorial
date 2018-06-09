"""
A QRadioButton class object presents a selectable button with a text label.
The user can select one of many options presented on the form.
This class is derived from QAbstractButton class.
Radio buttons are autoexclusive by default. Hence, only one of the radio buttons
in the parent window can be selected at a time.
If one is selected, previously selected button is automatically deselected.
Radio buttons can also be put in a QGroupBox or QButtonGroup to create more than
one selectable fields on the parent window.
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Radiodemo(QWidget):
    def __init__(self, parent=None):
        super(Radiodemo, self).__init__(parent)

        layout = QHBoxLayout()

        self.b1 = QRadioButton("Button1")
        self.b1.setChecked(True)
        self.b1.toggled.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QRadioButton("Button2")
        self.b2.toggled.connect(lambda:self.btnstate(self.b2))
        layout.addWidget(self.b2)

        vlayout = QVBoxLayout()
        vlayout.addLayout(layout)

        self.b3 = QRadioButton("Button3")
        self.b3.toggled.connect(lambda:self.btnstate(self.b3))
        vlayout.addWidget(self.b3)

        self.b4 = QRadioButton("Button4")
        self.b4.toggled.connect(lambda:self.btnstate(self.b4))
        vlayout.addWidget(self.b4)

        self.setLayout(vlayout)
        self.setWindowTitle("RadioButton demo")

    def btnstate(self, b):
        if b.isChecked() == True:
            print(b.text() + " is selected")
        else:
            print(b.text() + " is deselected")

def main():
    app = QApplication(sys.argv)
    ex = Radiodemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
