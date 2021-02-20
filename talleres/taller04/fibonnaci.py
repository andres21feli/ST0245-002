# -*- coding: utf-8 -*-

from IPython import get_ipython
get_ipython().magic('reset -sf') 

def fibonacci(n):

    if (n == 0): 
        return 0

    elif (n == 1): 
        return 1

    else: 
        return fibonacci(n-1) + fibonacci(n-2)

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

x= 35

for i in range(1, x):
    start_time = time.time()
    fibonacci(i)
    times.append(time.time() - start_time)
    
plot(times, x, "Addition")