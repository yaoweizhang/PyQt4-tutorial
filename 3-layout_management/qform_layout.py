import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    label1 = QLabel("Name")
    nm = QLineEdit()

    label2 = QLabel("Address")
    add1 = QLineEdit()
    add2 = QLineEdit()

    vbox = QVBoxLayout()
    vbox.addWidget(add1)
    vbox.addWidget(add2)

    fbox = QFormLayout()
    fbox.addRow(label1, nm)
    fbox.addRow(label2, vbox)

    hbox = QHBoxLayout()

    r1 = QRadioButton("Male")
    r2 = QRadioButton("Female")

    hbox.addWidget(r1)
    hbox.addWidget(r2)
    hbox.addStretch()

    fbox.addRow(QLabel("sex"), hbox)
    fbox.addRow(QPushButton("Submit"), QPushButton("Cancel"))

    win.setLayout(fbox)
    win.setWindowTitle("PyQttt")
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
