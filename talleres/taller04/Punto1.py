# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 07:52:38 2021

by andres21feli
"""
from IPython import get_ipython
get_ipython().magic('reset -sf') 


def array(arreglo):
    return arrayaux(arreglo,0)
    
    
def arrayaux(arreglo,maxi):
    
    if len(arreglo) == 0:
        return maxi
    else:
        if arreglo[0] > maxi:
            return arrayaux(arreglo[1:],arreglo[0])
        else:
            return arrayaux(arreglo[1:],maxi)
        
print(array([30,2,50,6]))
        