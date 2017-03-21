from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QSpacerItem

from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtWidgets import QVBoxLayout


class Splash(QSplashScreen):
    def __init__(self, *arg, **args):
        QSplashScreen.__init__(self, *arg, **args)
        self.setCursor(Qt.BusyCursor)
        self.setPixmap(QPixmap("images/titan1.jpg"))
        loaut = QVBoxLayout(self)
        loaut.addItem(QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.progress = QProgressBar(self)
        self.progress.setValue(0)
        self.progress.setMaximum(100)
        loaut.addWidget(self.progress)
        self.showMessage(u"Пример заставки", Qt.AlignTop)
        self.startTimer(5)
    def timerEvent(self, event):
        self.progress.setValue(self.progress.value() + 1)
        event.accept()