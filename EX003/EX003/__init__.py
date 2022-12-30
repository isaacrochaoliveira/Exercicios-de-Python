n1 = int(input('Informe um número: ')) # o meu método (int) antes do (input) converter o input que vou receber para inteiro
n2 = int(input('Informe mais um número: ')) # int(input()) // para número Inteiros || str(input()) ou input() // strings || float(input()) // Para número reais || bool(input()) // Para valores True e False (Verdadeiro e Falso)
# 2 Formas de somar
# 1 Forma
print(f'A soma entre {n1} + {n2} = {n1 + n2}') # Mais indicado quando se mostra a soma somente uma vez
# 2 Forma
soma = n1 + n2
print(f'A soma entre {n1} + {n2} = {soma}') # Mais indicado quando vai ser usar esta soma mais de uma vez ao decorrer do programa
