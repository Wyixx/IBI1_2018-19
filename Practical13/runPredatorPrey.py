# -*- coding: utf-8 -*-
"""
Created on Wed May 15 10:16:39 2019

@author: Wyxx
"""

import os
os.chdir('C:/Users/Wyxx/Documents/git/IBI1_2018-19/Practical13')


#convert xml file to cps and generate modelResult.csv(Melanie's code)
def xml_to_cps():
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w",encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
y=xml_to_cps()

#------------------------------------------------------------
os.chdir('C:/Users/Wyxx/Documents/git/IBI1_2018-19/Practical13')
os.system('CopasiSE.exe predator-prey.cps')
# run a Copasi ﬁle from within Python 


import re
import numpy
import matplotlib.pyplot as plt


xfile=open('modelResults.csv')
reader=xfile.readlines()
data=[]
row=1

for line in reader:
    splited=re.split(',|\n',line)
    splited.remove('')#delete'\n'
    row+=1 #as the first row is [time],[A],[B],it should be seperated
    if row>2:
        data.append(splited)

    
results=numpy.array(data)
results=results.astype(numpy.float)

#plot figure
plt.figure(figsize=(6,4),dpi=150)
plt.plot(results[:,0],results[:,1],label='Predator (b=0.02,d=0.4)')#the first column(0) is time, the second column(1)is the about predator
plt.plot(results[:,0],results[:,2],label='Prey (b=0.1,d=0.02)')#the third column(2) is about prey
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time Course')
plt.legend(loc='upper right')

#plot 'limit cycle'
plt.figure(figsize=(6,4),dpi=150)
plt.plot(results[:,1],results[:,2])#the relationship between the population of predators(column[1]) and the population of preys(column[2])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('Limit cycle')


#------------------changing values--------------------------------------
import xml.dom.minidom
DOMTree=xml.dom.minidom.parse('predator-prey.xml')
collection=DOMTree.documentElement
term=collection.getElementsByTagName('listOfParameters')[0]    
parameter=term.getElementsByTagName('parameter')

#edit the parameters
#The exact numbers can vary from 0 to 1
k_predator_dies=0.4
k_predator_breeds=0.02
k_prey_dies=0.02
k_prey_breeds=0.1

for t in parameter:
    if t.getAttribute('name')=='k_predator_dies':                   
        t.setAttribute('value',str(k_predator_dies))                       
    if t.getAttribute('name')=='k_predator_breeds': 
        t.setAttribute('value',str(k_predator_breeds))
    if t.getAttribute('name')=='k_prey_dies': 
        t.setAttribute('value',str(k_prey_dies))
    if t.getAttribute('name')=='k_prey_breeds': 
        t.setAttribute('value',str(k_prey_breeds))
yfile= open('predator-prey.xml','w')
DOMTree.writexml(yfile)
yfile.close()


#parameters have been edited
#Then:
#use the same approach to change xml to cps
#use the same approach to plot figures




#--------------running many simulations--------------------------------
#use a loop to change the four parameters and run simulation several times
#selecet parameters randomly  np.random.sample()
#every time, plot the 'time course'&'limit cycle' figures and store them together with corresponding parameters in a file


#use np.amax() to find the max number of predators during the simulation and print it out

#determine whether prey dies out during the course of the simulation
#use np.amin() to find the minimum number of prey
#compare the minimum value to 0








