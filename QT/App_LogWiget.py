from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QWidget


class LogWiget(QWidget):
    value_changed = pyqtSignal(object)

    def __init__(self,  parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.textEdit = QTextEdit(self)

        self.textEdit.setStyleSheet("background: grey")
        self.textEdit.setText("<b style='color:#ffFF00'>Cтарт приложения</span></b>")
        self.textEdit.append("<b style='color:#ff0000'>Другой текст</span></b>")
        vbox = QHBoxLayout()

        vbox.addWidget(self.textEdit)

        self.setLayout(vbox)
    def add(self, txt):
        self.textEdit.append("<b style='color:#ffffff'>{}</span></b>".format(txt))
