import math

def f(x):
    return math.exp(x)

a = 0
b = 1

def simpsonSimples(a, b):
    h = (b - a) / 2  
    x0 = a
    x1 = (a + b) / 2
    x2 = b

    integral = (h / 3) * (f(x0) + 4 * f(x1) + f(x2))
    return integral

def simpson_error(a, b):
    h = (b - a) / 2
    f4_max = math.exp(b)
    error = -(h**5 / 90) * f4_max
    return error



integral = simpsonSimples(a, b)
error = simpson_error(a, b)


print(f"Integral aproximada pelo método de Simpson H/3: {integral}")
print(f"Erro estimado: {error}")
