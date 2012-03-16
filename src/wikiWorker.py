# -*- coding: utf-8 -*-
'''
Created on 26.02.2012

@author: Burger
'''
from wikitools import wiki
from wikitools import category
from wikitools import page

class wikiWorker():
    _site = None
    _nameSite = None
    _links = []
    _templateNames = ['карточка планеты']
    
    def __init__(self, siteName = 'http://en.wikipedia.org/w/api.php'):
        self._nameSite = siteName       
    
    def __pageAndSite__(self,article):
        wikiversion = ""
        page = ""
        res = ""
        work = False
        for sim in unicode(unicode(article)):
            if(sim == "'"):
                work = not work
                if(not work):
                    if(page == ""): page = res
                    else: wikiversion = res 
                    res = ""
            elif(work):
                res = res + sim
        return {page:wikiversion}        
    
    def articlesFromCategory(self, siteName = 'http://en.wikipedia.org/w/api.php', categortName = u'Языки_программирования_по_алфавиту'):
        self._site = self._openSite(siteName) 
        programingCategory = category.Category(self._site, unicode(categortName))
        #return map(self.__pageAndSite__, programingCategory.getAllMembers())
        articles = {}
        for article in programingCategory.getAllMembers():
            articles.update(self.__pageAndSite__(article))
        return articles
    
    def _openSite(self, siteName = None):
        if(self._nameSite != siteName or self._nameSite == None):
            if siteName is not None:
                self._nameSite = siteName
            self._site = wiki.Wiki(self._nameSite)
        return self._site
    
    def add(self,link):
        self._links.append(link)
        
    def was(self,link):
        return link in self._links
        
    def getLinksFromPage(self,pageName):
        myPage = page.Page(self._site, pageName)
        return myPage.getLinks()
    
    def startPoint(self, siteName, pageName):
        self._site = self._openSite(siteName)
        myPage = page.Page(self._site, pageName)
        self.addOrMarkLink(pageName)
        for link in myPage.getLinks():
            self.addOrMarkLink(link)
    
    def getTamplateName(self, template = None):
        name = ""
        for sim in template:
            if sim != '{' and sim != '|' and sim != '\n':
                name = name + sim
            elif sim == '|':
                break
        return unicode(name).lower()
        
    def templatesFromPage(self, pageName):
        self._site = self._openSite()
        myPage = page.Page(self._site, pageName)
        if not myPage.exists: return []
        pageText = myPage.getWikiText()
        pageTemplates = []
        kol = 0
        template = ""
        for sim in pageText:
            if kol == 0 and template != "":
                template + '}'
                if self.getTamplateName(template) in self._templateNames:
                    pageTemplates.append(template + '}')
                template = ""
            if sim == '{': kol = kol + 1
            elif sim == '}': kol = kol - 1
            if kol != 0: template = template + sim
        return pageTemplates