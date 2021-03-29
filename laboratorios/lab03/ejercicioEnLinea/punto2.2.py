# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:46:47 2021

@author: Juank and Andres
"""

class Node:
    def __init__(self,data=None):
        self.data = data
        self.nxt = None

    def __str__(self):
        return "" + str(self.data)

class Lsimple:
    def __init__(self):
        self.first_Node = None
        self.last_Node = None


    def insert_text(self, text):
        aux = 1
        for i in text:
            NodoNuevo = Node(i)
            if i == '[':
                aux = 2

            elif i == ']':
                aux = 1

            elif self.first_Node == None:
                self.first_Node = NodoNuevo
                self.last_Node = NodoNuevo


            elif aux == 1:                             
                self.last_Node.nxt = NodoNuevo
                self.last_Node = NodoNuevo

            elif aux == 2:
                NodoNuevo.nxt = self.first_Node
                self.first_Node = NodoNuevo
                aux = 3
                indx = 0
            
            elif aux == 3:                     
                aux_node = self.first_Node
                for j in range(0,indx):
                    aux_node = aux_node.nxt

                NodoNuevo.nxt = aux_node.nxt
                aux_node.nxt = NodoNuevo
                indx = indx + 1
            


    def print_l(self):
        if self.first_Node != None:
            linked_list = ''
            current = self.first_Node
            linked_list = linked_list + current.data 
            while current.nxt != None:
                current = current.nxt
                linked_list = linked_list + current.data   
            return linked_list



text = Lsimple()
text.insert_text('[[a[[d[f[[g[g[h[h[dgd[fgsfa[f')
print(text.print_l())
