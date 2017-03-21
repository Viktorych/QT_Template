
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSizePolicy
from App.App_Variable import Variable



class Parameter(QWidget):
    value_changed = pyqtSignal(object)

    def __init__(self, value, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #self.components = []


        layout = QHBoxLayout(self)
        #for i in range(num_components):
        self.c = QLineEdit(str(value), self)
        #c.textChanged.connect(self.doEdit)

        self.c.setValidator(QDoubleValidator(0.99, 99.99, 2))
        self.c.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        #self.components.append(c)
        layout.addWidget(self.c, stretch=1)
        """
        for i in range(num_components, max_columns):
            lbl = QLabel('')
            lbl.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
            layout.addWidget(lbl, stretch=1)
        """
        layout.setContentsMargins(0, 0, 0, 0)
        self.c.editingFinished.connect(self._doEdit)
        self.setLayout(layout)
    def _doEdit(self):
        print ("Эдит")

class PropertiesWidget(QTreeView):

    def __init__(self, columns, Variable, *args, **kwargs):
        super(PropertiesWidget, self).__init__(*args, **kwargs)

        self.model = QStandardItemModel(self)
        self.setModel(self.model)
        self.model.setColumnCount(columns)
        self.model.setHeaderData(0, Qt.Horizontal, "Пременная")
        self.model.setHeaderData(1, Qt.Horizontal, "Значение")
        self.setColumnWidth(0,200)
        self.setColumnWidth(1, 100)
        self.setFocusPolicy(Qt.NoFocus)
        self.last_item = 0
        self.last_item = QStandardItem()
        self.parameters = {}
        self.Variable=Variable

        #print (self.Variable.A["Группа 1"])
        #self.begin_group(self.Variable.A["Группа 1"], "Группа 1")
        self.begin_group(self.Variable.A[0])
        for k, v in self.Variable.A.items():
            if k!=0:
                self.add_Parameter(k, v)
        self.end_group()
        self.begin_group(self.Variable.B[0])
        for k, v in self.Variable.B.items():
            if k != 0:
                self.add_Parameter(k, v)
        self.end_group()
        #self.begin_group(self.Variable.A["Группа 1"], "Группа 1")

            #self.add_Parameter("Переменная B", 10)

    def begin_group(self, name):
        root = QStandardItem(name)
        root.setEditable(False)

        self.model.appendRow([root])
        self.last_item = root

    def end_group(self):
        if (self.last_item and self.last_item.parent()):
            self.last_item = self.last_item.parent()

    def append_row(self, text, widget):
        if not self.last_item:
            return

        if text in self.parameters:
            raise Exception("Not allowed duplicate keys {0}".format(text))

        item = self.last_item
        child = QStandardItem(text)
        child2 = QStandardItem()
        child.setEditable(False)
        item.appendRow([child, child2])
        if widget:
            self.setIndexWidget(child2.index(), widget)

        self.expand(child.index().parent())

    def add_Parameter(self, key, value=0):
        widget = Parameter(value,  parent=self)
        self.append_row(key, widget)

