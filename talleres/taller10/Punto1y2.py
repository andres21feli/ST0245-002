# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:53:05 2021

@author: Juan Camilo Gutierrez & Andres Felipe Agudelo
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')


class Nodo:
    def __init__(self,data):
        self.data = data
        self.derecha = None
        self.izquierda = None


class ArbolBinario:
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
            

    def buscar(self, data):   
        return self.buscar_aux(data, self.raiz)

    def buscar_aux(self, data, actual):
        if actual == None:
            return False
        elif data == actual.data:
            return True
        elif data < actual.data:
            return self.buscar_aux(data, actual.izquierda)
        else:
            return self.buscar_aux(data, actual.derecha)


    
    def dibujar(self):
        print('digraph G {')
        if self.raiz == None:
            return 'Nada que dibujar'
        else:
            self.dibujarAUX(self.raiz)
        print('}')
            
    def dibujarAUX(self, actual):
        if actual.izquierda != None:
            print(str(actual.data)+'->'+str(actual.izquierda.data)+';')        
        if actual.derecha != None:
            print(str(actual.data)+'->'+str(actual.derecha.data)+';')

        if actual.izquierda == None and actual.derecha == None:
            return
        
        elif actual.izquierda != None and actual.derecha != None:
            return self.dibujarAUX(actual.izquierda) or self.dibujarAUX(actual.derecha)

        else:
            if actual.izquierda != None:
                return self.dibujarAUX(actual.izquierda)
            elif actual.derecha != None:
                return self.dibujarAUX(actual.derecha)

ArbolEjemplo = ArbolBinario()
ArbolEjemplo.raiz
ArbolEjemplo.insertar(9)
ArbolEjemplo.insertar(6)
ArbolEjemplo.insertar(10)
ArbolEjemplo.insertar(11)
ArbolEjemplo.insertar(9.5)
ArbolEjemplo.insertar(3)
# ArbolEjemplo.raiz.izquierda.data
# ArbolEjemplo.raiz.derecha.derecha.data
# ArbolEjemplo.raiz.derecha.izquierda.data
# ArbolEjemplo.buscar(1)

ArbolEjemplo.dibujar()
# COPIAR Y PEGAR TEXTO PRINTEADO EN LA PAGINA: http://www.webgraphviz.com/

# Ambos algoritmos, tanto el de búsqueda como el de insertar, funcionan partiendo el arbol en dos,
# y trabajando unicamente con una de sus mitades, de modo que se esperaría un comportamiento de tipo
# O(log_2(n)), SIN EMBARGO, este comportamiento depende de que el arbol esté balanceado (no es el caso)
# por tanto, todos los valores pueden estar arrojados hacia un solo lado de éste, causando así que tanto
# para insertar un valor, como para buscarlo, en el peor de los casos se debe recorrer todo el arreglo de n
# términos hacia un lado. Como resultado, la complejidad en tiempo de nuestros algoritmos para un arbol 
# NO balanceado es de O(n), donde n es la cantidad de datos.