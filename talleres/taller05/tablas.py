# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 11:51:45 2021

@author: User
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

import numpy as np

def tablas(n):
    tabla = np.zeros((n,n))
    for i in range(n):        
        for j in range(n):
            tabla[i,j]= (i+1)*(j+1)
    return tabla

# print(tablas(5))
            
import time
import matplotlib.pyplot as plt

def plot(times, n, lab):
    plt.xlabel('') 
    plt.ylabel('Time Complexity') 
    plt.plot(range(1, n), times, label = lab) 
    plt.grid() 
    plt.legend() 
    plt.show()

times = []

x= 500

for i in range(1, x):
    start_time = time.time()
    tablas(i)
    times.append(time.time() - start_time)
    
plot(times, x, "lol")
            
        
    