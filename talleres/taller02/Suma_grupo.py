# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:51:54 2021

by andres21feli and Jcgutierru
"""
from IPython import get_ipython
get_ipython().magic('reset -sf') 

def Suma_grupo(start, nums, target):
    if start >= len(nums):
        if target == 0:
            return True
        
        else:
            return False
    return Suma_grupo(start+1, nums, target) or Suma_grupo(start+1, nums, target-nums[start])

print(Suma_grupo(0,[2, 4, 8],10))
    