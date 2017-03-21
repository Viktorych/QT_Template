
from PyQt5.QtWidgets import QApplication
from time import time, sleep



from QT import App_MainWindow, App_Splash


from App import App_Variable


Variable = App_Variable.Variable()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    #print (QStyleFactory.keys())
    # qApp.setStyle(QStyleFactory.create("Fusion"))
    #
    # dark_palette = App_dark_palette.dark_palette()
    # qApp.setPalette(dark_palette)
    # qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    app.setStyle("Fusion")
    start = time()
    splash = App_Splash.Splash()
    splash.show()
    while time() - start < 1:
        sleep(0.001)
        app.processEvents()
    window = App_MainWindow.MainWindow(Variable)

    window.show()
    splash.finish(window)
    sys.exit(app.exec_())