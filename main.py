from Naive_Bayes import *

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

Datos= [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

NI1 = ["soleado", 19, "normal", "leve"]
NI2 = ["lluvioso", 34, "alta", "leve"]
NI3 = ["nublado", 14, "normal", "fuerte"]

A_Clasificar = [NI1,NI2,NI3]

if  __name__ ==  '__main__':
    tomar_decision = Naive_bayes(Datos,A_Clasificar)
    tomar_decision.Clasificar()
    tomar_decision.Resultados()