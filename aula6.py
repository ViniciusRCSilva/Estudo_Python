# CONJUNTOS E SUAS FUNÇÕES
# ------------------------------------------------------------
# Conjunto
# Não permite duplicidade!
conjunto = {1, 2, 3, 4}
conjunto2 = {4, 5, 6, 7, 8}

# 'add' irá adicionar um elemento no conjunto
conjunto.add(5)
# 'discard' irá descartar um elemento no conjunto
conjunto.discard(2)
print('Conjunto: ', conjunto)

print('Conjunto 2: ', conjunto2)

# 'conjunto_uniao' irá receber a união (union) de 'conjunto' e 'conjunto2'
conjunto_uniao = conjunto.union(conjunto2)
print('Conjunto uniao: ', conjunto_uniao)

# 'conjunto_interseccao' irá receber a intersecção (intersection) de 'conjunto' e 'conjunto2'
# Ou seja, o(s) valor(es) que são iguais nos dois conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Conjunto interseccao: ', conjunto_interseccao)

# 'conjunto_diferenca' irá receber a diferença (difference) entre o 'conjunto' e 'conjunto2'
conjunto_diferenca = conjunto.difference(conjunto2)
print('Conjunto diferenca entre "conjunto" e "conjunto2": ', conjunto_diferenca)

# 'conjunto_diferenca' irá receber a diferença (difference) entre o 'conjunto2' e 'conjunto'
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Conjunto diferenca entre "conjunto2" e "conjunto": ', conjunto_diferenca2)

# 'conjunto_dif_simetrica' irá receber a diferença simétrica (symmetric_difference) entre o 'conjunto' e 'conjunto2'
# Ou seja, ele irá receber os valores de 'conjunto' que não existem em 'conjunto2'
# como também irá receber os valores de 'conjunto2' que não existem em 'conjunto'
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Conjunto diferenca simetrica: ', conjunto_dif_simetrica)

print('\n')

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
# Retornará 'True', pois o 'conjunto_a' é um subconjunto de 'conjunto_b'
print('O "conjunto_a" eh um subconjunto de "conjuto_b"? ', conjunto_subset)

conjunto_subset2 = conjunto_b.issubset(conjunto_a)
# Retornará 'False', pois o 'conjunto_b' não é um subconjunto de 'conjunto_a'
print('O "conjunto_b" eh um subconjunto de "conjuto_a"? ', conjunto_subset2)

conjunto_superset = conjunto_b.issuperset(conjunto_a)
# Retornará 'True', pois o 'conjunto_b' é um superconjunto de 'conjunto_a'
print('O "conjunto_b" eh um superconjunto de "conjuto_a"? ', conjunto_superset)

conjunto_superset2 = conjunto_a.issuperset(conjunto_b)
# Retornará 'False', pois o 'conjunto_a' não é um superconjunto de 'conjunto_b'
print('O "conjunto_a" eh um superconjunto de "conjuto_b"? ', conjunto_superset2)

# Cria-se uma lista com duplicidade
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']

# Conversão da lista para conjunto
# Consequentemente, a duplicidade deixa de existir
conjunto_animal = set(lista)
print('Conjunto de animais: ', conjunto_animal)

# Conversão do conjunto para lista
lista_animal = list(conjunto_animal)
print('Lista de animais: ', lista_animal)
