# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:18:05 2017

@author: Kuba
"""

n = input("Kolik řádků se má tisknout? > ")
n = int(n)

print("\n")
#Tisk pravoúhlého trojúhelníku
for i in range (0, n):
    print((n-i)*"*")
    
print("\n")
#Tisk pyramidy
for i in range (0, n):
    print((n-1-i)*" " + (1+2*i)*"*")
    
print("\n")
#Tisk šipky
for i in range (0, n):
    if((i+1) <= (n/2)):         print((i+1)*"*")
    else:                       print((n-i)*"*")