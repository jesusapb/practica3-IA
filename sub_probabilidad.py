'''
En esta clase se calcula la probabilidad condicional del evento que se busca
'''
class sub_probabilidad:

    def __init__(self,datos,posion,A_sacar):
        self.datos = datos
        self.A_sacar = A_sacar
        self.poblacion= []
        self.posicion = posion
        self.valores_si= 0
        self.valores_no = 0

    def obtener_poblacion(self):
        for i in self.datos:
            if self.A_sacar == i[self.posicion]:
                self.poblacion.append(i)

        for i in self.poblacion:
            if i[4]== True:
                self.valores_si = self.valores_si + 1
            else:
                self.valores_no = self.valores_no + 1

        print("valores si:",self.valores_si)
        print("valores no:",self.valores_no)


    def calcular_probabilidad(self):
        pass


