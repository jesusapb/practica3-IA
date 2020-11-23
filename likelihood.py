''' En esta clase se calcula el likelihood de cada valor es el likelihood
de una hipótesis H dados los datos D,  es decir, la probabilidad
de obtener D dado que H es verdadera. '''

class likelihood:

    #se le pasa al constructor los datos, la posicion que ocupa la condicion
    # y el valor a comparar
    def __init__(self,datos,posicion,A_sacar):
        self.datos = datos
        self.A_sacar = A_sacar
        self.posicion= posicion
        self.poblacion_positiva= []
        self.poblacion_negativa =[]
        self.valores_si= 0
        self.valores_no = 0
        self.proba_si = 0
        self.proba_no = 0

# se optiene la poblacion que es positiva y la que es negativa
#se calcula aquellos que cumplen la condicion
    def obtener_poblaciones(self):
        for i in self.datos:
            if  i[4]== True:
                self.poblacion_positiva.append(i)
            else:
                self.poblacion_negativa.append(i)

        for i in self.poblacion_positiva:
            if i[self.posicion] == self.A_sacar:
                self.valores_si = self.valores_si + 1

        for i in self.poblacion_negativa:
            if i[self.posicion] == self.A_sacar:
                self.valores_no = self.valores_no + 1


    # En este metodo se vivide los individuos que pertenecen a la poblacion indicada
    # entre el numero de inviduos que cumplen la condicion
    def calcular_probabilidad(self):
        self.proba_si = self.valores_si /( len(self.poblacion_positiva))
        self.proba_no = self.valores_no / (len( self.poblacion_negativa))



    def imprimir_likelihood(self):
        print(len(self.poblacion_positiva))
        print(self.valores_si)
        print(self.proba_si)
        print(len(self.poblacion_negativa))
        print(self.valores_no)
        print(self.proba_no)
