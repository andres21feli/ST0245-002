# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 07:26:01 2021

by andres21feli
"""
from IPython import get_ipython
get_ipython().magic('reset -sf') 

from time import time



def fibonacci(n):

    if (n == 0): 

        return 0

    elif (n == 1): 

        return 1

    else: 

        return fibonacci(n-1) + fibonacci(n-2)



inicio = time()
print(fibonacci(35))
fin = time()
total = fin-inicio
print(total)