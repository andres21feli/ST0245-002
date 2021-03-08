# -*- coding: utf-8 -*-
"""

@author: Andres and Juank
"""

import numpy as np

class MiArrayList():

    def __init__(self,DEFAULT_CAPACITY = 4):
        self.size = 0
        self.elements = np.zeros(DEFAULT_CAPACITY)
    
    def get_size(self):
        return self.size

    def capacity(self):
        return self.elements.size
    
    def add(self, e):
        if self.size == self.capacity():
           nuevo = np.zeros(int(self.capacity()*2)+1)
           for i in range(0, self.capacity()): # O(n)
              nuevo[i] = self.elements[i]  # O(n)
           self.elements = nuevo
        self.elements[self.size] = e
        self.size = self.size + 1
        # T(n) es O(n) en el peor caso, que es cuando está lleno
 
    def get(self, i):
        return self.elements
    
 
    def addInIndex(self, index, e):

        if self.size == self.capacity():                   # Si el arreglo excederá la capacidad
            nuevo = np.zeros(int(self.capacity()*2)+1)       
            for i in range(0, self.capacity()): # O(n)
              nuevo[i] = self.elements[i]  # O(n)
            self.elements = nuevo
            if index <= self.get_size()-1:                   # Si el index está adentro del tamaño
                for i in range (self.get_size(),index, -1):                 
                    self.elements[i] = self.elements[i-1]
            self.elements[index] = e        

        elif index <= self.get_size()-1:                 # el index está dentro del tamaño del arreglo 
            for i in range (self.get_size(),index, -1): 
                self.elements[i] = self.elements[i-1]
            self.elements[index] = e    

        elif index > self.get_size()-1 and self.capacity() > self.get_size(): # el index y la capacidad 
            self.elements[self.get_size()] = e                                # son mayores que el tamaño      
        self.size = self.size + 1


    def TrimToSize(self):
        self.elements = self.elements[:self.get_size()]


    def delete(self):
        self.elements[self.get_size()-1] = 0
        self.size = self.size -1

    def deleteInIndex(self, index):
        self.elements[index: self.get_size()-index-1] = self.elements[index+1: self.get_size()-index]
        self.elements[self.get_size()-1] = 0
        self.size = self.size -1