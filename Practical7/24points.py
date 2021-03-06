# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:53:03 2019

@author: Wyxx
"""
import re
from fractions import Fraction
#-------------------verify input numbers--------------------------
#The input numbers must be interger between 1 and 23
re_numtest = re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)')#intergers between 1 and 23
i = 1
while i:
    i = 0
    data = input('Please input numbers to computer 24:(use \',\' to divide them)\n')
    numList = data.split(',')
    for number in numList:
        if re_numtest.match(number): #test if the input numbers are between 1 and 23
            continue
        else: 
            print('The input number must be intergers from 1 to 23')
            i = 1#if the input numbers are not intergers between 1 to 23, input and test again
            break

num = list(map(int,numList))  
#---------------------count recursion times------------------------
count = 0 
#n is len(num) 
def dfs(n):
    global count
    count = count +1
#the mean idea is to reduce the numbers one by one
#every time, select 2 numbers and perform various operations
#as 2 numbers run(+=*/) into one, the length of input numbers decreases
    if n == 1:
        if(float(num[0])==24):#1 means the 24 has been calculated successfully
            return 1
        else:
            return 0#0 means no 24 is calculated
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            a = num[i]
            b = num[j]
            num[j] = num[n-1]
            
            num[i] = a+b
            if(dfs(n-1)):
                return 1
            
            num[i] = a-b
            if(dfs(n-1)):
                return 1  
            
            num[i] = b-a
            if(dfs(n-1)): 
                return 1 
            
            num[i] = a*b
            if(dfs(n-1)): 
                return 1  
            
            if a:
                #floats are not precise
                num[i] = Fraction(b,a)#handling rational numbers
                if(dfs(n-1)): 
                    return 1 
                
            if b:
                num[i] = Fraction(a,b)
                if(dfs(n-1)): 
                    return 1 
            #Backtracking  
            num[i] = a
            num[j] = b
    return 0 

#-----------------------run the function with inputted numbers------------------
if (dfs(len(num))): 
    print('Yes')
else: 
    print('No')
print('Recursion times:',count)

                

