dia = int(input('Informe o dia: '))
mes = int(input('Informe o mês: '))
ano = int(input('Informe o ano: '))

data_valida = False
ano_bissesto = True

if not (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)):
    ano_bissesto = False

if ano <= 2008:
    if 1 <= dia <= 31 and mes == 1:
        data_valida = True
    elif (1 <= dia <= 28 and mes == 2 and not ano_bissesto) or (1 <= dia <= 29 and mes == 2 and ano_bissesto):
        data_valida = True
    elif 1 <= dia <= 31 and mes == 3:
        data_valida = True
    elif 1 <= dia <= 30 and mes == 4:
        data_valida = True
    elif 1 <= dia <= 31 and mes == 5:
        data_valida = True
    elif 1 <= dia <= 30 and mes == 6:
        data_valida = True
    elif 1 <= dia <= 31 and mes == 7:
        data_valida = True
    elif 1 <= dia <= 31 and mes == 8:
        data_valida = True
    elif 1 <= dia <= 30 and mes == 9:
        data_valida = True
    elif 1 <= dia <= 31 and mes == 10:
        data_valida = True
    elif 1 <= dia <= 30 and mes == 11:
        data_valida = True
    elif 1 <= dia <= 31 and mes == 12:
        data_valida = True

if data_valida:
    print('A DATA INFORMADA É VÁLIDA!')
else:
    print('A DATA INFORMADA NÃO É VÁLIDA!')
