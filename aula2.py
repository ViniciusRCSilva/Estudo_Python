# VARIÁVEIS, OPERAÇÕES MATEMÁTICAS, CONVERSÕES E CONCATENAÇÕES
# ------------------------------------------------------------
# Variáveis
print('Variaveis:')
a = 10
b = 6

print(a)
print(b)
print('\n')

# Operações
print('Operacoes:')
soma = a + b
print('Soma: ', soma)
subtracao = a - b
print('Subtracao: ', subtracao)
multiplicacao = a * b
print('Multiplicacao: ', multiplicacao)
divisao = a / b
print('Divisao: ', divisao)
resto = a % b
print('Resto da divisao: ', resto)
print('\n')

# Conversões
print('Convertendo para strings:')
print('Soma: ' + str(soma))
print('Subtracao: ' + str(subtracao))
print('Multiplicacao: ' + str(multiplicacao))
print('Divisao: ' + str(divisao))
print('Resto da divisao: ' + str(resto))

x = '1'
soma2 = int(x) + 1
print('soma2: ', soma2)
print('str_soma2: ' + str(soma2))
print('\n')

# Concatenação
print('Concatenacao:')
# Primeira forma:
print('Soma: {}, subtracao: {}, multiplicacao: {}, divisao: {} e resto: {}'
      .format(soma, subtracao, multiplicacao, divisao, resto))
# ------------------------------------------------------------
# Segunda forma:
print('Soma: {soma}, subtracao: {subtracao}, multiplicacao: {multiplicacao}, divisao: {divisao} e resto: {resto}'
      .format(soma=soma, subtracao=subtracao, multiplicacao=multiplicacao, divisao=divisao, resto=resto))
# ------------------------------------------------------------
# Terceira forma:
print(f'Soma: {soma}, subtracao: {subtracao}, multiplicacao: {multiplicacao}, divisao: {divisao} e resto: {resto}')
print('\n')

# Interações com o usuário
valorA = int(input('Entre com o valor de a: '))
valorB = int(input('Entre com o valor de b: '))

soma = valorA + valorB
print('Soma: ', soma)
subtracao = valorA - valorB
print('Subtracao: ', subtracao)
multiplicacao = valorA * valorB
print('Multiplicacao: ', multiplicacao)
divisao = valorA / valorB
print('Divisao: ', divisao)
resto = valorA % valorB
print('Resto da divisao: ', resto)

resultado = 'Soma: {soma}, subtracao: {subtracao}, multiplicacao: {multiplicacao}, divisao: {divisao} e resto: {resto}'\
      .format(soma=soma, subtracao=subtracao, multiplicacao=multiplicacao, divisao=divisao, resto=resto)

print(resultado)
