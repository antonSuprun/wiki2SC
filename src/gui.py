# -*- coding: utf-8 -*-
'''
Created on 16.03.2012

@author: kulex4
'''
import sys
import wiki2SC

from PySide import QtCore, QtGui

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        logGroup = QtGui.QGroupBox("log")
        self.logBrowser = QtGui.QTextBrowser();
        
        controlGroup = QtGui.QGroupBox("control")
        
        choiceComboBox = QtGui.QComboBox()
        choiceComboBox.addItem("en.wikipedia.org")
        choiceComboBox.addItem("ru.wikipedia.org")
        startButton = QtGui.QPushButton("start")

        logLayout = QtGui.QGridLayout()
        logLayout.addWidget(self.logBrowser, 0, 0)
        logGroup.setLayout(logLayout)
        
        startLayout = QtGui.QGridLayout()
        startLayout.addWidget(choiceComboBox, 0, 0)
        startLayout.addWidget(startButton, 1, 0)
        controlGroup.setLayout(startLayout)
        
        layout = QtGui.QGridLayout()
        layout.addWidget(logGroup, 0, 0)
        layout.addWidget(controlGroup, 0, 1)
        
        self.setLayout(layout)
        self.resize(800, 480)
        self.setWindowTitle("wiki2sc")
        
        choiceComboBox.activated[int].connect(self.choiceChanged)
        startButton.clicked.connect(self.startButton)

    def choiceChanged(self, index):
        if index == 0:
            self.logBrowser.append("eng")
        elif index == 1:
            self.logBrowser.append("rus")
    
    def startButton(self):
        self.thread = WorkThread(self.logBrowser)
        self.thread.start()
        self.thread.exit()
        
class WorkThread(QtCore.QThread):
    def __init__(self, output):
        QtCore.QThread.__init__(self)
        self.output = output
        
    def run(self):
        operator = wiki2SC.wiki2SC(path='D:\\gwf-wiki\\', siteName='http://ru.wikipedia.org/w/api.php', log = self.output)
        operator.work( page=u'Уран_(планета)')
        self.exec_()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
