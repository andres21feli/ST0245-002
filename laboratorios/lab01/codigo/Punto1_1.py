# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 21:16:26 2021

@author: Andres and Juank
"""
import numpy as np

def lcs(cadenaA ,cadenaB ):   
    return lcs_aux(cadenaA,cadenaB,len(cadenaA),len(cadenaB),np.zeros((len(cadenaA)+1,len(cadenaB)+1)))
        
def lcs_aux(cadenaA ,cadenaB ,m ,n ,T):
    for i in range(m):                          # C1*m
        for j in range(n):                      # C2(n*m)
            if cadenaA[i] == cadenaB[j]:        # C3(n*m)
                T[i][j] = T[i-1][j-1]+1         # (C3+C4)(n*m)
            else:                               # C5(n*m)
                T[i][j] = max(T[i-1][j],T[i][j-1]) # (C5+C6)(n*m)
    return (np.amax(T))                       # C7


numero_n_datos = 1000
datos = open("Acipenser transmontanus mitochondrial DNA.txt", "r")
archivo = datos.readlines()
X = archivo[0][:numero_n_datos]

datos2 = open("Anser albifrons mitochondrion DNA.txt", "r")
archivo2 = datos2.readlines()
Y = archivo2[0][:numero_n_datos]


print(lcs(X,Y))   

