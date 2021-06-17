# CLASSES E MÉTODOS
# ------------------------------------------------------------
# # Classe
class Calculadora:
    # Métodos
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

# Instancia uma classe
calculadora = Calculadora(10, 2)
print('Calculadora 1: ')
print('Soma: ', calculadora.soma())
print('Subtracao: ', calculadora.subtracao())
print('Multiplicacao: ', calculadora.multiplicacao())
print('Divisao: ', calculadora.divisao())

print('\n')
# # ------------------------------------------------------------
# # Classe
class Calculadora2:
    # Métodos
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

# Instancia uma classe
calculadora = Calculadora2()
print('Calculadora 2: ')
print('Soma: ', calculadora.soma(10, 2))
print('Subtracao: ', calculadora.subtracao(10, 2))
print('Multiplicacao: ', calculadora.multiplicacao(10, 2))
print('Divisao: ', calculadora.divisao(10, 2))

print('\n')
# ------------------------------------------------------------
# Classe
class Televisao:
    # Métodos
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1
        else:
           print('TV Desligada')

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print('TV Desligada')

def energia(self):
    if self == False:
        return 'Desligada'
    else:
        return 'Ligada'

print(__name__)
# Só executa o trecho se a chamada vier do próprio arquivo
if __name__ == '__main__':
    televisao = Televisao()
    print('Televisao: ')
    print(energia(televisao.ligada))

    televisao.power()
    print(energia(televisao.ligada))

    televisao.power()
    print(energia(televisao.ligada))

    televisao.power()
    print(energia(televisao.ligada))

    print('Canal: ', televisao.canal)

    televisao.aumenta_canal()
    print('Canal: ', televisao.canal)

    televisao.diminui_canal()
    televisao.diminui_canal()
    print('Canal: ', televisao.canal)

    televisao.power()
    print(energia(televisao.ligada))

    televisao.aumenta_canal()
    print('Canal: ', televisao.canal)
