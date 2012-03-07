# -*- coding: utf-8 -*-
'''
Created on 27.02.2012

@author: kulex4
'''
from creators.templateCreator import*
from parsers.templateParser import *

class ParserAndCreatorFactory():
    _parsers = {}
    _creators = {}
    def __init__(self):
        a = planetParser()
        self._parsers['карточка планеты'] = a
        
        b = planetCreator()
        self._creators['карточка планеты'] = b
                
    def getParser(self, information):
        if information in self._parsers:
            parser = self._parsers[information]
        else: parser = baseParser()
        return parser
    
    def getCreator(self, information):
        if information in self._creators:
            creator = self._creators[information]
        else: creator = baseCreator()
        return creator