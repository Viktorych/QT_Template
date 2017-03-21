import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTreeView
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSizePolicy


class VecParameter(QWidget):
    value_changed = pyqtSignal(object)

    def __init__(self, value, num_components, max_columns=4, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.components = []
        if num_components > max_columns:
            num_components = max_columns

        layout = QHBoxLayout(self)
        for i in range(num_components):
            c = QLineEdit(str(value[i]), self)
            c.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
            self.components.append(c)
            layout.addWidget(c, stretch=1)
            """
        for i in range(num_components, max_columns):
            lbl = QLabel('')
            lbl.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
            layout.addWidget(lbl, stretch=1)
"""
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)


class PropertiesWidget(QTreeView):

    def __init__(self, columns, *args, **kwargs):
        super(PropertiesWidget, self).__init__(*args, **kwargs)

        self.model = QStandardItemModel(self)
        self.setModel(self.model)
        self.model.setColumnCount(columns)
        self.model.setHeaderData(0, Qt.Horizontal, "Property")
        self.model.setHeaderData(1, Qt.Horizontal, "Value")
        self.setColumnWidth(0,200)
        self.setColumnWidth(1, 100)
        self.setFocusPolicy(Qt.NoFocus)
        self.last_item = 0
        self.last_item = QStandardItem()
        self.parameters = {}

    def begin_group(self, name, key):
        root = QStandardItem(name)
        root.setEditable(False)
        if not key:
            root.setData(key)
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

    def add_vec1(self, key, value=[0]):
        widget = VecParameter(value, 1, parent=self)
        self.append_row(key, widget)

    def add_vec2(self, key, value=[0]):
        widget = VecParameter(value, 2, parent=self)
        self.append_row(key, widget)

    def add_vec3(self, key, value=[0]):
        widget = VecParameter(value, 3, parent=self)
        self.append_row(key, widget)

    def add_vec4(self, key, value=[0, 0, 0, 0]):
        widget = VecParameter(value, 4, parent=self)
        self.append_row(key, widget)


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = PropertiesWidget(2)
    ex.begin_group("foo", "foo")
    ex.add_vec1("vec1vxcfvcxbvc fdsgfdgdfsg", [1])
    ex.add_vec1("vec2 fbsdsb dsfgdsf sdfg", [10])
    ex.add_vec1("vec3", [1, 2, 3])
    ex.add_vec1("vec4", [1, 2, 3, 4])
    ex.end_group()
    ex.begin_group("foo1", "foo2")
    ex.add_vec1("vec1", [1])
    ex.add_vec1("vec2", [10])
    ex.add_vec3("vec3", [1, 2, 3])
    ex.add_vec4("vec4", [1, 2, 3, 4])
    ex.end_group()

    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()