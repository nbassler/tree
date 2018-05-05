import sys
import logging

from PyQt5 import QtWidgets

from view import MyView
from model import MyModel
from controller import TreeCtrl


logger = logging.getLogger(__name__)


def main(args):
    app = QtWidgets.QApplication(sys.argv)

    v = MyView()
    v.show()
    m = MyModel()
    TreeCtrl(m, v)

    app.exec_()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main(sys.argv[1:]))
