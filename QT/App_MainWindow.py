from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox
from App import App_Variable
from QT import App_CentralWG

class MainWindow(QMainWindow):
    """Главное окно приложения"""
    def __init__(self, Variable):
        super().__init__()
        self.setAction()
        self.setMenuBar()
        self.setToolBar()
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('QT Программа')
        self.statusBar().showMessage('Готово')
        self.setWindowIcon(QIcon('Images/app_icon.png'))  # App Icon

        self.Variable = Variable
        #print (self.Variable.)
        self.CentralWG=App_CentralWG.CWG(self.Variable)
        self.setCentralWidget(self.CentralWG)







    def setAction(self):
        self.exitAction = QAction(QIcon('Images/Exit.png'), 'Выход', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Выход из приложения')
        self.exitAction.triggered.connect(qApp.quit)

        self.aboutAction = QAction(QIcon('Images/About.png'), 'О программе', self)
        #self.aboutexitAction.setShortcut('Ctrl+Q')
        self.aboutAction.setStatusTip('О программе')
        self.aboutAction.triggered.connect(self.about)

        self.helpAction = QAction(QIcon('Images/Help.png'), 'Помощь', self)
        # self.helpAction.setShortcut('Ctrl+Q')
        self.helpAction.setStatusTip('Помощь')
        # self.helpAction.triggered.connect(qApp.quit)

        self.newFileAction = QAction(QIcon('Images/new.png'), 'Новый', self)
        # self.newFileAction.setShortcut('Ctrl+Q')
        self.newFileAction.setStatusTip('Новый файл')
        # self.newFileAction.triggered.connect(qApp.quit)

        self.openFileAction = QAction(QIcon('Images/Open.png'), 'Открыть', self)
        # self.openFileAction.setShortcut('Ctrl+Q')
        self.openFileAction.setStatusTip('Открыть файл')
        # self.openFileAction.triggered.connect(qApp.quit)
        self.saveFileAction = QAction(QIcon('Images/Save.png'), 'Сохранить', self)
        # self.saveFileAction.setShortcut('Ctrl+Q')
        self.saveFileAction.setStatusTip('Сохранить в файл')
        # self.saveFileAction.triggered.connect(qApp.quit)

        self.settingAction = QAction(QIcon('Images/setting.png'), 'Насторойки', self)
        # self.settingAction.setShortcut('Ctrl+Q')
        self.settingAction.setStatusTip('Насторойки программы')
        # self.settingAction.triggered.connect(qApp.quit)

        self.printAction = QAction(QIcon('Images/print.png'), 'Печать', self)
        # self.printAction.setShortcut('Ctrl+Q')
        self.printAction.setStatusTip('Печать')
        # self.printAction.triggered.connect(qApp.quit)

    def setMenuBar(self):
        """определение Меню бара"""
        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('Файл')
        viewMenu = self.menubar.addMenu('Вид')
        settingMenu = self.menubar.addMenu('Настройка')
        helpMenu = self.menubar.addMenu('Помощь')
        """Меню Файл"""
        fileMenu.addAction(self.newFileAction)
        fileMenu.addAction(self.openFileAction)
        fileMenu.addAction(self.saveFileAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.printAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.settingAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        """Меню Помощь"""
        helpMenu.addAction(self.helpAction)
        fileMenu.addSeparator()
        helpMenu.addAction(self.aboutAction)

    def setToolBar(self):
        """Определение тулбара"""
        self.toolbar = self.addToolBar('Файл')
        #self.toolbar = self.addToolBar('Setting')
        self.toolbar.addAction(self.openFileAction)
        self.toolbar.addAction(self.saveFileAction)
        self.toolbar.addAction(self.settingAction)
        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.exitAction)

    def about(self):
        # QMessageBox.about (QWidget parent, QString caption, QString text)
        QMessageBox.about(self, 'О программе',
                          '''О программе.<br />
                              This accepts HTML formatting <b> bold</b>''')
