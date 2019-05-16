# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:13:55 2019

@author: Wyxx
"""


import xml.dom.minidom
import pandas as pd
import re

df=pd.DataFrame(columns=['id','name','definition','childnodes'])
DOMTree=xml.dom.minidom.parse('go_obo.xml')
obo=DOMTree.documentElement

#define how to count childnodes
def Child(id,geneset):
    for t in terms:
        parents=t.getElementsByTagName('is_a')
        gene=t.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data==id:
                geneset.add(gene)
                Child(gene,geneset)#At first, I forgot this step.Then it couldn't find the childnodes of the childnode.
                #we have to make sure that there is no more childnode

terms=obo.getElementsByTagName('term')
for term in terms:
    defstr=term.getElementsByTagName('defstr')[0].childNodes[0].data
    if re.search('autophagosome',defstr): #find genes related with 'autophagosome' (contain word 'autophagosome')
        #find the information of target genes and put them into dataframe
        id=term.getElementsByTagName('id')[0].childNodes[0].data
        name=term.getElementsByTagName('name')[0].childNodes[0].data
        geneset=set()
        Child(id,geneset)#use the function to find childnodes
        df=df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(geneset)]}))
        print(id,len(geneset))
df.to_excel('autophagosome_full.xlsx',index=False)


    

