
class probabilidad2:

    def __init__(self,datos):
        self.datos = datos
        self.proba_si = 0
        self.proba_no = 0
        self.tama = len(self.datos)


    def sacar_probabilidad(self):
        contador_si = 0
        contador_no = 0
        for i in self.datos:
            if i[4] == True:
                contador_si = contador_si + 1
            else:
                contador_no = contador_no + 1

        #print(contador_si)
        self.proba_si = contador_si/ self.tama
        #print(self.proba_si)
        #print(contador_no)
        self.proba_no = contador_no / self.tama
        #print(self.proba_no)

    def imprimir_probabilidad(self):
        print(self.proba_si)
        print(self.proba_no)
