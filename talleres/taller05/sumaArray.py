# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:05:38 2021

@author: User
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

def sumaArray(arreglo):
    suma = 0
    for i in range(len(arreglo)):
        suma = suma + arreglo[i]
    return suma
    

# arreglo= [1, 2, 3]
# print (sumaArray(arreglo))

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

x= 20000

for i in range(1, x):
    holabb = random.randint(100, size=i)
    start_time = time.time()
    sumaArray(holabb)
    times.append(time.time() - start_time)
    
plot(times, x, "b")

