def sum_to_n(n):
    if n <= 0:
        return 0
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

def sum_evens(n):
    answer = 0
    for i in range(2,n+1,2):
        answer = answer + i
    return answer

def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado = resultado * i
    return resultado
