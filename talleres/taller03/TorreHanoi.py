# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:46:21 2021

@author: User
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

def hanoi(topN, o = "Torre1", a = "Torre2", d = "Torre3"):
    if topN == 1:
        print ('mover un disco de la ' + o + ' a la ' + d)
    else:
        hanoi(topN-1, o, d, a)
        print ('mover un disco de la ' + o + ' a la ' + d)
        hanoi(topN-1, a, o, d)
        
print(hanoi(3))
