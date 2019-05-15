# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:53:03 2019

@author: Wyxx
"""

number_list=input()
number_list=list(number_list)
number_list.sort()#sort numbers input from the smallest to the biggest
print(number_list)
operator_list=['+','-','*','/']
def insertParentheses(number_list,operator_list):
    count=0
    expression_list=[]
    for each_number_list in number_list:
        for each_operator_list in number_list:
            expression1=str(each_number_list[0])+each_operator_list[0]+str(each_number_list[1])+each_operator_list[1]+str(each_number_list[2])+each_operator_list[2]+str(each_number_list[3])
            try:
                result=eval(expression1)
            except:
                result=0
            if result==24:
                expression_list.append(expression1+'='+str(result)
                count+=1
            else:
                expression2
                

