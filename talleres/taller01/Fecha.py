import math

class Fecha():

    def __init__(self, dia, mes, anyo):
        self.__dia = dia
        self.__mes = mes
        self.__anyo = str(anyo)

        if self.__dia < 10:
            self.__dia = str(self.__dia)
            self.__dia = self.__dia.zfill(2)
        else:
            self.__dia = str(self.__dia)
        
        if self.__mes < 10:
            self.__mes = str(self.__mes)
            self.__mes = self.__mes.zfill(2)
        else:
          self.__mes = str(self.__mes)

        self.__array_fecha = [self.__anyo,self.__mes,self.__dia]

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
        self.__anyo2 = str(anyo2)

        if self.__dia2 < 10:
            self.__dia2 = str(self.__dia2)
            self.__dia2 = self.__dia2.zfill(2)
        else:
            self.__dia2 = str(self.__dia2)
        
        if self.__mes2 < 10:
            self.__mes2 = str(self.__mes2)
            self.__mes2 = self.__mes2.zfill(2)
        else:
          self.__mes2 = str(self.__mes2)

        self.__array_fecha2 = [self.__anyo2,self.__mes2,self.__dia2]
        self.fecha_concatenada2 = int(''.join(self.__array_fecha2))
        if self.fecha_concatenada < self.fecha_concatenada2:
            return -1
        
        elif self.fecha_concatenada == self.fecha_concatenada2:
            return 0

        elif self.fecha_concatenada > self.fecha_concatenada2:
            return 1

Dia_hora_anyo = Fecha(21,3,2000)
print(Dia_hora_anyo.get_dia())
print(Dia_hora_anyo.get_mes())
print(Dia_hora_anyo.get_anyo())
print(Dia_hora_anyo.fecha_num())
print(Dia_hora_anyo.comparar(1,2,2000))