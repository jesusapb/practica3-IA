from conjuntos import *
from probabilidad import *
#lista =[]

A = ["soleado", 36, "alta", "leve", False]
B = ["soleado", 28, "alta", "fuerte", False]
C = ["nublado", 30, "alta", "leve", True]
D = ["lluvioso", 20, "alta", "leve", True]
E = ["lluvioso", 2, "normal", "leve", True]
F = ["lluvioso", 5, "normal","fuerte",True]
G = ["lluvioso",11,"normal","fuerte", True]
#H = ["lluvioso",11,"normal","fuerte",True]
I = ["soleado",22,"alta", "leve", True]
J = ["soleado",9,"normal","leve",True]
K = ["lluvioso", 17,"normal","leve", True]
L = ["soleado", 19,"normal","fuerte",True]
M = ["nublado", 22,"alta","fuerte",True]
N = ["nublado",27,"normal","leve",True]
O = ["lluvioso", 21,"alta","fuerte", False]

lista= [A,B,C,D,E,F,G,I,J,K,L,M,N,O]
#crear un metodo para mejorar la impresion
#print(lista)


#clasificar = conjutos(lista)
#clasificar.clasificar_conjuntos()
#clasificar.imprimir_listas()


proba = probabilidad(lista)
proba.calcular_probabilidad()

