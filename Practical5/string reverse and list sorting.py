# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:00:46 2019

@author: Wyxx
"""

s=input()
s=s[ : :-1]
s=s.split(" ")
L=sorted(s)
L.reverse()
print(L)