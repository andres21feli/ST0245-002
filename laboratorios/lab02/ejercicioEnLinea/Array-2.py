# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:09:19 2021

@author: Juan Camilo Gutierrez y Andres Felipe Agudelo
"""


def sum13(array):                                          # C0
    if len(array) == 0:                                    # C1
        return 0                                           # C2
    suma=0                                                 # C3

    i = 0                                                  # C4
    while i < len(array):                                  # C5 * n
        if array[i] != 13:                                 # C6 * n
            suma = suma + array[i]                         # C7 * n
        elif array[i] == 13 and i != len(array):           # C8 * n
            i = i + 1                                      # C9 * n
        i = i+1                                            # C10 * n
 
    return suma                                            # C11

#%%
def only14(array):                                 # C0
    if len(array) == 0:                            # C1
        r = False                                  # C2
    else:                                          # C3
        r = True                                   # C4
         
    for i in range(len(array)):                    # C5 * n
        if (array[i] != 1) and (array[i] != 4):    # C6 * n
            r = False                              # C7 * n
    return r                                       # C8


#%%
def sameEnds(array, n):                               # C0
    ArrayIn = []                                      # C1
    ArrayFin = []                                     # C2
    for i in range(n):                                # C3 * n
        ArrayIn = ArrayIn + [array[i]]                # C3 * n
        ArrayFin = [array[len(array)-1-i]] + ArrayFin # C4 * n

    if ArrayIn == ArrayFin:                           # C7
        return True                                   # C8
    else:                                             # C9
        return False                                  # C10

#%%
def fizzArray(n):                   # C0
    result=[]                       # C1
    for i in range(n):              # C2 * n
        result = result + [i]       # C3 * n
    return result                   # C4

#%%
def fizzArray3(init, n):            # C0      
    result=[]                       # C1
    for i in range(init,n):         # C2 * n
        result = result + [i]       # C3 * n
    return result                   # C4

#%%
def has22(array):                                # C0 
    r = False                                    # C1
    for i in range(len(array)-1):                # C2 * n
        if array[i] == 2 and array[i+1] == 2:    # C3 * n
            r = True                             # C4 * n
    return r                                     # C5

