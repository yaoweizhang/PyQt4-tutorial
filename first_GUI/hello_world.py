"""
This script show how to build first gui.
"""
import sys
from PyQt4 import QtGui

def window():
    """main function"""
    app = QtGui.QApplication(sys.argv)
    win = QtGui.QWidget()
    win.setGeometry(200, 200, 200, 50)
    win.setWindowTitle("PyQtttt")

    label = QtGui.QLabel(win)
    label .setText("Hello World!!!")
    label .move(50, 20)

    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    window()
