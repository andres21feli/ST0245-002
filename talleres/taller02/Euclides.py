# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:37:00 2021

by andres21feli and Jcgutierru
"""
from IPython import get_ipython
get_ipython().magic('reset -sf') 

def Euclides_Algoritmo(m,n):
    if m < n:
        temp = n
        n = m
        m = temp
    if m%n == 0:
        return (n)
    # else:
    return Euclides_Algoritmo(n, m%n)

print(Euclides_Algoritmo(150, 39))