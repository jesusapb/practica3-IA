from Decidir import *


class Naive_bayes:

    def __init__(self,Datos,A_Clasificar):
        self.Datos = Datos
        self.A_Clasificar = A_Clasificar
        self.Respuestas= []


    def tomar_decisiones(self):
        #print(self.Datos)
        #print(self.A_Clasificar)

        for i in self.A_Clasificar:

            tomar_decision = Decidir(self.Datos,i)
            tomar_decision.Tomar_decision()
            self.Respuestas.append(tomar_decision.Respuesta)
            #print(i)

        print(self.Datos)
        print(self.A_Clasificar)
        print("Respuestas: ",self.Respuestas)
        #pass


