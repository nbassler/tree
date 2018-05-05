import logging

from PyQt5.QtWidgets import QTreeWidgetItem


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

    def setup_callbacks(self, view):
        logger.debug("setup_callbacks()")
        view.btn.clicked.connect(self.add_data)
        view.btn.clicked.connect(self.odd_doto)

    @staticmethod
    def odd_doto(self):
        logger.debug("odd_doto()")

    def add_data(self):
        logger.debug("add_data()")
        # self.model.vdx.append("Smerg")
        # self.tvdx.addChile(QTreeWidgetItem(["Smerg"]))

    def update_tree():
        pass
