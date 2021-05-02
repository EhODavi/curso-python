soma_total = 0
contador = 0

while True:
    nota = int(input('Informe a nota do aluno: '))

    if not (10 <= nota <= 20):
        break

    soma_total = soma_total + nota
    contador = contador + 1

print(f'Média aritmética das notas: {soma_total / contador}')
