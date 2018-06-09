"""
QSlider class object presents the users with a groove over which a handle can
be moved. It is a classic widget to control a bounded value. Position of the handle
on the grovve is equivalent to an integer between the lower and the upper bounds of
the control.
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class sliderdemo(QWidget):
    def __init__(self, parent=None):
        super(sliderdemo, self).__init__(parent)

        layout = QVBoxLayout()

        self.l1 = QLabel("Try slide it!")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(10)
        self.s1.setMaximum(30)
        self.s1.setValue(20)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setTickInterval(5)
        self.s1.valueChanged.connect(self.valuechange)
        layout.addWidget(self.s1)

        self.setLayout(layout)
        self.setWindowTitle("SpinBox demo")

    def valuechange(self):
        size = self.s1.value()
        self.l1.setFont(QFont("Arial", size))
        self.l1.setText("Value: " + str(size))

def main():
    app = QApplication(sys.argv)
    ex = sliderdemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

