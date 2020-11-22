from conjuntos import *

class probabilidad:

    def __init__(self,datos):
        self.datos = datos
        self.prob_pronostico=[]
        self.prob_temperatatura = []
        self.prob_humedad= []
        self.prob_viento = []
        self.prob_asado = []
        #listas de valores
        self.pronostico = []
        self.temperatura = []
        self.humedad = []
        self.viento = []
        self.Asado =[]
        self.lista_pronostico = []
        self.lista_temperatura = []
        self.lista_humedad = []
        self.lista_viento = []
        self.lista_asado = []
        self.tama = len(self.datos)

    def construir_listas(self):
        for i in self.datos:
            self.lista_pronostico.append(i[0])
            self.lista_temperatura.append(i[1])
            self.lista_humedad.append(i[2])
            self.lista_viento.append(i[3])
            self.lista_asado.append(i[4])

    def calcular_probabilidad(self):
        clasificar = conjuntos(self.datos)
        clasificar.clasificar_conjuntos()
        #clasificar.imprimir_listas()
        self.pronostico= clasificar.pronostico
        self.temperatura = clasificar.temperatura
        self.humedad = clasificar.humedad
        self.viento = clasificar.viento
        self.Asado = clasificar.Asado

        for i in self.pronostico:
            self.prob_pronostico.append([i, self.lista_pronostico.count(i) / self.tama])
        self.prob_pronostico.sort()
        print(self.prob_pronostico)

        for i in self.temperatura:
            self.prob_temperatatura.append([i, self.lista_temperatura.count(i)/self.tama])

        self.prob_temperatatura.sort()
        print(self.prob_temperatatura)
        
        for i in self.humedad:
            self.prob_humedad.append([i, self.lista_humedad.count(i)/self.tama])

        self.prob_humedad.sort()
        print(self.prob_humedad)

        for i in self.viento:
            self.prob_viento.append([i,self.lista_viento.count(i)/ self.tama])
        self.prob_viento.sort()
        print(self.prob_viento)

        for i in self.Asado:
            self.prob_asado.append([i,self.lista_asado.count(i)/self.tama])
        print(self.prob_asado)






    def imprimir_probailidades(self):
        pass
