"""
QLineEdit object is the most commonly used input field. It provides a box in which
one line of text can be entered. In order to enter multi-line text,
QTextEdit object is required.
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    e1 = QLineEdit()
    e1.setValidator(QIntValidator())
    e1.setMaxLength(4)
    e1.setAlignment(Qt.AlignRight)
    e1.setFont(QFont("Arial", 20))

    e2 = QLineEdit()
    e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

    e3 = QLineEdit()
    e3.setInputMask("+999_999_9999")

    e4 = QLineEdit()
    e4.textChanged.connect(textchanged)

    e5 = QLineEdit()
    e5.setEchoMode(QLineEdit.Password)
    e5.editingFinished.connect(enterPress)

    e6 = QLineEdit("hello python")
    e6.setReadOnly(True)

    flo = QFormLayout()
    flo.addRow("integer validator", e1)
    flo.addRow("double validator", e2)
    flo.addRow("input Mask", e3)
    flo.addRow("Text changed", e4)
    flo.addRow("Password", e5)
    flo.addRow("Read only", e6)

    win.setLayout(flo)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())

def textchanged(text):
    print("contents of text box: " + text)

def enterPress():
    print("edited")

if __name__ == "__main__":
    window()
