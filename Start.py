from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, qApp
from time import time, sleep

from PyQt5.QtWidgets import QStyleFactory

from QT import App_MainWindow,App_Splash,App_dark_palette


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    #print (QStyleFactory.keys())
    qApp.setStyle(QStyleFactory.create("Fusion"))
    dark_palette = App_dark_palette.dark_palette()
    qApp.setPalette(dark_palette)
    qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    #app.setStyle("Fusion")
    start = time()
    splash = App_Splash.Splash()
    splash.show()
    while time() - start < 1:
        sleep(0.001)
        app.processEvents()
    window = App_MainWindow.MainWindow()

    window.show()
    splash.finish(window)
    sys.exit(app.exec_())