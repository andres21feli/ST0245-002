import math
import matplotlib.pyplot as plt

class Line():

    def __init__(self, x1, x2, y1, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__listax = []
        self.__listay = []

    def puntos_intermediosx(self):
        for i in range(self.__x1,self.__x2+1):
            self.__listax.append(i)

        return self.__listax

    def puntos_intermediosy(self):
        for j in range(self.__y1, self.__y2+1):
            self.__listay.append(j)

        return self.__listay

Linea = Line(0,3,0,3)   
print(Linea.puntos_intermediosx())
print(Linea.puntos_intermediosy())

plt.plot(Linea.puntos_intermediosx(),Linea.puntos_intermediosy())
plt.show()