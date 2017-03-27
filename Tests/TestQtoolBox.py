import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QToolBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # tool box
        tool_box = QToolBox()

        # items
        tool_box.addItem(QPlainTextEdit('Text 1'),
                         'Page 1')
        tool_box.addItem(QPlainTextEdit('Text 2'),
                         'Page 2')

        # vertical box layout
        vlayout = QVBoxLayout()
        vlayout.addWidget(tool_box)
        self.setLayout(vlayout)


application = QApplication(sys.argv)

# window
window = Window()
window.setWindowTitle('Tool Box')
window.resize(280, 300)
window.show()

sys.exit(application.exec_())
