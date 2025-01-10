import numpy as np
import math


valor_x = np.array([-1, 0, 1, 2])
valor_y = np.array([1, 1, 0, -1])
x_interpolacao = 1.3

def diferencas(valor_x, valor_y):
    n = len(valor_x)
    tabela = np.zeros((n, n))
    tabela[:, 0] = valor_y

    print("Tabela:")
    print(f"{'x':>3} | {'f(x)':>6} | {' Divisao. 1º ordem':>22} | {'  Divisao. 2º ordem':>22} | {' Divisao. 3º ordem':>30}")
    print("__" * 60)


    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i + 1][j - 1] - tabela[i][j - 1]) / (valor_x[i + j] - valor_x[i])

        print(f"{valor_x[i]:>3} | {valor_y[i]:>6} | ", end=" ")
        for col in range(1, j+1):
            print(f"{tabela[i][col]:>20.6f} |", end=" ")
        print()

    return tabela[0]


def polinomioNewton(coefs, valor_x, x):
    n = len(coefs)
    resultado = coefs[0]
    produto = 1.0

    print("\nCalculo do valor interpolado:")
    print(f"P(x) = {coefs[0]:.6f} ", end="")
    for i in range(1, n):
        produto *= (x - valor_x[i - 1])
        resultado += coefs[i] * produto
        print(f"+ ({coefs[i]:.6f}) * ({x} - {valor_x[i - 1]:.1f})", end="")
    print(f"\nValor interpolado: {resultado:.6f}")

    return resultado


def estimacao_erro(valor_x, x, f4_aprox=1):
    produto = 1
    for xi in valor_x:
        produto *= (x - xi)
    erro = abs(f4_aprox * produto / math.factorial(4))
    return erro

coefs = diferencas(valor_x, valor_y)



valor_interpolacao = polinomioNewton(coefs, valor_x, x_interpolacao)


erro = estimacao_erro(valor_x, x_interpolacao, f4_aprox=1)


print(f"\n Interpolação em x = {x_interpolacao}: {valor_interpolacao}")
print(f"Erro aproximado x = {x_interpolacao}: {erro:.6f}")
