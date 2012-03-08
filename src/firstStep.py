# -*- coding: utf-8 -*-
'''
Created on 15.02.2012

@author: Burger
'''
from wikiWorker import wikiWorker
from ParserAndCreatorFactory import ParserAndCreatorFactory
from compiler.ast import Printnl

def work():
    ob = wikiWorker('http://ru.wikipedia.org/w/api.php')
    #ob.startPoint('http://ru.wikipedia.org/w/api.php', u'Венера_(планета)')
    templates = ob.templatesFromPage(u'Уран_(планета)')
    myFactory = ParserAndCreatorFactory()
    
    for template in templates:
        templateName =ob.getTamplateName(template)
        parser = myFactory.getParser(templateName)
        information = parser.parse(template)
        creator = myFactory.getCreator(templateName)
        result=creator.create(information)
        path='C:\\Users\\Burger\\Desktop\\'
        print path,result['name']
        f = file(unicode(path+result['name'])+'.gwf',"w")
        f.write(result['information'])
        f.close()
        
        print templateName,'-',result['name']

gui=False
if gui:
    import workWithGui
    workWithGui.work()
else: work()