# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:09:13 2019

@author: Wyxx
"""

import numpy as np
import matplotlib.pyplot as plt

N=10000 #total number of people in the population
I=1 #number of the infected
R=0 #the recovered
S=N-I-R #the susceptible
beta=0.3 #probability to be infected
gamma=0.05 #probability to recover

i=[]
r=[]
s=[]

#use a variable to control the loop number
#use 0 and 1 to represent two situations in each random choice
count=0
while count<1000:
    inf=np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N]) # 0 for susceptible, 1 for infected
    infected=sum(inf) #as '1' is for infected, 'sum' can get the number of people that get infected this time
    I=I+infected
    S=S-infected
    s.append(S)
    
    rec=np.random.choice(range(2),I,p=[1-gamma,gamma])# 0 for infected, 1 for recovered
    recovered=sum(rec)
    I=I-recovered
    R=R+recovered
    i.append(I)
    r.append(R)
    count += 1
print('the number of susceptible people is',S)
print('the number of infected people is',I)
print('the number of recovered people is',R)

###plot the figure
plt.figure(figsize=(6,4),dpi=150)
plt.plot(s,color='blue')
plt.plot(i,color='orange')
plt.plot(r,color='green')
plt.legend(labels=['susceptible','infected','recovered'],loc='upper right')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.savefig('C:/Users/Wyxx/Documents/git/IBI1_2018-19/Practical12/SIR model.png',type='png')