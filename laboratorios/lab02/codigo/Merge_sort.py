# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:59:47 2021

@author: Andres and Juank
"""
def mergesort(a):                                 
    if len(a) == 1:                          
        return a  
    mid = len(a)//2       
    arrayo = a[:mid]
    arrayt = a[mid:]     
    arrayo = mergesort(arrayo)                   
    arrayt = mergesort(arrayt)                    
    return (merge(arrayo,arrayt,a))                
    
def merge(arrayO,arrayT,a):                         
    i = j = k = 0                      
    while len(arrayO) >j and len(arrayT) > i:    
        if arrayO[j] > arrayT[i]:              
            a[k]= arrayT[i]  
            i = i + 1              
        else:              
            a[k] = arrayO[j]  
            j = j + 1                   
        k = k + 1
    while len(arrayO) >j :                    
        a[k] = arrayO[j]    
        j = j + 1
        k = k + 1                        
    while len(arrayT) > i:                     
        a[k] = arrayT[i]    
        i = i + 1
        k = k + 1                     
    return a   

print(mergesort([2, 1, 5, 9, 0, 50, 10, 3, 89, 0]))                        
