# -*- coding: utf-8 -*-
'''
Created on 27.02.2012

@author: Burger
'''
import re

def fromText(text):
    templates = []
    kol = 0
    template = ""
    for sim in text:
        if kol == 0 and template != "":
            template + '}'
            templates.append(template + '}')
            template = ""
        if sim == '{': kol = kol + 1
        elif sim == '}': kol = kol - 1
        if kol != 0: template = template + sim
    if template!='' and kol==0: templates.append(template)
    prev=''
    our=False
    templete=''   
    for sim in text:
        if sim=='!' and prev=='<':
            our=True
            templete=prev+sim
        elif sim!='>' and our:
            templete=templete+sim
        elif sim=='>':
            templates.append(templete)
            templete=''
            our=False
        prev=sim
    
    return templates

class baseParser():
    
    def dellSpaces(self,text):
        k=0
        for sym in text:
            if sym==' ':
                k=k+1
            else:break
        text=text[k:len(text)]
        k=0
        text1=text[::-1]
        l=len(text)-1
        while(l>-1):
            if text[l]==' ' or text[l]=='\n':l=l-1
            else:break
        
        text=text[0:l+1]
        
        return text
    
    def templateUnification(self,template):
        dell=fromText(template[2:len(template)])
        for templ in dell:
            template=re.sub(templ,'', template)
        template=re.sub('<br />','\n', template)
        template=re.sub(r'\[.*|.*\]','', template)
        template=re.sub('&nbsp;','', template)
        template=re.sub('<ref.*>','', template)
        template=re.sub('</ref>','', template)
        template=re.sub('<sup>','^',template)
        template=re.sub('</sup>','',template)
        
        template=re.sub('<','&lt;',template)
        template=re.sub('&','&amp;',template)
        template=re.sub('>','&gt;',template)
        template=re.sub('"','&quot;',template)
         
        return template
    
    def _keyValue(self, template):
        template=self.templateUnification(template)
        information={}   
        key=''
        word=''
        first=False
        for sym in template:
            if sym == '|':
                key=self.dellSpaces(key)
                word=self.dellSpaces(word)
                if word!='' and key!='':
                    information[self.dellSpaces(key)]=self.dellSpaces(word)
                key=''
                word=''
            elif sym=='=':
                key=word
                word=''
            else: word=word+sym
        return information
    
    def parse(self, template): return self._keyValue(template)
    
class planetParser(baseParser):
    def parse(self, template): return self._keyValue(template)