# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 21:39:22 2021

@author: Andres and Juank
"""

import matplotlib.pyplot as plt

class vertices:
    def __init__(self,ide,x,y,name):
        self.ide = ide
        self.x = x
        self.y = y
        self.name = name
    def __str__(self):
        return "" + str(self.ide)

    def plotvertices(self):
        fig = plt.figure
        plt.plot(self.x,self.y, marker="o", color="blue")
        plt.text(self.x,self.y,self.name)
        

class arcos:
    def __init__(self,ide1,ide2,dist,name,v):
        self.ide1 = ide1
        self.ide2 = ide2
        self.dist = dist
        self.name = name

    def linea2D(self):
        xvalues = [v1.x,v2.x]
        yvalues = [v1.y,v2.y]
        xprom = (v2.x-v1.x)/2
        yprom = (v2.y-v1.y)/2
        plt.text(xprom,yprom,self.name)
        plt.plot(xvalues,yvalues)

def linea2D(v1,v2,name):
    xvalues = [v1.x,v2.x]
    yvalues = [v1.y,v2.y]
    xprom = (v2.x+v1.x)/2
    yprom = (v2.y+v1.y)/2
    plt.text(xprom,yprom,name)
    plt.plot(xvalues,yvalues)


file = open('medellin_pequeno.txt','r')
complt_file = file.readlines()

split_file=[]
for i in range(0,len(complt_file)-1):
    split_file = split_file + [0]


for i in range(1,len(complt_file)):
    split_file[i-1] = complt_file[i].split(' ')

######################################################################################################
v=[]
i=0
while split_file[i][0] != '\n':
    v = v + [vertices(split_file[i][0],float(split_file[i][1]),float(split_file[i][2]),split_file[i][3])]
    i=i+1


a= []
for j in range(i+2,len(split_file)):
    a = a +[arcos(split_file[j][0],float(split_file[j][1]),float(split_file[j][2]),split_file[j][3],v)]

for i in v:   
    # print(i.ide)
    i.plotvertices()

for i in a:
    for j in v:
        if int(j.ide) == int(i.ide1):
            vertia = j
        if int(j.ide) == int(i.ide2):
            vertib = j
             
    linea2D(vertia,vertib,i.name)

