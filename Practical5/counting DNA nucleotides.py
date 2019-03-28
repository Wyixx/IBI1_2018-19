# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:16:22 2019

@author: Wyxx
"""

DNA=input()#input a sequence of DNA
myDict={}
for word in DNA:
    if word in myDict:#count the number of ATCG (a specific kind of nucleotide)
        myDict[word]+=1
    else:
        myDict[word]=1 #There is only one such nucleotide
print(myDict)
import matplotlib.pyplot as plt#plot the proportions of different nucleotides
labels='A','T','C','G'
sizes=tuple(myDict.values())
explode=(0,0.1,0,0)
Fig,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.show()
