# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 18:59:22 2021

@author: Andres and Juank
"""
def maxSpan(array):                                       # C0
    spanF=0                                               # C1
    for i in range(len(array)):                           # C2 * n
        for j in range(len(array)):                       # C3 * n * n
            if array[i] == array[len(array)-1-j]:         # C4 * n^2
                span = len(array)-j-i                     # C5 * n^2
                spanF = max(span,spanF)                   # C6 * n^2
    return spanF                                          # C7


def fix34(array):                                      # C0
    j = 0                                              # C1
    for i in range(len(array)):                        # C2 * n
        if array[i] == 3:                              # C3 * n
            aux = 0                                    # C4 * n
            while j <= len(array) and aux <1:          # C5 * n * n
                if array[j] == 4:                      # C6 * n^2
                    array[j] = array[i+1]              # C7 * n^2
                    array[i+1] = 4                     # C8 * n^2
                    aux = aux + 1                      # C9 * n^2
                    auxj = j+1                         # C10 * n^2
                j = j + 1                              # C11 * n^2
            j = auxj                                   # C12 * n
    return array                                       # C13 



def fix45(array):                                     # C0
    j = 0                                             # C1
    for i in range(len(array)):                       # C2 * n
        if array[i] == 4:                             # C3 * n
            aux = 0                                   # C4 * n
            while j <= len(array) and aux <1:         # C5 * n * n
                if array[j] == 5:                     # C6 * n^2
                    array[j] = array[i+1]             # C7 * n^2
                    array[i+1] = 5                    # C8 * n^2
                    aux = aux + 1                     # C9 * n^2
                    auxj = i+2                        # C10 * n^2
                j = j + 1                             # C11 * n^2
            j = auxj                                  # C12 * n
    return array                                      # C13 



def squareUp(n):                                      # C0
    square = []                                       # C1
    for i in range(n,0,-1):                           # C2 * n
        for j in range(1,n+1):                        # C3 * n * n
            if j <= i:                                # C4 * n^2
                square = [j] + square                 # C5 * n^2
            elif j > i:                               # C6 * n^2
                square = [0] + square                 # C7 * n^2
    return square                                     # C8


def canBalance(array):                                # C0
    if len(array) <= 1:                               # C1
        return False                                  # C2
    for i in range(1,len(array)):                     # C3 * n
        arrayOne = array[0:i]                         # C4 * n
        arrayTwo = array[i:]                          # C5 * n
        sumOne = sum(arrayOne)                        # C6 * n
        sumTwo = sum(arrayTwo)                        # C7 * n
        if sumOne == sumTwo:                          # C8 * n
            return True                               # C9 * n
    if sumOne != sumTwo:                              # C10
        return False                                  # C11
