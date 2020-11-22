from conjuntos import *
from probabilidad import *
from sub_probabilidad import *
#from Naive_Bayes import *
from sub_probabilidad2 import *
from probablidad2 import *
from Decidir import *

#lista =[]

A = ["soleado", 36, "alta", "leve", False]
B = ["soleado", 28, "alta", "fuerte", False]
C = ["nublado", 30, "alta", "leve", True]
D = ["lluvioso", 20, "alta", "leve", True]
E = ["lluvioso", 2, "normal", "leve", True]
F = ["lluvioso", 5, "normal","fuerte",False]
G = ["lluvioso",11,"normal","fuerte", True]
H = ["soleado",22,"alta", "leve",False]
I = ["soleado",9,"normal","leve",True]
J = ["lluvioso", 17,"normal","leve", True]
K = ["soleado", 19,"normal","fuerte",True]
L = ["nublado", 22,"alta","fuerte",True]
M = ["nublado",27,"normal","leve",True]
N = ["lluvioso", 21,"alta","fuerte", False]

lista= [A,B,C,D,E,F,G,H,I,J,K,L,M,N]
#crear un metodo para mejorar la impresion
#print(lista)

NI1 = ["soleado", 19, "normal", "leve"]
NI2 = ["lluvioso", 34, "alta", "leve"]
NI3 = ["nublado", 14, "normal", "fuerte"]



#clasificar1 =conjuntos(lista)
#clasificar1.clasificar_conjuntos()
#clasificar1.imprimir_listas()


#proba = probabilidad(lista)
#proba.construir_listas()
#proba.calcular_probabilidad()



#print(NI1)
#print(NI2)

#indv = sub_probabilidad(lista,0,"soleado")
#indv.obtener_poblacion()


#decidir = Naive_bayes(lista)
#decidir.nuevoCalculo(NI1)


#verosimilitud = sub_probabilidad2(lista, 2,"alta")
#verosimilitud.obtener_poblaciones()
#verosimilitud.calcular_probabilidad()


decision = Decidir(lista,NI3)
decision.Tomar_decision()
