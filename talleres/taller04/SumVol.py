# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:02:27 2021

@author: El andriu y el jk
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')


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

def SumVol (start, Boxsizes , target):
    if start >= len(Boxsizes):
        if target == 0:
            return True
        else:
            return False
    return SumVol(start + 1, Boxsizes, target) or SumVol(start + 1, Boxsizes, target-Boxsizes[start])


times = []

for i in range(1, 1000):
    start_time = time.time()
    SumVol(0, random.randint(50, size=8), random.randint(50))
    times.append(time.time() - start_time)
    
plot(times, 1000, "Addition")