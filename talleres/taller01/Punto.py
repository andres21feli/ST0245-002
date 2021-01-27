# -*- coding: utf-8 -*-
import math

class Punto2D():
    #"""Representacion de punto en 2 dimenciones"""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
      return self.__y

    def radio_polar(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def angulo_polar(self):
        return math.atan(self.__y/self.__x)
 

    def dist_euclidiana(self, x2, y2):
        self.__x2 = x2
        self.__y2 = y2
        return math.sqrt( pow((self.__x2-self.__x),2)+pow((self.__y2-self.__y),2));

Punto = Punto2D(10,20)
print(Punto.get_x())
print(Punto.get_y())
print(Punto.radio_polar())
print(Punto.angulo_polar())
print(Punto.dist_euclidiana(0,0))