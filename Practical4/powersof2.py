# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 00:25:59 2019

@author: Wyxx
"""

#define x as the power, count down from 13
x=13
#input the number n
n=int(input())
#define a as the output
a=str(n)+"is 2**"
#loop
while n!=0:
    if n-2**x<0:
        x=x-1#select a smaller power
        continue
    if n-2**x>0:
        a=a+str(x)+"+2**"
        n=n-2**x
        continue
    if n-2**x==0:
        a=a+str(x)
        break
print(a)