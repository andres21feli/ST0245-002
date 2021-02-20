# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:49:04 2021

@author: Andriu feat jk
"""
from IPython import get_ipython
get_ipython().magic('reset -sf') 

    
def max(arreglo):
    return arrayaux(arreglo,0)    
    
def arrayaux(arreglo,maxi):
    
    if len(arreglo) == 0:
        return maxi
    else:
        if arreglo[0] > maxi:
            return arrayaux(arreglo[1:],arreglo[0])
        else:
            return arrayaux(arreglo[1:],maxi)
        
# print(array([30,2,50,6]))

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

x= 100000

for i in range(1, x):
    start_time = time.time()
    # max(random.randint(1,10, size=random.randint(1,10)))
    max(random.randint(1,20, size=40))
    times.append(time.time() - start_time)
    
plot(times, x, "Addition")