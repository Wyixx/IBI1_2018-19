# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 00:27:00 2019

@author: Wyxx
"""
#To judge if it is divisible by 7
b=123123
y=b%7
print(y)

#define a,b,c,d,e
a=123
b=123123
c=b/7
d=c/11
e=d/13
print(e)
if a==e:#compare e to a
    print("a==e")
elif a>e:
    print("a>e")
else:
    print("a<e")


x=True
y=False
if (x and not y)or(y and not x):
    print("w is true")
else:
    print("w is false")

x=True
y=False
if x!=y:
    print("z is true")
else:
    print("z is false")