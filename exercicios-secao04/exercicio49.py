hora_inicio = int(input('Informe a hora: '))
minuto_inicio = int(input('Informe o minuto: '))
segundo_inicio = int(input('Informe o segundo: '))
duracao = int(input('Informe a duração em segundos: '))

segundos_final = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio + duracao

horas_final = int(segundos_final / 3600)
segundos_final = segundos_final % 3600

minutos_final = int(segundos_final / 60)
segundos_final = segundos_final % 60

print(f'Horas: {horas_final}')
print(f'Minutos: {minutos_final}')
print(f'Segundos: {segundos_final}')
