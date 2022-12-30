x = str(input('Digite Algo: '))
print(type(x)) # O Método (type()) ele me retorna o tipo primitivo
print(f'Só tem Espaços: {x.isspace()}') # isspace() verifica pra mim se a string só tem espeços isso é:           |  Isso que eu acabei um informar ao lado, só tem espaços
print(f'É um número: {x.isnumeric()}') # isnumeric() verifica pra mim se a string pode ser considerado um número
print(f'É um alfabético: {x.isalpha()}') # isalpha() verifica pra mim se a string pode ser considerado uma letra
print(f'É alfanúmero: {x.isalnum()}') # isalnum() verifica pra mim se a string pode ser considerada alphanúmerico - Alfabético e Númerico

