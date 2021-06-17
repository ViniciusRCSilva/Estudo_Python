# EXCEÇÕES
# ------------------------------------------------------------
lista = [1, 10]
arquivo = open('teste.txt', 'r')

try:
    texto = arquivo.read()
    # ------------------------------------------------------------
    # Erros
    # divisao = 10 / 0
    # numero = lista[2]
    # x = a
    # arquivo.close() -> deve ser movido para o finally
    # ------------------------------------------------------------
    # Sem erros
    # divisao = 10 / 1
    # numero = lista[1]
# ------------------------------------------------------------
# Erro se o número for dividido por 0
except ZeroDivisionError:
    print('Nao eh possivel realizar uma divisao por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operacao aritmetica')
# Erro ao tentar capturar um número que não está presente na lista
except IndexError:
    print('Erro ao acessar um indice invalido na lista')
# Qualquer excessão que cair abaixo, irá mostrar qual foi erro
except BaseException as ex:
    print('Erro:', ex)
else:
    print('Executa quando nao ocorre excessao')
# 'finally' sempre executa o restante do código
finally:
    print('Sempre executa')
    arquivo.close()
