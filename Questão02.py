def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return print(f'O número {n} pertence à sequência de Fibonacci.')
    else:
        return print(f'O número {n} não pertence à sequência de Fibonacci.')


n = int(input('Digite um número e verifique se ele pertence a sequencia de fibonacci: '))

fibonacci(n)