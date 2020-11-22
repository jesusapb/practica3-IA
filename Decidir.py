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

        #temperatura
        v_temperatura = sub_probabilidad2(self.datos,1,self.lugar_1)
        v_pronostico.obtener_poblaciones()
        v_pronostico.calcular_probabilidad()

        # Proba Humedad
        v_humedad = sub_probabilidad2(self.datos,2,self.lugar_2)
        v_humedad.obtener_poblaciones()
        v_humedad.calcular_probabilidad()

        #viento
        v_viento = sub_probabilidad2(self.datos,3,self.lugar_3)
        v_viento.obtener_poblaciones()
        v_viento.calcular_probabilidad()

        ##Casos positivos

        self.calculo_si = v_pronostico.proba_si * v_humedad.proba_si * v_viento.proba_si * self.proba_si

        ##Casos negativo
        self.calculo_no = v_pronostico.proba_no * v_humedad.proba_no * v_viento.proba_no * self.proba_no

        #If para saber que asignar
        if self.calculo_si > self.calculo_no:
            self.Respuesta =  True




    def impimirRespuestas(self):
        print(self.calculo_si)
        print(self.calculo_no)
        print(self.Respuesta)
