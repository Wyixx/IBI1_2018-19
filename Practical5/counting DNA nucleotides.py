# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:16:22 2019

@author: Wyxx
"""

DNA=input()
DNA=DNA.split(" ")
myDict={}
for word in DNA:
    if word in myDict:
        myDict[word]+=1
    else:
        myDict[word]=1
print(myDict)
import matplotlib.pyplot as plt
labels='A','T','C','G'
sizes=tuple(myDict.values())
explode=(0,0.1,0,0)
fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()
