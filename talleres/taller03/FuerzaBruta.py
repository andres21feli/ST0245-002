# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 09:48:29 2021

@author: User
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')


def subset(s, base = ""):
    if len (s) == 0:
        print (base)
    else:
        for i in range(len(s)):
            subset(s[:i]+s[i+1:], base+s[i])
        
subset("abcd")
