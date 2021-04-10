# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 12:38:30 2021

@author: Andres and Juank
"""
import numpy as np
class UnaTablaDeHash:
    def __init__(self):
        self.tabla = np.zeros(11460).astype(str)

    def funcionHash(self, k):
        key = 0
        for i in range(len(k)):
            key = (int(ord(k[i]))*i + key)%11460
        return key     
  
    def get(self, k):
        posicion = self.funcionHash(k)
        return self.tabla[posicion]
       
    def put(self, k,  v):
        posicion = self.funcionHash(k)
        self.tabla[posicion] = v

    def show(self):
        return self.tabla

    

tabla = UnaTablaDeHash()

archivo = open("usda-dc-directory.csv",'r') #NO uso C: ni D:
texto_en_string = archivo.read()
archivo.close()
lineas = texto_en_string.split("\n") # \n quiere decir salto de linea

aux = np.zeros(11460).astype(str)
cont = 0
for linea in lineas:
    columnas = linea.split(',')
    tabla.put(columnas[0]+' '+columnas[1],columnas[3])
    aux[cont] = columnas[0]+' '+columnas[1]
    cont = cont + 1

for key in aux:
      print(key,tabla.get(key))
