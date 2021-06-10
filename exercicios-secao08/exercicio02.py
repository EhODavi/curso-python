from typing import List


def converte_data(data: str) -> None:
    data_str: List[str] = data.split('/')

    print(f'{data_str[0]} de ', end='')

    if data_str[1] == '01':
        print('Janeiro de ', end='')
    elif data_str[1] == '02':
        print('Fevereiro de ', end='')
    elif data_str[1] == '03':
        print('Março de ', end='')
    elif data_str[1] == '04':
        print('Abril de ', end='')
    elif data_str[1] == '05':
        print('Maio de ', end='')
    elif data_str[1] == '06':
        print('Junho de ', end='')
    elif data_str[1] == '07':
        print('Julho de ', end='')
    elif data_str[1] == '08':
        print('Agosto de ', end='')
    elif data_str[1] == '09':
        print('Setembro de ', end='')
    elif data_str[1] == '10':
        print('Outubro de ', end='')
    elif data_str[1] == '11':
        print('Novembro de ', end='')
    else:
        print('Dezembro de ', end='')

    print(f'{data_str[2]}.')
