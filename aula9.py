# MANUPULAÇÃO DE ARQUIVOS EXTERNOS
# ------------------------------------------------------------
# Importa a biblioteca para realizar a copia de um arquivo
import shutil

def escrever_arquivo(texto):
    # 'open' cria ou abre um arquivo
    # 'w' irá sempre sobrescrever o conteúdo existente dentro do arquivo
    arquivo = open('teste.txt', 'w')

    # Escreve dentro de um arquivo
    # arquivo.write('Minha primeira escrita')
    arquivo.write(texto)

    # Sempre fechar o arquivo após sua utilização
    arquivo.close()

def atualizar_arquivo(arquivo, texto):
    # 'a' irá atualizar o conteúdo dentro do arquivo
    arquivo = open(arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(arquivo):
    # 'r' irá apenas ler o conteúdo dentro do arquivo
    arquivo = open(arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # 'split' toda vez que encontrar o que desejamos, ele insere em
    # uma lista.
    # Aqui separamos pela quebra de linha
    aluno_nota = aluno_nota.split('\n')
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 3
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/Users/vinic/PycharmProjects/')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'D:/Users/vinic/PycharmProjects/')

if __name__ == '__main__':
    mover_arquivo('Notas.txt')
    # lista_media = media_notas('Notas.txt')
    # print(lista_media)
    # escrever_arquivo('Primeira linha\n')
    # aluno = 'Cesar, 10, 10, 9'
    # atualizar_arquivo('Notas.txt', '\n' + aluno)
    # ler_arquivo('teste.txt')