# MANIPULAÇÃO DE DATAS
# ------------------------------------------------------------
# Importa a biblioteca para trabalhar com datas
from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    # Recebe a data atual
    data_atual = date.today()
    # 'strftime' é utilizado para converter a data para string no formato desejado
    print(data_atual.strftime('%d/%m/%y'))
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

def trabalhando_com_datetime():
    # Recebe a data e a hora atual
    data_atual = datetime.now()
    data_atual_str = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    print(data_atual.strftime('%c'))
    print(data_atual_str)
    # ------------------------------------------------------------
    # Retorna o dia da semana atual
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terca', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    # Associamos a tupla ao weekday, pois temos o mesmo formato e assim podemos trazer o dia
    # da semana traduzido
    print(tupla[data_atual.weekday()])
    # ------------------------------------------------------------
    # datetime recebe (ano, mes, dia, hora, minuto, segundo)
    data_criada = datetime(2018, 6, 20, 15, 30, 20)
    print(data_criada.strftime('%d/%m/%Y %H:%M:%S'))
    # ------------------------------------------------------------
    data_string = '01/01/2019 12:20:22'
    # 'strptime' converte uma string para data, passando o formato como parâmetro
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    # ------------------------------------------------------------
    # 'timedelta' faz o cálculo de dias ou horas que podem ser retirados em dias
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)

if __name__ == '__main__':
    trabalhando_com_date()
    trabalhando_com_time()
    trabalhando_com_datetime()
