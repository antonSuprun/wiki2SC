# -*- coding: utf-8 -*-
'''
Created on 15.02.2012

@author: Burger
'''
from wikiWorker import wikiWorker
from ParserAndCreatorFactory import ParserAndCreatorFactory
from compiler.ast import Printnl, TryFinally

class wiki2SC():
    _path=None
    _worker=None
    def __init__(self,path="",siteName = 'http://en.wikipedia.org/w/api.php'):
        self._path=path
        self._worker=wikiWorker('http://ru.wikipedia.org/w/api.php')
    
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
        templates = self._worker.templatesFromPage(page)
        result=False
        try:
            if(len(templates)>0):
                result=True
                myFactory = ParserAndCreatorFactory()
                for template in templates:
                    self.parseTemplete(self._path,template,self._worker.getTamplateName(template),myFactory)
        except:
            print 'ERROR page--',page,'\n'
            result=False
                      
        return result
    
    def work(self,page):
        links=[page]
        while(1):
            newWave=[]
            print '--------------------------',len(links),'---------------------------------'
            for link in links:
                if self._worker.was(link):continue
                print link,
                if self.workWithPage(page=link):
                    newWave=newWave+self._worker.getLinksFromPage(link)
                    print ' yes'
                else: print ' no'
            links=[]
            if len(newWave)>0:
                links=newWave
            else:break

operator=wiki2SC(path='C:\\Users\\Burger\\Desktop\\',siteName='http://ru.wikipedia.org/w/api.php')
operator.work( page=u'Уран_(планета)')
