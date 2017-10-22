# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 19:31:12 2017

@author: Kuba
"""

n = input("Kolik členů posloupnosti se má tisknout? > ")
n = int(n)
posloupnost = [0, 1]
for i in range (0, n):
    posloupnost.append(posloupnost[i]+posloupnost[i+1])
print(posloupnost)