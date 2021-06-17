# LAMBDA (FUNÇÃO ANÔNIMA)
# ------------------------------------------------------------
# def contador_letras(lista_palavras):
#     contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador

# Faz a mesma coisa, de forma simplicada ↓
contador_letras = lambda lista: [len(x) for x in lista]
# Contudo, só é eficiente para funções que dê para resolver com apenas uma linha

lista_animais = ['cachorro', 'gato', 'elefante']

print(contador_letras(lista_animais))

print('\n')
# ------------------------------------------------------------
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

print(soma(10, 5))
print(subtracao(10, 5))
print(multiplicacao(10, 5))
print(divisao(10, 5))

print('\n')
# ------------------------------------------------------------
# Dicionário
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

print(soma(10, 2))
print(subtracao(10, 2))
print(multiplicacao(10, 2))
print(divisao(10, 2))
