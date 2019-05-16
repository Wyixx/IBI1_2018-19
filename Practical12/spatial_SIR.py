# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:10:55 2019

@author: Wyxx
"""

import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptible population
#0 for susceptible, 1 for infected, 2 for recovered
population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1 #select a point and infect it randomly (it changes from 0 to 1)

#plot the heat map at time 0
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')

beta=0.3 #probability to be infected
gamma=0.05 #probability to recover

#loop for 100 times
for n in range(1,101):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x=infectedIndex[0][i]
        y=infectedIndex[1][i]
        population[x,y]=np.random.choice(range(3),1,p=[0,1-gamma,gamma])[0] #0 for susceptible,1 for infected,2 for recovered
        #or:population[x,y]=np.random.choice(range(1,3)),1,p=[1-gamma,gamma][0] 


        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]

                            
    #plot the heat map at times 10,50 and 100
    if n in [10,50,100]:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')                      
            
#count infection times
#find infected points
#If the neighbor is not infected, determine whether infects it or not randomly. And follow the probability beta.
#If it is infected, determine whether it will recover or not randomly. And follow the probabilty gamma.
    
   

    
