# CONDIÇÕES: OPERADORES RELACIONAIS E DE COMPARAÇÃO
# ------------------------------------------------------------
# Variáveis
a = float(input('Entre com a primeira nota: '))
b = float(input('Entre com a segunda nota: '))
c = float(input('Entre com a terceira nota: '))

#Condições
if a <= 10.0 and b <= 10.0 and c <= 10.0:
    media = (a + b + c) / 3

    print('Media: {}' .format(media))

    if media >= 7.0:
        print('Aprovado')
    elif media <= 6.9:
        print('Recuperacao')
    elif media <= 5.9:
        print('Reprovado')
else:
    print('Alguma nota informada esta errada')

# ------------------------------------------------------------
# Operadores relacionais (< e >)
# if a > b:
#     print('{a} maior que {b}' .format(a = a, b = b))
# # elif = else + if
# elif a < b:
#     print('{b} maior que {a}' .format(b = b, a = a))
# else:
#     print('Os valores sao iguais.')
#
# if a > b and a > c:
#     print('{a} maior que {b} e maior que {c}' .format(a = a, b = b, c = c))
# elif a < b and c < b:
#     print('{b} maior que {a} e maior que {c}' .format(b = b, a = a, c = c))
# elif a < c and b < c:
#     print('{c} maior que {a} e maior que {b}' .format(c = c, a = a, b = b))
# else:
#     print('Os valores sao iguais.')
#
# resto_a = a % 2
# resto_b = b % 2
# resto_c = c % 2
#
# print('Sao pares ou impares?')
# if resto_a == 0 and resto_b == 0 and resto_c == 0:
#     print('Todos sao pares')
# elif resto_a == 0 and resto_b == 0 and resto_c != 0:
#     print('Apenas o primeiro e o segundo valor sao pares')
#     print('O terceiro valor eh impar')
# elif resto_a != 0 and resto_b == 0 and resto_c == 0:
#     print('Apenas o segundo e o terceiro valor sao pares')
#     print('O primeiro valor eh impar')
# elif resto_a == 0 and resto_b != 0 and resto_c == 0:
#     print('Apenas o primeiro e o terceiro valor sao pares')
#     print('O segundo valor eh impar')
# elif resto_a == 0 and resto_b != 0 and resto_c != 0:
#     print('Apenas o primeiro valor eh par')
#     print('O segundo e o terceiro valor sao impares')
# elif resto_a != 0 and resto_b == 0 and resto_c != 0:
#     print('Apenas o segundo valor eh par')
#     print('O primeiro e o terceiro valor sao impares')
# elif resto_a != 0 and resto_b != 0 and resto_c == 0:
#     print('Apenas o terceiro valor eh par')
#     print('O primeiro e o segundo valor sao impares')
# else:
#     print('Todos sao impares')
