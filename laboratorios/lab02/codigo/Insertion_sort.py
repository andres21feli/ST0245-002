# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:57:02 2021

@author: Juank and Andres
"""
def Insertion_Sort(arreglo):
    for i in range(len(arreglo)-1): # n +c0
        j = i # c1
        while arreglo[j+1] < arreglo[j] and j>-1:  # n  
            aux = arreglo[j] # c3
            arreglo[j] = arreglo[j+1] # c4
            arreglo[j+1] = aux # c5
            j = j-1 # c6
    return arreglo # c7

print(Insertion_Sort([2, 1, 5, 9, 0, 50, 10, 3, 89, 0]))
