# REQUESTS
# ------------------------------------------------------------
import requests

def retorna_dados_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    # Ao aparecer '200', quer dizer que o resquest teve sucesso
    print(response.status_code)
    # # print('Text:')
    # # print(response.text)
    # # print('Json:')
    dados_cep = response.json()
    return dados_cep
    # print('Logradouro:')
    # print(dados_cep['logradouro'])

def retorna_dados_pokemon(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # Retorna o HTML da página
    response = retorna_response('https://github.com/ViniciusRCSilva')
    print(response)
    # Retorna o conteúdo da página
    # print(retorna_dados_cep('22041001'))
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])
