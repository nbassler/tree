import logging

# from PyQt5 import QtGui
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

        tctx.setCheckState(0, Qt.Checked)

        # tctx.addChild(QTreeWidgetItem([model.ctx]))

        for i, item in enumerate(model.vdx):
            # child = QTreeWidgetItem(parent)
            tvdx.addChild(QTreeWidgetItem([item]))
            child = tvdx.child(i)
            child.setCheckState(0, Qt.Checked)

        for i, item in enumerate(model.dos):
            tdos.addChild(QTreeWidgetItem([item]))
            child = tdos.child(i)
            child.setCheckState(0, Qt.Checked)

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
        self.popup_menu_ctx = self.create_popup_menu_ctx()
        self.popup_menu_vdx = self.create_popup_menu_vdx()

    def create_popup_menu_ctx(self):
        popup_menu = QMenu(self.view.tw)
        popup_menu.addAction("New CTX", self.menu_open)
        popup_menu.addAction("Rename CTX", self.menu_open)
        popup_menu.addSeparator()
        popup_menu.addAction("Delete CTX", self.menu_open)
        return popup_menu

    def create_popup_menu_vdx(self):
        popup_menu = QMenu(self.view.tw)
        popup_menu.addAction("New VDX", self.menu_open)
        popup_menu.addAction("Rename VDX", self.menu_open)
        popup_menu.addSeparator()
        popup_menu.addAction("Delete VDX", self.menu_open)
        return popup_menu

    def setup_callbacks(self, view):
        tw = view.tw

        logger.debug("setup_callbacks()")
        view.btn.clicked.connect(lambda: self.add_data())
        # view.btn.clicked.connect(self.odd_doto)
        tw.setContextMenuPolicy(Qt.CustomContextMenu)
        tw.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos):
        tw = self.view.tw

        getSelected = tw.selectedItems()
        if getSelected:

            baseNode = getSelected[0]  # QTreeWidgetItem
            parent = baseNode.parent()  # QTreeWidgetItem
            getChildNode = baseNode.text(0)

            logger.debug("Node name: {}".format(getChildNode))
            if parent:
                logger.debug("parent: {}".format(parent.text(0)))
            else:
                return

        logger.debug("on_context_menu() {}".format(pos))

        logger.debug("menu_context() {}".format(pos))
        node = tw.mapToGlobal(pos)

        if parent.text(0) == "CTX":
            action = self.popup_menu_ctx.exec_(tw.mapToGlobal(pos))

        elif parent.text(0) == "ROIs":
            action = self.popup_menu_vdx.exec_(tw.mapToGlobal(pos))

        else:
            return

        logger.debug("action: {}".format(action.text()))
        logger.debug("node: {}".format(node))

    def menu_open(self):
        logger.debug("menu_open()")

    def add_data(self):
        logger.debug("add_data()")
        self.model.vdx.append("Smerg")
        self.tvdx.addChild(QTreeWidgetItem(["Smerg"]))
        child = self.tvdx.child(self.tvdx.childCount() - 1)  # get the ref to last added chiled
        child.setCheckState(0, Qt.Unchecked)

    def update_tree():
        pass
