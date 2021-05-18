vetor = []
vetor_impar = []
vetor_par = []

for i in range(6):
    numero = int(input('Informe um número: '))
    vetor.append(numero)

    if numero % 2 == 0:
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)

print(f'\nNúmeros pares digitados: {vetor_par}')
print(f'Soma dos números pares digitados: {sum(vetor_par)}')
print(f'Números ímpares digitados: {vetor_impar}')
print(f'Quantidade de números ímpares digitados: {len(vetor_impar)}')
