import numpy as np


def f(x):
    return np.exp(x)


a, b = 0, 1  
n = 10       
h = (b - a) / n  


x = np.linspace(a, b, n + 1)
y = f(x)


soma_impares = np.sum(y[1:n:2])  
soma_pares = np.sum(y[2:n-1:2]) 
integral_simpson = (h / 3) * (y[0] + 4 * soma_impares + 2 * soma_pares + y[-1])


f_fourth_max = np.exp(1)  
erro_estimado = -n * (h**5 / 90) * f_fourth_max


print(f"Valor aproximado da integral (Simpson composto): {integral_simpson}")
print(f"Erro estimado: {erro_estimado}")
