import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, qApp
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStyleFactory
from PyQt5.QtWidgets import QWidget


class AppWidget(QWidget):
    def __init__(self, parent=None):
        super(AppWidget, self).__init__(parent)
        horizontalLayout = QHBoxLayout()
        self.styleLabel = QLabel("Set Style:")
        self.styleComboBox = QComboBox()
        # add styles from QStyleFactory
        self.styleComboBox.addItems(QStyleFactory.keys())
        # find current style
        index = self.styleComboBox.findText(
                    qApp.style().objectName(),
                    QtCore.Qt.MatchFixedString)
        # set current style
        self.styleComboBox.setCurrentIndex(index)
        # set style change handler
        self.styleComboBox.activated[str].connect(self.handleStyleChanged)
        horizontalLayout.addWidget(self.styleLabel)
        horizontalLayout.addWidget(self.styleComboBox)
        self.setLayout(horizontalLayout)

    # handler for changing style
    def handleStyleChanged(self, style):
        qApp.setStyle(style)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    widgetApp = AppWidget()
    widgetApp.show()
    sys.exit(app.exec_())