# PERSONALIZANDO EXCEÇÕES
# ------------------------------------------------------------
class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, messagem):
        self.messagem = messagem

while True:
    try:
        x = float(input('Entre com uma nota de 0-10: '))
        # ------------------------------------------------------------
        if x > 10:
            # 'raise' força uma exceção
            raise InputError('Nota nao pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota nao pode ser menor que 0')
        # ------------------------------------------------------------
        break
    except ValueError:
        print('Deve-se digitar apenas numeros!')
    except InputError as ex:
        print(ex)