# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:54:26 2021

@author: Andres and Juank
"""
 
from collections import deque

def solvecal(elements):
    operators = '+-*/'
    elements = elements.split(' ')
    aList = deque([])
    for t in elements:
        if not t in operators:
            aList.appendleft(t)

        else:
            a = int(aList[0])
            aList.popleft()
            b = int(aList[0])
            aList.popleft()

            inde = operators.index(t)
            if inde == 0:
                aList.appendleft(str(a+b))

            elif inde == 1:
                aList.appendleft(str(b-a))

            elif inde == 2:
                aList.appendleft(str(a*b))

            else:
                aList.appendleft(str(b/a))

    last = aList[0]
    return last

a = '6 60 + 8 *'
print(solvecal(a))
