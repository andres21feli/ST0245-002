# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:19:03 2021

@author: Juan Camilo Gutierrez & Andres Felipe Agudelo
"""
from IPython import get_ipython;   
get_ipython().magic('reset -sf')

class Nodo():
    def __init__(self, obj=None, nxt = None):
        self.obj = obj # Nombre de mi Nodo (a la vez el 'dato')
        self.nxt = nxt # Nombre del Nodo siguiente

    def __str__(self):
        return "" + str(self.obj)

class Lsimple():
    def __init__(self):
        self.first_Node = None
        self.last_Node = None
        self.size = 0

    def insert(self, element, indx ):
        NodoNuevo = Nodo(element)
        if self.first_Node == None:
           self.first_Node = NodoNuevo
           self.last_Node = NodoNuevo
        elif indx == 0:          # Establecer posicion de head
            NodoNuevo.nxt = self.first_Node
            self.first_Node = NodoNuevo
            
            # NodoNuevo.indx = indx
        elif indx >= self.size-1:   # Establecer posicion de tail
            self.last_Node.nxt = NodoNuevo
            self.last_Node = NodoNuevo
            
        elif indx > 0 and indx < self.size: # Establecer poscicion entre head y tail
            aux_node = self.first_Node
            for i in range(0,indx-1):
                aux_node = aux_node.nxt

            NodoNuevo.nxt = aux_node.nxt
            aux_node.nxt = NodoNuevo
            
        self.size = self.size + 1    
        

    def get_size(self):
        return self.size

    def remove(self, indx):
        if self.first_Node == None:
            return None
        
        elif self.size == 1:
            self.first_Node = None
            self.last_Node = None
            self.size =0
            return None

        elif indx == 0:
            self.first_Node = self.first_Node.nxt
            self.size = self.size - 1 

        elif indx >= self.size-1: 
            current = self.first_Node
            while current.nxt.nxt != None:
                current = current.nxt
            self.last_Node = current
            current.nxt = None
            self.size = self.size - 1   

        elif indx > 0 and indx < self.size: # Establecer poscicion entre head y tail
            aux_node = self.first_Node
            for i in range(0,indx-1):
                aux_node = aux_node.nxt
            aux_node.nxt=aux_node.nxt.nxt
            self.size = self.size - 1 


    def search(self, element):
        if self.size == 0:
            return None

        auxnode = self.first_Node
        aux = 0
        while auxnode.obj != element and aux < self.size-1:
            auxnode = auxnode.nxt
            aux = aux + 1
        if auxnode.obj == element:
            return (aux)
        else:
            return (None)


    def print_l(self):
        if self.first_Node != None:
            linked_list = []
            current = self.first_Node
            linked_list = linked_list + [int(current.obj)] 
            while current.nxt != None:
                current = current.nxt
                linked_list = linked_list + [int(current.obj)]   
            return linked_list

lista1 = Lsimple()
lista1.insert(4,0)
lista1.insert(5,0)
lista1.insert(7,1)
lista1.insert(8,1)
lista1.insert(10,2)
lista1.remove(3)
lista1.remove(3)
lista1.remove(2)
# lista1.remove(400)
# lista1.remove(4)


print('cabeza es: ',lista1.first_Node)
print('cola es: ',lista1.last_Node)
print('tamaño es: ',lista1.get_size())
print('LinkedList es: ',lista1.print_l())
print(lista1.search(8))