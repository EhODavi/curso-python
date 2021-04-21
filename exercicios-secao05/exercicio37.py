hora_entrada = int(input('Informe a hora da entrada: '))
min_entrada = int(input('Informe o minuto da entrada: '))
hora_saida = int(input('Informe a hora da saída: '))
min_saida = int(input('Informe o minuto da saída: '))

total_entrada = hora_entrada * 60 + min_entrada
total_saida = hora_saida * 60 + min_saida
total = 0

if (hora_saida < hora_entrada) or (hora_saida == hora_entrada and min_saida <= min_entrada):
    total = (24 * 60) - (total_entrada - total_saida)
else:
    total = total_saida - total_entrada

total_hora = int(total / 60)
total_min = total % 60

if total_min > 0:
    total_hora = total_hora + 1

if total_hora == 1 or total_hora == 2:
    print(f'Total a ser pago ({total_hora} horas): {total_hora}')
elif total_hora == 3 or total_hora == 4:
    print(f'Total a ser pago ({total_hora} horas): {total_hora * 1.40}')
else:
    print(f'Total a ser pago ({total_hora} horas): {total_hora * 2.00}')
