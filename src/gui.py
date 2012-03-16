# -*- coding: utf-8 -*-
'''
Created on 16.03.2012

@author: kulex4
'''
import sys
import wiki2SC

from PySide.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 480)
        self.setWindowTitle("wiki2SC")
        centralWidget = QWidget(self)
        
        self.textBrowser = QTextBrowser()
        self.pushButton = QPushButton("Start")
        self.pushButton.setFixedSize(128, 32)
        
        layout = QVBoxLayout(centralWidget)
        layout.addWidget(self.textBrowser)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
        self.setCentralWidget(centralWidget)
        
        self.pushButton.clicked.connect(self.startWork)
    
    def startWork(self):
        operator = wiki2SC.wiki2SC(path='D:\\gwf-wiki\\',siteName='http://ru.wikipedia.org/w/api.php',log=self.textBrowser)
        operator.work( page=u'Уран_(планета)')
        self.textBrowser.append("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())
