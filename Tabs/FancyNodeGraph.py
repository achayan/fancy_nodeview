
import platform
import os
from Katana import QtGui, QtWidgets, QtCore, UI4
import NodegraphAPI

class DropPanelPanel(UI4.Tabs.BaseTab):
    def __init__(self, parent):
        UI4.Tabs.BaseTab.__init__(self, parent)
        layout = QtWidgets.QVBoxLayout(self)
        self.__formats = {".abc":["Alembic_In", "abcAsset"], ".usd":["UsdIn", "fileName"],".usda":["UsdIn", "fileName"],".usdc":["UsdIn", "fileName"], ".usdz":["UsdIn", "fileName"]}
        self.setLayout(layout)
        # this is a bad idea but it works. For some reason we get event triggered twice
        # With this check we can stop that
        self.isTriggered = False
        self.searchStr = "file://"
        if platform.system() == "Windows":
            self.searchStr = "file:///"
        self.__nodeGraph = UI4.App.Tabs.FindTopTab('Node Graph', alsoRaise=False)
        self.__nodeGraph.setAcceptDrops(True)
        layout.addWidget(self.__nodeGraph)
        self.__nodeGraph.installEventFilter(self)

    def eventFilter(self, target, e):
        if isinstance(e, QtGui.QDropEvent):
            if not self.isTriggered:
                mime = e.mimeData()
                files_to_import = bytes(mime.data('text/uri-list')).decode()
                files_to_import = files_to_import.split("\r\n")
                for eachItem in files_to_import:
                    if eachItem:
                        impFile = eachItem.replace(self.searchStr, "")
                        if os.path.exists(impFile):
                            file_path, ext = os.path.splitext(impFile)
                            xn = yn = 0
                            allNodes = NodegraphAPI.GetAllSelectedNodes()
                            if allNodes:
                                (xn, yn) = NodegraphAPI.GetNodePosition(allNodes[0])
                            if ext in self.__formats:
                                nodeData = self.__formats[ext]
                                inNode = NodegraphAPI.CreateNode(nodeData[0],NodegraphAPI.GetRootNode())
                                inNode.getParameter(nodeData[1]).setValue(str(impFile), 0)
                                inNode.setName(str(os.path.basename(file_path)))
                                NodegraphAPI.SetNodePosition(inNode, (xn, yn - 50))
                self.isTriggered = True
                return True
            else:
                self.isTriggered = False
        return QtCore.QObject.eventFilter(self, target, e)

PluginRegistry = [
("KatanaPanel", 2.0, " Fancy Node Graph", DropPanelPanel),
]