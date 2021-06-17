# LAÇOS
# ------------------------------------------------------------
# Laços
nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota invalida.\nEntre novamente com a nota: '))

# ------------------------------------------------------------
# limite = int(input('Entre com o valor limite: '))
#
# for i in range(limite + 1):
#     div = 0
#     x = 0
#     for x in range(1, i + 1):
#         resto = i % x
#         if resto == 0:
#             div += 1
#     if x == 1 or div == 2:
#         print('Numero {i} primo'.format(i=i))
#     else:
#         print('Numero {i} nao eh primo'.format(i=i))
# ------------------------------------------------------------
# num = int(input('Insira um numero: '))
# div = 0
#
# for x in range(1, num+1):
#     resto = num % x
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print('Numero {num} primo' .format(num=num))
# else:
#     print('Numero {num} nao eh primo' .format(num=num))
# ------------------------------------------------------------
# # Percorre do 0-4
# for x in range(5):
#     print(x)
# # Percorre do 1-10
# for x in range(1, 10):
#     print(x)