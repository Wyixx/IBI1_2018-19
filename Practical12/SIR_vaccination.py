# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:31:25 2019

@author: Wyxx
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4),dpi=150)
V=0 #the vaccinated
while V<10000:
    N=10000 #toal number of people in the population
    I=1 #number of the infected
    R=0 #the recovered
    S=N-I-R-V #the susceptible
    beta=0.3 #probability to be infected
    gamma=0.05 #probability to recover

    i=[]
    r=[]
    s=[]

#use a variable to control the loop number
#use 0 and 1 to represent two situations in each random choice
    count=0
    while count<1000:
        inf=np.random.choice(range(2),S,p=[1-beta*I/N,beta*I/N])
        infected=sum(inf)
        I=I+infected
        S=S-infected
        s.append(S)
    
        rec=np.random.choice(range(2),I,p=[1-gamma,gamma])
        recovered=sum(rec)
        I=I-recovered
        R=R+recovered
        i.append(I)
        r.append(R)
        count += 1
        
    plt.plot(i,label='{:3.2f}%'.format(V/N*100))
    plt.legend(loc='upper right')
    plt.xlabel('time')
    plt.ylabel('number of people')
    plt.title('SIR model with different vaccination rates')
    V=V+1000
plt.plot(0,label='100.00%')
plt.legend(loc='upper right')
plt.savefig('C:/Users/Wyxx/Documents/git/IBI1_2018-19/Practical12/SIR_vaccination model.png',type='png')
    
    

    


   
