

class conjuntos:


    def __init__(self,datos):
        self.datos = datos
        self.pronostico=[]
        self.temperatura=[]
        self.humedad = []
        self.viento = []
        self.Asado = []

    def clasificar_conjuntos(self):
        for i in self.datos:
            self.pronostico.append(i[0])
            self.temperatura.append(i[1])
            self.humedad.append(i[2])
            self.viento.append(i[3])
            self.Asado.append(i[4])

        self.pronostico = list(set(self.pronostico))
        self.temperatura = list(set(self.temperatura))
        self.humedad = list(set(self.humedad))
        self.viento = list(set(self.viento))
        self.Asado = list(set(self.Asado))


    def imprimir_listas(self):
        print(self.pronostico)
        print(self.temperatura)
        print(self.humedad)
        print(self.viento)