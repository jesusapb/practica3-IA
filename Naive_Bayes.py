from probabilidad_aposteriori import *

''' Esta clase toma las Datos base y aquellos A clasificar y se pasan a la 
clase a Decidir para clasificar cada unos de los individuos '''

class Naive_bayes:
    #se le pasa al constructor los Datos base y los datos A clasificar
    def __init__(self,Datos,A_Clasificar):
        self.Datos = Datos
        self.A_Clasificar = A_Clasificar
        self.Respuestas= []

    # En este metodo se clasifican los valores a clasificar
    def Clasificar(self):
        for i in self.A_Clasificar:
            tomar_decision = probabilidad_aposteriori(self.Datos,i)
            tomar_decision.Tomar_decision()
            #tomar_decision.impimirRespuestas()
            self.Respuestas.append(tomar_decision.Respuesta)


    # Este metodo es muy importante en el se imprimen los resultados
    def Resultados(self):
        print("Datos iniciales:",self.Datos)
        print("datos A clasificar:",self.A_Clasificar)
        print("Respuestas:", self.Respuestas)