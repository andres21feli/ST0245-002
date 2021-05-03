# -*- coding: utf-8 -*-
"""
Created on Sun May  2 21:10:35 2021

@author: Andres and Juankas
"""
class Nodo:
    def __init__(self,data):
        self.data = data
        self.izquierda = None
        self.derecha = None

class Arbol_binario:
    def __init__(self):
        self.raiz = None

    def insertar(self, data):
        if self.raiz is None:
            self.raiz = Nodo(data)
        else:
            self.insertar_aux(data, self.raiz)

    def insertar_aux(self, data, actual):
        if data < actual.data:
            if actual.izquierda == None:
                actual.izquierda = Nodo(data)
            else:
                self.insertar_aux(data,actual.izquierda)

        else:
            if actual.derecha == None:
                actual.derecha = Nodo(data)
            else:
                self.insertar_aux(data,actual.derecha)

    def Pos_orden(self,lista):
        for i in lista:
            self.insertar(i)

        self.print_nums(self.raiz)
        
    def print_nums(self,raiz):
        
        if raiz != None:
            self.print_nums(raiz.izquierda) 
            self.print_nums(raiz.derecha) 
            print(raiz.data) 
            
ArbolB = Arbol_binario()
input_data = [50,30,24,5,28,45,98,52,60]
ArbolB.Pos_orden(input_data)
