# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 23:58:03 2019

@author: Wyxx
"""

#judge whether x is even or odd using x%2
#if x is even, dividing by 2
#if x is odd, multipying 3 and adding 1
x=int(input("Enter an integer:"))
while x!=1:
    if x%2==0:
        x=x/2
    else:
        x=x*3+1
    print(x)