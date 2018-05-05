import logging

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtWidgets import QMenu

logger = logging.getLogger(__name__)


class TreeCtrl(object):

    def __init__(self, model, view):

        self.model = model
        self.view = view

        tw = view.tw

        tw.setHeaderLabels(['MyTest'])

        tctx = QTreeWidgetItem(["CTX"])
        tvdx = QTreeWidgetItem(["ROIs"])
        tdos = QTreeWidgetItem(["DOSs"])
        tlet = QTreeWidgetItem(["LETs"])

        tctx.addChild(QTreeWidgetItem([model.ctx]))

        for item in model.vdx:
            tvdx.addChild(QTreeWidgetItem([item]))

        for item in model.dos:
            tdos.addChild(QTreeWidgetItem([item]))

        for item in model.let:
            tlet.addChild(QTreeWidgetItem([item]))

        tw.addTopLevelItem(tctx)
        tw.addTopLevelItem(tvdx)
        tw.addTopLevelItem(tdos)
        tw.addTopLevelItem(tlet)

        tctx.setExpanded(True)  # should be set, after it was added to the TreeWidget
        tvdx.setExpanded(True)
        tdos.setExpanded(True)
        tlet.setExpanded(True)

        self.setup_callbacks(view)

        self.tvdx = tvdx
        self.popup_menu = self.create_popup_menu()

    def create_popup_menu(self):
        popup_menu = QMenu(self.view.tw)
        popup_menu.addAction("New", self.menu_open)
        popup_menu.addAction("Rename", self.menu_open)
        popup_menu.addSeparator()
        popup_menu.addAction("Delete", self.menu_open)
        return popup_menu

    def setup_callbacks(self, view):
        tw = view.tw

        logger.debug("setup_callbacks()")
        view.btn.clicked.connect(lambda: self.add_data())
        # view.btn.clicked.connect(self.odd_doto)
        tw.setContextMenuPolicy(Qt.CustomContextMenu)
        tw.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        logger.debug("on_context_menu() {}".format(pos))
        tw = self.view.tw
        logger.debug("menu_context() {}".format(pos))
        node = tw.mapToGlobal(pos)
        action = self.popup_menu.exec_(tw.mapToGlobal(pos))
        logger.debug("action: {}".format(action.text()))
        # print(dir(action))

    def menu_open(self):
        logger.debug("menu_open()")

    def add_data(self):
        logger.debug("add_data()")
        self.model.vdx.append("Smerg")
        self.tvdx.addChild(QTreeWidgetItem(["Smerg"]))

    def update_tree():
        pass
