segundos = int(input('Informe um valor inteiro em segundos: '))

horas = int(segundos / 3600)
segundos = segundos % 3600

minutos = int(segundos / 60)
segundos = segundos % 60

print(f'Horas: {horas}')
print(f'Minutos: {minutos}')
print(f'Segundos: {segundos}')
