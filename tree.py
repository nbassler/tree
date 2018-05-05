import sys
import logging

from PyQt5 import QtWidgets

logger = logging.getLogger(__name__)


class Example(QtWidgets.QWidget):

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
        self.show()


def main(args):
    app = QtWidgets.QApplication(sys.argv)

    ex = Example()
    ex.show()

    app.exec_()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main(sys.argv[1:]))
