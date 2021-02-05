# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(Juan Camilo Gutierrez Urrego)s
201710009014
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

  
def subconjuntos(s):
    subconjuntosBase("", s)

def subconjuntosBase(base, t):
    
    if (len(t) == 0):
        print (base)
        return 
    
    else:
        return subconjuntosBase( base + t[0], t[1:]) or subconjuntosBase(base, t[1:])
        
    
print(subconjuntos("abc"))