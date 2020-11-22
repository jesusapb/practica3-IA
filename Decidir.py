from probabilidad import *
from probablidad2 import *
from sub_probabilidad2 import *
class Decidir:

    def __init__(self, datos, individuo):
        self.datos = datos
        self.individuo = individuo
        # print(self.individuo)

        self.calculo_si = 0
        self.calculo_no = 0

        self.lugar_0 = self.individuo[0]
        self.lugar_1 = self.individuo[1]
        self.lugar_2 = self.individuo[2]
        self.lugar_3 = self.individuo[3]

        proba= probabilidad2(datos)
        proba.sacar_probabilidad()
        self.proba_si = proba.proba_si
        self.proba_no= proba.proba_no

        self.Respuesta = False



    def CalcularProbabilidades(self,individuo):
        #print(self.datos)
        pass

        


    def Tomar_decision(self):

        #proba pronostico
        v_pronostico = sub_probabilidad2(self.datos,0,self.lugar_0)
        v_pronostico.obtener_poblaciones()
        v_pronostico.calcular_probabilidad()
        # Proba Humedad


        ##casos positivos
        self.calculo_si = v_pronostico.proba_si * self.proba_si

        ##casos negativo

        self.calculo_no = v_pronostico.proba_no * self.proba_no
        ##if para saber que asignar

        if self.calculo_si > self.calculo_no:
            self.Respuesta =  True

        print(self.calculo_si)
        print(self.calculo_no)
        print(self.Respuesta)


