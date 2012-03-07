'''
Created on 04.03.2012

@author: Burger
'''
from PySide.QtGui import *
import sys
import threading
from wikiWorker import wikiWorker
from ParserAndCreatorFactory import ParserAndCreatorFactory

        
class MainWindow(QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.resize(800, 480)
        self.setWindowTitle("wiki2sc")
        centralWidget = QWidget(self)
        
        self.textBrowser = QTextBrowser()
        self.pushButton = QPushButton("Make a wonder")
        self.pushButton.setFixedSize(128, 32)
        
        layout = QVBoxLayout(centralWidget)
        layout.addWidget(self.textBrowser)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
        #self.setCentralWidget(centralWidget)
        
        self.pushButton.clicked.connect(self.start)
    
    def start(self): 
        #threading.Thread(target=self.work,name='thread').start()
        self.work()
    
    def work(self):
        ob = wikiWorker('http://ru.wikipedia.org/w/api.php')
        #ob.startPoint('http://ru.wikipedia.org/w/api.php', u'Венера_(планета)')
        templates = ob.templatesFromPage(u'Венера_(планета)')
        myFactory = ParserAndCreatorFactory()
        
        for template in templates:
            templateName = getTamplateName(template)
            parser = myFactory.getParser(templateName)
            information = parser.parse(template)
            self.textBrowser.append('JKJ')
            for key in information:
                self.textBrowser.append(unicode(key)+'--------'+ unicode(information[key]))
            creator = myFactory.getCreator(templateName)
            self.textBrowser.append(creator.create(template))

def work():
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())

