import logging

from PyQt5 import QtWidgets
# from PyQt5 import QtGui

logger = logging.getLogger(__name__)


class MyView(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        vbox = QtWidgets.QVBoxLayout(self)

        btn = QtWidgets.QPushButton('Add Data', self)
        tw = QtWidgets.QTreeWidget()

        vbox.addWidget(tw)
        vbox.addWidget(btn)
        self.setLayout(vbox)

        self.setWindowTitle('TreeWidget')
        self.resize(300, 500)

        self.tw = tw
        self.btn = btn
