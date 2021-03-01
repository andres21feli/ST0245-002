# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:56:28 2021

@author: Juank and Andres
"""

def fibonacci(n):

    if (n == 0):                               # c0
        return 0                               # c1

    elif (n == 1):                             # c3
        return 1                               # c4

    else:                                      # c5
        return fibonacci(n-1) + fibonacci(n-2) # T(n) = c6 + T(n-1) + T(n-2)

print(fibonacci(6))

#%%

def powerN(base,n,aux=1):
    if n == 0:                           # c0
        return aux                       # c1
    else:                                # c2
        return powerN(base,n-1,base*aux) # T(n) = c3 + T(n-1)

print(powerN(2,4))

#%%

def changeXY(string, auxstring = ''):
    if len(string) == 0:                                        # c0
        return auxstring                                        # c1
    elif string[len(string)-1] == 'x':                          # c2
        return changeXY(string[:len(string)-1],'y'+auxstring)   # T(n) = c3 + T(n-1)
    else:                                                       # c4
        return changeXY(string[:len(string)-1],string[len(string)-1]+auxstring) 
                                                                # T(n) = c5 + T(n-1)

print(changeXY('axhixb'))

#%%

def changePi(string, auxstring = ''):
    if len(string) == 0:                                            # c0
        return auxstring                                            # c1
    elif string[len(string)-2]+string[len(string)-1] == 'pi':       # c2
        return changePi(string[:len(string)-2],'3.14'+auxstring)    # T(n) = c3 + T(n-2)
    else:                                                           # c4
        return changePi(string[:len(string)-1],string[len(string)-1]+auxstring) 
                                                                    # T(n) = c5 + T(n-1)

print(changePi('pipiripi'))

#%%

def NoX(string, auxstring = ''):
    if len(string) == 0:                                                   # c0
        return auxstring                                                   # c1
    elif string[len(string)-1] == 'x':                                     # c2
        return NoX(string[:len(string)-1],''+auxstring)                    # T(n) = c3 + T(n-1)
    else:                                                                  # c4
        return NoX(string[:len(string)-1],string[len(string)-1]+auxstring) # T(n) = c5 + T(n-1)

print(NoX('xxh'))