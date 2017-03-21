from PyQt5 import QtCore

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from App.App_Variable import Variable
from QT import App_PropertiesWidget
class CWG(QWidget):
    """Центральный вигет"""

    def __init__(self,Variable, parent=None):
        super().__init__(parent)
        self.Variable = Variable
        print (self.Variable.A)
        self.treeview  = App_PropertiesWidget.PropertiesWidget(2,self.Variable)
        self.treeview.setHeaderHidden(True)

        #for i in range(1, 2):
            #self.treeview.setColumnWidth(i, 200)
        #self.treeview.setHeader(QHeaderView())
        #self.treeview.itemModel.setHeaderData(0, QtCore.Qt.Horizontal, 'Column {}'.format("0"))
        # """
        # e2 = QLineEdit()
        # e2.setText("10")
        # e2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        # """
        # model = QStandardItemModel()
        # rootNode = model.invisibleRootItem()
        # branch1 = QStandardItem("Группа переменных 1")
        # branch1.appendRow([QStandardItem("Переменная A"), None])
        # childnode = QStandardItem("Переменная B")
        # branch1.appendRow([childnode, None])
        #
        # branch2 = QStandardItem("Группа переменных 2")
        # branch2.appendRow([QStandardItem("Переменная C"), None])
        # branch2.appendRow([QStandardItem("Переменная D"), None])
        # branch2.appendRow([QStandardItem("Переменная E"), None])
        # branch2.appendRow([QStandardItem("Переменная F"), None])
        # branch2.appendRow([QStandardItem("Переменная J"), None])
        #
        # rootNode.appendRow([branch1, None])
        # rootNode.appendRow([branch2, None])

        #self.treeview.setModel(model)
        #self.treeview.setColumnWidth(0, 150)
        #self.treeview.expandAll()




        #self.addWidget(self.treeview)
        table = QtWidgets.QTableWidget()
        tableItem = QtWidgets.QTableWidgetItem()

        table.setWindowTitle("Set QWidget for Entire QTableWidget Column")
        table.resize(400, 250)
        table.setRowCount(4)
        table.setColumnCount(4)

        table.setHorizontalHeaderLabels(["Столбец 1", "Столбец 3", "Столбец 2", "Столбец 4"])
        table.setVerticalHeaderLabels(["Строка 1", "Строка 3", "Строка 2", "Строка 4"])
        table.setItem(0, 0, QtWidgets.QTableWidgetItem("ITEM 1_1"))
        table.setItem(0, 1, QtWidgets.QTableWidgetItem("ITEM 1_2"))

        table.setItem(1, 0, QtWidgets.QTableWidgetItem("ITEM 2_1"))
        table.setItem(1, 1, QtWidgets.QTableWidgetItem("ITEM 2_2"))

        table.setItem(2, 0, QtWidgets.QTableWidgetItem("ITEM 3_1"))
        table.setItem(2, 1, QtWidgets.QTableWidgetItem("ITEM 3_2"))

        table.setItem(3, 0, QtWidgets.QTableWidgetItem("ITEM 4_1"))
        table.setItem(3, 1, QtWidgets.QTableWidgetItem("ITEM 4_2"))

        # Add Widget to the rightmost Element of First Row
        #table.setItem(0, 2, tableItem)

        # Add QPushButton to the rightmost QTableWidgetItem on first row
        #table.setCellWidget(0, 2, QtWidgets.QPushButton("Cell Widget"));



        self.treeview.setAlternatingRowColors(True)
        vbox = QHBoxLayout()
        #vbox.addStretch(1)
        vbox.addWidget(self.treeview)
        vbox.addWidget(table)
        self.setLayout(vbox)
