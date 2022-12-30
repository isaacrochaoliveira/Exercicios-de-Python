nome = str(input('Qual é o seu nome? ')) # O str nesse caso é opcional, porque já estamos lendo uma string
# 2 formas de mostrar variáveis na tela
# Forma 1º
print(f'Seja bem vindo {nome}')
# Forma 2º
print('Seja bem vindo {}'.format(nome))
# Até existe uma 3 forma, mas eu não recomendo ela que é a com (%), pois ela é da versão antiga do Python
