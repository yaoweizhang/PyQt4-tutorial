"""
A horizontal QMenuBar just below the title bar of QMainWindow object is reserved
for dsiplaying QMenu objects.
QMenu class provides a widget which can be added to menu bar. It is also used to
create context menu and popup menu. Each QMenu object may contain one or more
QAction objects or cascaded QMenu objects.
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class menudemo(QMainWindow):
    def __init__(self, parent=None):
        super(menudemo, self).__init__(parent)

        layout = QHBoxLayout()

        bar = self.menuBar()
        b_file = bar.addMenu("file")

        b_save = QAction("Save", self)
        b_save.setShortcut("Ctrl+S")
        b_file.addAction(b_save)

        edit = b_file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

        quit = QAction("Quit", self)
        b_file.addAction(quit)
        b_file.triggered[QAction].connect(self.processtrigger)
        self.setLayout(layout)
        self.setWindowTitle("menu demo")

    def processtrigger(self, q):
        print(q.text() + " is triggered")

def main():
    app = QApplication(sys.argv)
    ex = menudemo()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
