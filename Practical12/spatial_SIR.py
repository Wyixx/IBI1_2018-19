# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:10:55 2019

@author: Wyxx
"""

import numpy as np
import matplotlib.pyplot as plt

#make array of all susceptible population
population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap='viridis',interpolation='nearest')

beta=0.3 #probability to be infected
gamma=0.05 #probability to recover
