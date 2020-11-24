from probablidad_apriori import *
from likelihood import *

''' En esta clase se calcula la probabalidad a posteriori,
la distribución de probabilidad final para la hipótesis.
Es la consecuencia lógica de haber usado un conjunto de datos, un likelihood y un a priori '''

class probabilidad_aposteriori:

    # se le pasa al contructor los datos de aprendizaje y el individuo que sera clasificado
    def __init__(self, datos, individuo):
        self.datos = datos
        self.individuo = individuo
        self.calculo_si = 0
        self.calculo_no = 0
        self.lugar_0 = self.individuo[0]
        self.lugar_1 = self.individuo[1]
        self.lugar_2 = self.individuo[2]
        self.lugar_3 = self.individuo[3]
        proba= probabilidad_apriori(datos)
        proba.sacar_probabilidad()
        self.proba_si = proba.proba_si
        self.proba_no= proba.proba_no
        self.Respuesta = "No"


    ''' En esta clase se toma la decision de cual probabalidad es mas grande, primero se
        saca el likelihood por para cada elemento del individuo, luego se multiplican segun
        corresponda si son positivos o negativos, acontinuacion se comparan para saber cual
         es mas grande y se hace la asignacion '''
    def Tomar_decision(self):

        #Pronostico
        v_pronostico = likelihood(self.datos,0,self.lugar_0)
        v_pronostico.obtener_poblaciones()
        v_pronostico.calcular_probabilidad()

        #Temperatura
        v_temperatura = likelihood(self.datos,1,self.lugar_1)
        v_temperatura.obtener_poblaciones()
        v_temperatura.calcular_probabilidad()

        #Humedad
        v_humedad = likelihood(self.datos,2,self.lugar_2)
        v_humedad.obtener_poblaciones()
        v_humedad.calcular_probabilidad()

        #viento
        v_viento = likelihood(self.datos,3,self.lugar_3)
        v_viento.obtener_poblaciones()
        v_viento.calcular_probabilidad()

        ##Casos positivos
        #self.calculo_si = v_pronostico.proba_si * v_humedad.proba_si * v_viento.proba_si * self.proba_si
        self.calculo_si = v_pronostico.proba_si *v_temperatura.proba_si * v_humedad.proba_si * v_viento.proba_si * self.proba_si

        ##Casos negativo
        #self.calculo_no = v_pronostico.proba_no * v_humedad.proba_no * v_viento.proba_no * self.proba_no
        self.calculo_no = v_pronostico.proba_no * v_temperatura.proba_no * v_humedad.proba_no * v_viento.proba_no * self.proba_no

        #If para saber que asignar
        if self.calculo_si >= self.calculo_no:
            self.Respuesta = "Si"


    # Este metodo fue una forma de rastrear los resultados antes de la comparacion para verificar
    def impimirRespuestas(self):
        print(self.calculo_si)
        print(self.calculo_no)
        print(self.Respuesta)
