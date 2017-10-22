#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 12:35:08 2017

@author: vas35137
"""

n = input("Kolik řádků má tisknout? > ")
n = int(n)

pole = []
num = [1]

flag = [0,0,0]

pole.append(num)




for y in range(1, n):
    num = []
    for x in range(0, (len(pole[y-1])+1)):    #Generuje o jedno číslo, než je počet čísel v předchozím řádku
       num.append(x) 
    pole.append(num)
    

"""    
    
    
    if  (x-1 < 0):                 
            num.append(pole[y-1][x])
            flag[0] += 1
        elif((x+1) > len(pole[y-1])):  
            num.append(pole[y-1][x-1])
            flag[1] += 1
        else:                          
            num.append((pole[y-1][x]) + (pole[y-1][x-1]))
            flag[2] += 1
            
"""