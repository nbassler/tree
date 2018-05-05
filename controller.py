import logging

from PyQt5.QtWidgets import QTreeWidgetItem


logger = logging.getLogger(__name__)


class TreeCtrl(object):

    def __init__(self, model, view):
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

    def setup_callbacks():
        pass

    def add_data():
        pass

    def update_tree():
        pass
