import numpy as np


def f(x):
    return np.exp(x)


a, b = 0, 1  
h = b - a    


integral_trapezio_simples = (h / 2) * (f(a) + f(b))


f_second_max = np.exp(1) 
erro_estimado = -(f_second_max * h**3) / 12


print(f"Valor aproximado da integral (trapézio simples): {integral_trapezio_simples}")
print(f"Erro estimado: {erro_estimado}")