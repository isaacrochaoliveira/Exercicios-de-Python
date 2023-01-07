from math import sqrt
n = int(input('Informe um número: '))

# Dobro, Triplo, e Raiz Quadrada
print(f'O seu dobro é: {n * 2}')
print(f'O seu triplo é: {n * 3}')

# Para calcularmos a raiz quadrada podemos:
raiz = n ** (1/2)
print(f'Sua raiz quadrada: {raiz:.2f}') # :.2f - Significa que o número real vai ter dois números após a vírgula

# Podemos também utilizar uma função:
print(f'Sua raiz quadrada: {sqrt(n):.2f}')

# Existe mais uma função que nós retorna a raiz quadrada
print(f'Sua raiz quadrada: {pow(n, (1/2)):.2f}')
