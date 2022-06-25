import random

listaval = []

def genrnd(num_inf, num_sup, cant_numeros):
    num_aleatorio = 0 

    for i in range(cant_numeros):
      num_aleatorio = random.randrange(num_inf, num_sup, 1)
      listaval.append(num_aleatorio)
    return listaval

genrnd(1, 500, 50)