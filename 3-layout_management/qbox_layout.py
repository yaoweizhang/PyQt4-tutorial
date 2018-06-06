import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    button1 = QPushButton("Button1")
    button2 = QPushButton("Button2")

    vbox = QVBoxLayout()
    vbox.addStretch()
    vbox.addWidget(button1)
    vbox.addStretch()
    vbox.addWidget(button2)
    vbox.addStretch()

    button3 = QPushButton("Button3")
    button4 = QPushButton("Button4")

    hbox = QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(button3)
    hbox.addStretch()
    hbox.addWidget(button4)
    hbox.addStretch()

    vbox.addStretch()
    vbox.addLayout(hbox)
    win.setLayout(vbox)
    win.setWindowTitle("PyQtttt")
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
