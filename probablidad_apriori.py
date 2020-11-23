'''En esta clase se calcula la probabilidad a priori, la cual es la forma de
introducir conocimiento previo sobre los valores que puede tomar la hipótesis.'''

class probabilidad_apriori:

    # Al constructor se le pasan los datos
    def __init__(self,datos):
        self.datos = datos
        self.proba_si = 0
        self.proba_no = 0
        self.tama = len(self.datos)


    ''' se saca la probabilidad, primero contando cuantos valores son
    positivos y cuantos son negativos, acontinuacion se divide cada uno
    entre el tamaño de la poblacion para obtener las probilidades '''
    def sacar_probabilidad(self):
        contador_si = 0
        contador_no = 0
        for i in self.datos:
            if i[4] == True:
                contador_si = contador_si + 1
            else:
                contador_no = contador_no + 1

        self.proba_si = contador_si / self.tama
        self.proba_no = contador_no / self.tama

    # Este metodo fue una forma de rastrear los resultados
    def imprimir_probabilidad(self):
        print(self.proba_si)
        print(self.proba_no)
