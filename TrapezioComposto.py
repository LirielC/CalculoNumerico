def f(x):
    return np.exp(x)

a, b = 0, 1  
n = 10       
h = (b - a) / n  

x = np.linspace(a, b, n + 1)  
y = f(x)


TrapezioComp = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

f_second_max = np.exp(1)  
erro_estimado = -(n * h**3 / 12) * f_second_max

print(f"Valor aproximado da integral: {TrapezioComp}")
print(f"Erro estimado: {erro_estimado}")