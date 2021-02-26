# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:11:07 2021

@author: User
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

def bailar(arreglo):
    for i in range(len(arreglo)-1): # n +c0
        j = i # c1
        while arreglo[j+1] < arreglo[j] and j>-1:  # n  
            aux = arreglo[j] # c3
            arreglo[j] = arreglo[j+1] # c4
            arreglo[j+1] = aux # c5
            j = j-1 # c6
    return arreglo # c7
            

print(bailar([2, 1, 5, 9, 0, -1, 10, 3, 89, 0]))


import time
import matplotlib.pyplot as plt
from numpy import random

def plot(times, n, lab):
    plt.xlabel('') 
    plt.ylabel('Time Complexity') 
    plt.plot(range(1, n), times, label = lab) 
    plt.grid() 
    plt.legend() 
    plt.show()

times = []

x= 600

for i in range(1, x):
    start_time = time.time()
    bailar(random.randint(50, size=i))
    times.append(time.time() - start_time)
    
plot(times, x, "b")