# -*- coding: utf-8 -*-
'''
Created on 15.02.2012

@author: Burger
'''
from wikiWorker import wikiWorker
from ParserAndCreatorFactory import ParserAndCreatorFactory

class wiki2SC():
    _path=None
    _worker=None
    streamLog=None
    def __init__(self,path="", siteName = 'http://ru.wikipedia.org/w/api.php', log = None):
        self.streamLog = log
        self._path = path
        self._worker = wikiWorker(siteName)
    
    def parseTemplete(self,path,template,templateName,myFactory):
        parser = myFactory.getParser(templateName)
        information = parser.parse(template)
        creator = myFactory.getCreator(templateName)
        result=creator.create(information)
            
        f = file(unicode(path+result['name'])+'.gwf',"w")
        f.write(result['information'])
        f.close()
    
    
    def workWithPage(self,page):
        self._worker.add(page)
        templates = self._worker.templatesFromPage(page)# только шаблоны поддающиеся парсингу
        result=False
        try:
            if(len(templates)>0):
                result=True
                myFactory = ParserAndCreatorFactory()
                for template in templates:
                    self.parseTemplete(self._path,template,self._worker.getTamplateName(template),myFactory)
        except:
            self.streamLog.append('ERROR page--'+page)
            print 'ERROR page--',page,'\n'
            result=False
                      
        return result
    
    def work(self,page):
        links=[page]
        while(1):
            newWave=[]
            print '--------------------------',len(links),'---------------------------------'
            kol=0
            for link in links:
                kol=kol+1
                if self._worker.was(link):continue
                self.streamLog.append(link)
                print link,
                if self.workWithPage(page=link):
                    newWave=newWave+self._worker.getLinksFromPage(link)
                    self.streamLog.append('yes')
                    print ' yes'
                else:
                    self.streamLog.append('no')
                    print ' no'
                if kol>10:break
            links=[]
            if len(newWave)>0:
                links=newWave
            else:break



#operator=wiki2SC(path='D:\\gwf-wiki\\',siteName='http://ru.wikipedia.org/w/api.php')
#operator.work( page=u'Уран_(планета)')
