import math
#Nome: Liriel 

def f(x):
    return x * math.log(x) - 1

def bisection_method(a, b, tol):
    if f(a) * f(b) >= 0:
        print("Aviso: A função não muda de sinal no intervalo fornecido. O método pode não encontrar uma raiz.")
    
    iteration = 0
    print(f"Iteração {iteration}: Intervalo inicial [a = {a}, b = {b}]")
    
    while (b - a) / 2 > tol:
        iteration += 1
        midpoint = (a + b) / 2
        f_mid = f(midpoint)
        error = abs(f_mid)  
        
        print(f"Iteração {iteration}:")
        print(f"  a = {a:.5f}, f(a) = {f(a):.5f}")
        print(f"  b = {b:.5f}, f(b) = {f(b):.5f}")
        print(f"  Ponto médio (m) = {midpoint:.5f}, f(m) = {f_mid:.5f}")
        print(f"  Erro atual = {error:.5f}")
        
        if f_mid == 0 or error <= tol:  
            print(f"Raiz encontrada: x = {midpoint:.5f} com erro {error:.5f}")
            return midpoint
        elif f(a) * f_mid < 0:
            b = midpoint
        else:
            a = midpoint
    
    raiz_aproximada = (a + b) / 2
    final_error = abs(f(raiz_aproximada))
    
    if final_error > tol:
        print(f"Não foi encontrada uma raiz com a precisão desejada. Erro final = {final_error:.5f}")
    else:
        print(f"Raiz aproximada: x = {raiz_aproximada:.5f} com erro {final_error:.5f}")
    
    return raiz_aproximada


a = 2
b = 3
tolerancia = 0.01  


raiz = bisection_method(a, b, tolerancia) 
