import numpy as np

def suma_acumulativa():
    """Calcula la suma acumulativa del 0 al 10"""
    suma = np.sum(np.arange(0,11,1))
    return "{}".format(suma)

print(suma_acumulativa())