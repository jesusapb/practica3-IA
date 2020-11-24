from Naive_Bayes import *

A = ["soleado", 36, "alta", "leve", "No"]
B = ["soleado", 28, "alta", "fuerte", "No"]
C = ["nublado", 30, "alta", "leve", "Si"]
D = ["lluvioso", 20, "alta", "leve", "Si"]
E = ["lluvioso", 2, "normal", "leve", "Si"]
F = ["lluvioso", 5, "normal","fuerte","No"]
G = ["lluvioso",11,"normal","fuerte", "Si"]
H = ["soleado",22,"alta", "leve","No"]
I = ["soleado",9,"normal","leve","Si"]
J = ["lluvioso", 17,"normal","leve", "Si"]
K = ["soleado", 19,"normal","fuerte","Si"]
L = ["nublado", 22,"alta","fuerte","Si"]
M = ["nublado",27,"normal","leve","Si"]
N = ["lluvioso", 21,"alta","fuerte", "No"]
#Lista de los Datos preliminares
Datos= [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

NI1 = ["soleado", 19, "normal", "leve"]
NI2 = ["lluvioso", 34, "alta", "leve"]
NI3 = ["nublado", 14, "normal", "fuerte"]
#Lista de los datos A_clasificar
A_Clasificar = [NI1,NI2,NI3]

if  __name__ ==  '__main__':
    '''Se instancia la clase Naive_bayes y la constructor se le pasan dos
     parametros, la lista de datos preliminares y los datos A_Clasificar'''
    tomar_decision = Naive_bayes(Datos,A_Clasificar)
    tomar_decision.Clasificar()
    tomar_decision.Resultados()
