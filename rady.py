# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:56:14 2017

@author: Kuba
"""

import random
#Generuje 20 náhodných čísel od 1 do 50 
seznam = [random.randint(-50,50) for i in range(20)]
print(seznam)

#Počet sudých čísel
n = 0
for x in seznam:
    if((x%2) == 0): n += 1
print("Počet sudých čísel:", n)


#Větší než 11 a menší, než 9
vetsimensi = []
for x in seznam:
    if((x > 11) and (x < 19)): vetsimensi.append(x)
print("Čísla větší než 11 a menší než 19:", vetsimensi)

#Dělitelná 3 a 4
delitelna = []
for x in seznam:
    if(((x%3) == 0) and ((x%4) == 0)): delitelna.append(x)
print("Čísla dělitelná 3 a 4:", delitelna)

#Celkový součet kladných a záporných
kladna = 0
zaporna = 0
for x in seznam:
    if  (x > 0): kladna += x
    elif(x < 0): zaporna += x
print("Součet kladných čísel:", kladna)
print("Součet záporných čísel:", zaporna)

#Součet druhých mocnin
mocniny = 0
for x in seznam:
    mocniny += x**2
print("Součet druhých mocnin:", mocniny)

#Průměr
prumer = sum(seznam)/len(seznam)
print("Aritmetický průměr:", prumer)