# LISTAS E TUPLAS
# ------------------------------------------------------------
# Listas
print('Parte de listas:\n')
lista = [1, 3, 5, 7]
#                   [0]       [1]      [2]
lista_animal = ['cachorro', 'gato', 'elefante']

# ------------------------------------------------------------
# print(lista)
# print(lista_animal)
# print(lista_animal[1])
# ------------------------------------------------------------

i = 1
for x in lista_animal:
    print(f'Animal {i}: ', x)
    i += 1

print('\n')

soma = 0
for x in lista:
    soma += x
print('Soma Lista: ', soma)

# Funções
print('Soma funcao Lista: ', sum(lista))
print('Maior numero Lista: ', max(lista))
print('Menor numero Lista: ', min(lista), '\n')

print(max(lista_animal))
print(min(lista_animal), '\n')

animal = input('Insira o nome de um animal: ')

if animal in lista_animal:
    print(f'Existe um(a) {animal} na lista!')
else:
    print(f'Nao existe um(a) {animal}!')
    # 'append' serve para adicionar algo na lista
    lista_animal.append(animal)
    print(f'Porem, {animal} foi adicionado(a) na lista!')
    print(lista_animal)

print('\n')

# Irá ordernar a lista
lista_animal.sort()
print('Lista ordenada: ', lista_animal)

# Irá inverter a lista
lista_animal.reverse()
print('Lista invertida: ', lista_animal)

# 'pop' serve para retirar algo na lista
lista_animal.pop()
print('Deleta o ultimo da lista: ', lista_animal)

# 'remove' serve para remover algo na lista
lista_animal.remove('elefante')
print('Deleta o elefante da lista: ', lista_animal)

print('\n')

# ------------------------------------------------------------

# Tuplas
print('Parte de tuplas:\n')
tupla = (1, 10, 12, 14)
print('Tupla: ',tupla)
print('Tupla[0]: ', tupla[0])

# Irá dar erro. A tupla é imutável!!!
# tupla[0] = 12

# Irá retornar a quantidade de elementos dentro da tupla
print('Quantidade de elementos: ', len(tupla))

# Converte a lista numa tupla
tupla_animal = tuple(lista_animal)
print('Tupla animal: ', tupla_animal)

# Converte a tupla numa lista
lista_numerica = list(tupla)
print('Lista numerica: ', lista_numerica)
