"""
A QSpinBox object presents the user with a textbox which displays an integer with up/down
button on its right. The value in the textbox increases/decreases if the up/down button
is pressed. By default, the integer number in the box starts with 0, goes upto 99 and
changes by step 1.
Use ADoubleSpinBox for float values.
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class spindemo(QWidget):
    def __init__(self, parent=None):
        super(spindemo, self).__init__(parent)

        layout = QVBoxLayout()

        self.l1 = QLabel("current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.sp = QSpinBox()
        self.sp.valueChanged.connect(self.valuechange)
        layout.addWidget(self.sp)

        self.setLayout(layout)
        self.setWindowTitle("SpinBox demo")

    def valuechange(self):
        self.l1.setText("Current value: " + str(self.sp.value()))

def main():
    app = QApplication(sys.argv)
    ex = spindemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
