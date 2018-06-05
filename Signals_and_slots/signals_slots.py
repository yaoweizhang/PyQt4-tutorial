"""This script shows how to connect button signal and slots function"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
    """main function"""
    app = QApplication(sys.argv)
    win = QDialog()

    button1 = QPushButton(win)
    button1.setText("Button1")
    button1.move(50, 20)
    button1.clicked.connect(b1_clicked)

    button2 = QPushButton(win)
    button2.setText("Button2")
    button2.move(50, 50)
    QObject.connect(button2, SIGNAL("clicked()"), b2_clicked)

    win.setGeometry(400, 400, 200, 100)
    win.setWindowTitle("PyQtttt")
    win.show()

    sys.exit(app.exec_())

def b1_clicked():
    """button 1 slot function"""
    print("Button 1 clicked")

def b2_clicked():
    """button 2 slot function"""
    print("Button 2 clicked")

if __name__ == "__main__":
    window()
