# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:17:37 2021

@author: Juank and Andres
"""
def formas(n):
    return formas_aux(n,0)


def formas_aux(n,formasn):      
    if n == 0:
        return formasn + 1
    elif n < 0:
        return 0
    else:
        return formas_aux(n-1,formasn) + formas_aux(n-2,formasn)

print(formas(8))