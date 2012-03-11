# -*- coding: utf-8 -*-
'''
Created on 15.02.2012

@author: Burger
'''
from wikiWorker import wikiWorker
from ParserAndCreatorFactory import ParserAndCreatorFactory
from compiler.ast import Printnl, TryFinally


def parseTemplete(path,template,templateName,myFactory):
    parser = myFactory.getParser(templateName)
    information = parser.parse(template)
    creator = myFactory.getCreator(templateName)
    result=creator.create(information)
        
    f = file(unicode(path+result['name'])+'.gwf',"w")
    f.write(result['information'])
    f.close()


def workWithPage(worker,page,pathToSave):
    worker.add(page)
    templates = worker.templatesFromPage(page)
    result=False
    try:
        if(len(templates)>0):
            result=True
            myFactory = ParserAndCreatorFactory()
            for template in templates:
                parseTemplete(pathToSave,template,worker.getTamplateName(template),myFactory)
    except:
        print 'ERROR page--',page,'\n'
        result=False
                  
    return result

def work(worker,page,pathToSave):
    links=[page]
    while(1):
        newWave=[]
        print '--------------------------',len(links),'---------------------------------'
        for link in links:
            if worker.was(link):continue
            print link,
            if workWithPage(worker,link, pathToSave):
                newWave=newWave+worker.getLinksFromPage(link)
                print ' yes'
            else: print ' no'
        links=[]
        if len(newWave)>0:
            links=newWave
        else:break

worker=wikiWorker('http://ru.wikipedia.org/w/api.php')
work(worker,u'Уран_(планета)','C:\\Users\\Burger\\Desktop\\')
