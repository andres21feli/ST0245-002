# -*- coding: utf-8 -*-
import math

class Punto2D():
    #"""Representacion de punto en 2 dimenciones"""

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return __x

    def get_y(self):
      return __y

    def radio_polar(self):
        return math.sqrt(x**2 + y**2)

    def angulo_polar(self):
        return math.atan(y/x)
 

    def dist_euclidiana(self, other):
        x2 = other.x
        y2 = other.y
        return math.sqrt( pow((x2-x),2)+pow((y2-y),2));

class Fecha():

    def __init__(self, dia, mes, anyo):
        self.__dia = dia
        self.__mes = mes
        self.__anno = anyo

    def get_dia(self):
        return __dia

    def get_mes(self):
        return __mes

    def get_anyo(self):
        return __anyo
