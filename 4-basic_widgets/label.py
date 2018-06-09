"""
QLabel object acts as a placeholder to display non-editable text or image, or a movie
of animated GIF. It can also be used as a mnemonic key for other widgets.
Plain text, hyperlink or rich text can be displaed on the label.
Methods of QLabel class:
    setAlignment(): Qt.AlignLeft, Qt.AlignRight, Qt.AlignCenter, Qt.AlignJustify
    setIndent(): Sets the labes text indent
    setPixmap(): Displays an image
    Text(): Displays the caption of the label
    setText(): Programmatically sets the cpation
    selectedText(): Display the slected text from the label
    setBuddy(): Associates the label with an input widget
    setWordWrap(): Enables or disables wrapping text in the label
Signals of QLabel class:
    linkActivated: Works when clicked
    linkHovered: Works when hovered
"""

import sys
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()

    l1 = QLabel()
    l2 = QLabel()
    l3 = QLabel()
    l4 = QLabel()

    l1.setText("Hello world")
    l2.setText("Welcome to Python GUI Programming")
    parent_path = os.path.abspath(os.path.join(__file__, "..", ".."))
    jpg_path = os.path.join(parent_path, "data", "huaji.jpg")
    print(jpg_path)
    l3.setPixmap(QPixmap(jpg_path))
    l4.setText("TutorialsPoint")

    l1.setAlignment(Qt.AlignCenter)
    l3.setAlignment(Qt.AlignCenter)
    l4.setAlignment(Qt.AlignRight)

    vbox = QVBoxLayout()
    vbox.addWidget(l1)
    vbox.addStretch()
    vbox.addWidget(l2)
    vbox.addStretch()
    vbox.addWidget(l3)
    vbox.addStretch()
    vbox.addWidget(l4)

    l1.setOpenExternalLinks(True)
    l1.setTextInteractionFlags(Qt.TextSelectableByMouse)
    l2.linkHovered.connect(clicked)
    l4.linkActivated.connect(hovered)

    win.setLayout(vbox)
    win.setWindowTitle("QLabel Demo")
    win.show()
    sys.exit(app.exec_())

def clicked():
    print("clicked")

def hovered():
    print("hovering")

if __name__ == "__main__":
    window()

