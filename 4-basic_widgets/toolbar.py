"""
A QToolBar widget is a movable panel consisting of text buttons, buttons with
icons or other widgets.
"""
import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class tooldemo(QMainWindow):
    def __init__(self, parent=None):
        super(tooldemo, self).__init__(parent)
        layout = QVBoxLayout()

        tb = self.addToolBar("File")
        root_path = os.path.abspath(os.path.join(__file__, "..", ".."))
        jpg_path = os.path.join(root_path, "data", "huaji.jpg")

        b_new = QAction(QIcon(jpg_path), "new", self)
        tb.addAction(b_new)

        b_open = QAction(QIcon(jpg_path), "open", self)
        tb.addAction(b_open)

        b_save = QAction(QIcon(jpg_path), "save", self)
        tb.addAction(b_save)

        tb.actionTriggered[QAction].connect(self.toolbtnpressed)
        self.setLayout(layout)
        self.setWindowTitle("toolbar demo")

    def toolbtnpressed(self, a):
        print("pressed tool button is ", a.text())

def main():
    app = QApplication(sys.argv)
    ex = tooldemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
