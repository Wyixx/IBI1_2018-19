# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:00:46 2019

@author: Wyxx
"""

s=input('please enter a string of words:\n')
s=s[ : :-1]
s=s.split(" ") #get the words from the string, split by spaces

#sort & reverse
L=sorted(s)
L.reverse()
print(L)