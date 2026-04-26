import random
def rolar_dados (Ndados):
    resultado = []
    a = 0
    i=0
    while i < Ndados:
        a = random.randint(1,6)
        resultado.append(a)
        i = i+1
    return resultado

