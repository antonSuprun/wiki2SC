# -*- coding: utf-8 -*-
'''
Created on 27.02.2012

@author: Burger
'''
import datetime
import re

class baseCreator():
    forId=1
    names=[]
    def create(self,information):
        return "base creator"
    
    def getID(self,name):
        if name=='' or name in self.names:
            self.forId=self.forId+1
            id=abs(hash(self.forId))
        else: id=str(abs(hash(name)))
        if not name in self.names: self.names.append(name)
        return id
       
    def genNode(self,name,x,y,space='',type='general_node'):
        id=self.getID(name)
        node=space+'<node type="node/const/'+type+'" idtf="'+unicode(name)+'" shapeColor="0" id="'+unicode(id)+'" parent="0" left="0" top="0" right="36" bottom="25" textColor="164" text_angle="0" text_font="Times New Roman [Arial]" font_size="10" x="'+str(x)+'" y="'+str(y)+'" haveBus="false">\n'
        node=node+space+'    <content type="0" mime_type="" file_name=""/>\n'+space+'</node>\n'
        return {'node':node,'id':id}
    
    def genArc(self,name='',b_x=0,b_y=0,e_x=0,e_y=0,id_b=0,id_e=0,space='',type='arc/const/pos',dotBBalance=0, dotEBalance=0,nodeType='arc'):
        id_b=str(id_b)
        id_e=str(id_e)
        id=self.getID(name)
        arc=space+'<'+nodeType+' type="'+type+'" idtf="'+name+'" shapeColor="0" id="'+str(id)+'" parent="0" id_b="'+str(id_b)+'" id_e="'+str(id_e)+'" b_x="'+str(b_x)+'" b_y="b_y" e_x="'+str(e_x)+'" e_y="'+str(e_y)+'" dotBBalance="'+str(dotBBalance)+'" dotEBalance="'+str(dotBBalance)+'">\n'
        arc=arc+space+'    <points/>\n'+space+'</'+nodeType+'>\n'
        return {'arc':arc,'id':id}

    
class planetCreator(baseCreator):
    def groupName(self):
        return'планета'
    def create(self,information):
        result='<?xml version="1.0" encoding="UTF-8"?>\n'
        result=result+'<GWF version="1.6">\n'
        space='    '
        result=result+space+'<staticSector>\n'
        space=space+space
        
        group=self.genNode(name=self.groupName(),x=293, y=58, space=space, type='group')
        planet=self.genNode(name=information['название'], x=140, y=64, space=space)
        arc=self.genArc(b_x=293, b_y=58, e_x=140, e_y=64, id_b=group['id'], id_e=planet['id'], space=space, type='arc/const/pos')
        
        result=result+group['node']+'\n'+planet['node']+'\n'+arc['arc']
        
        x=217
        y=130
        space='        '
        for rel,inf in information.iteritems():
            name=unicode(rel)
            relation=self.genNode(name,x,y,space,'relation')
            result=result+relation['node']
            
            node=self.genNode(name=inf, x=x+50, y=y+50, space=space)
            result=result+node['node']
            
            node2=self.genNode(name=information['название'], x=x-50, y=y+50, space=space)
            result=result+node2['node']
                       
            pair=self.genArc(b_x=293,b_y=58,e_x=x, e_y=y, id_b=node2['id'], id_e=node['id'], space=space, type='pair/const/orient',nodeType='pair')
            
            arc=self.genArc(b_x=x, b_y=y,id_b=relation['id'], id_e=pair['id'], space=space, dotBBalance=0.5)
            result=result+pair['arc']+arc['arc']            
            y=y+120
     
        #bus=space+'<bus type="" idtf="" shapeColor="0" id="64731704" parent="0" owner="63495480" b_x="139.739" b_y="63.4977" e_x="139.739" e_y="'+str(y-50)+'">\n'
        #bus=bus+space+'    <points/>\n'+space+'</bus>\n'
        
        space='    '
        result=result+space+'</staticSector>\n'
        result=result+'</GWF>\n'
        result=re.sub('&','&amp;', result)
        answer={'name':information['название'],'information':result}
        return answer

#parser=planetParser()
