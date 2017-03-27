
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLineEdit,QLabel
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSizePolicy
from App.App_Variable import Variables



from  App import App_Variable

class Parameter(QWidget):
    value_changed = pyqtSignal(object)
    #prop=App_Variable.Property()
    #prop.Ed_izm
    def __init__(self,Property, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #self.components = []
        self.prop=Property
        #self.prop.

        layout = QHBoxLayout(self)
        #for i in range(num_components):
        self.c = QLineEdit(str(self.prop.Value), self)
        #c.textChanged.connect(self.doEdit)
        self.ed_izm=QLabel(self.prop.Ed_izm)
        validator=QDoubleValidator(0.99, 99.99, 2)
        validator.setNotation(QDoubleValidator.StandardNotation)
        self.c.setValidator(validator)
        self.c.setAlignment(Qt.AlignRight)
        self.c.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        #self.components.append(c)
        self.c.setMaximumWidth(100)
        layout.addWidget(self.c, stretch=1)
        layout.addWidget(self.ed_izm)
        """
        for i in range(num_components, max_columns):
            lbl = QLabel('')
            lbl.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
            layout.addWidget(lbl, stretch=1)
        """
        layout.setContentsMargins(0, 0, 20, 0)
        self.c.editingFinished.connect(self._doEdit)
        self.setLayout(layout)
    def _doEdit(self):
        self.prop.Value=self.c.text()
        print (self.prop)
        #pass
        #print ("Эдит")

class PropertiesWidget(QTreeView):

    def __init__(self, columns, Variables, *args, **kwargs):
        super(PropertiesWidget, self).__init__(*args, **kwargs)
        self.setMaximumWidth(400)

        self.Variables=Variables
        self.reload()
        #self.begin_group("test")

        #self.end_group()

        #print (self.Variable.A["Группа 1"])
        #self.begin_group(self.Variable.A["Группа 1"], "Группа 1")

        # self.begin_group(self.Variable.A[0])
        # for k, v in self.Variable.A.items():
        #     if k!=0:
        #         self.add_Parameter(k, v)
        # self.end_group()
        # self.begin_group(self.Variable.B[0])
        # for k, v in self.Variable.B.items():
        #     if k != 0:
        #         self.add_Parameter(k, v)
        # self.end_group()
        # #self.begin_group(self.Variable.A["Группа 1"], "Группа 1")
        #
        #     #self.add_Parameter("Переменная B", 10)

    def reload(self):
        self.model = QStandardItemModel(self)
        self.setModel(self.model)
        self.model.setColumnCount(2)
        self.model.setHeaderData(0, Qt.Horizontal, "Пременная")
        self.model.setHeaderData(1, Qt.Horizontal, "Значение")
        self.setColumnWidth(0, 250)
        self.setColumnWidth(1, 100)
        self.setFocusPolicy(Qt.NoFocus)
        self.last_item = 0
        self.last_item = QStandardItem()
        self.parameters = {}
        #print (self.Variables)
        s = 0
        for p in self.Variables.List:
            if p.Type == 0:
                if s != 0:
                    self.end_group()
                self.begin_group(p.Name)
            elif p.Type == 1:
                self.add_Parameter(p)
            s = 1
        self.end_group()



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

    def add_Parameter(self, param):
        widget = Parameter(param,  parent=self)
        self.append_row(param.Name, widget)

