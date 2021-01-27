import math

class Fecha():

    def __init__(self, dia, mes, anyo):
        self.__dia = dia
        self.__mes = mes
        self.__anyo = anyo
        self.__array_fecha = [str(self.__anyo),str(self.__mes),str(self.__dia)]

    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def get_anyo(self):
        return self.__anyo

    def fecha_num(self):
        self.fecha_concatenada = int(''.join(self.__array_fecha))
        return self.fecha_concatenada

    def comparar(self, dia2, mes2, anyo2):
        self.__dia2 = dia2
        self.__mes2 = mes2
        self.__anyo2 = anyo2
        self.__array_fecha2 = [str(self.__anyo2),str(self.__mes2),str(self.__dia2)]
        self.fecha_concatenada2 = int(''.join(self.__array_fecha2))
        if self.fecha_concatenada < self.fecha_concatenada2:
            return -1
        
        elif self.fecha_concatenada == self.fecha_concatenada2:
            return 0

        elif self.fecha_concatenada > self.fecha_concatenada2:
            return 1

Dia_hora_anyo = Fecha(21,1,2000)
print(Dia_hora_anyo.get_dia())
print(Dia_hora_anyo.get_mes())
print(Dia_hora_anyo.get_anyo())
print(Dia_hora_anyo.fecha_num())
print(Dia_hora_anyo.comparar(1,2,2000))