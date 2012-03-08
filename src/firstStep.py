# -*- coding: utf-8 -*-
'''
Created on 15.02.2012

@author: Burger
'''
from wikiWorker import wikiWorker
from ParserAndCreatorFactory import ParserAndCreatorFactory
from compiler.ast import Printnl


def parseTemplete(path,template,templateName,myFactory):
    parser = myFactory.getParser(templateName)
    information = parser.parse(template)
    creator = myFactory.getCreator(templateName)
    result=creator.create(information)
        
    f = file(unicode(path+result['name'])+'.gwf',"w")
    f.write(result['information'])
    f.close()


def work(worker,firstPage,pathToSave):
    templates = worker.templatesFromPage(firstPage)
    myFactory = ParserAndCreatorFactory()
    for template in templates:
        parseTemplete(pathToSave,template,worker.getTamplateName(template),myFactory)   

worker=wikiWorker('http://ru.wikipedia.org/w/api.php')
work(worker,u'Уран_(планета)','C:\\Users\\Burger\\Desktop\\')
