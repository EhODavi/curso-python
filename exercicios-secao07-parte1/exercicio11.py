vetor = []
soma_positivo = 0
quantidade_negativo = 0

for i in range(10):
    numero = float(input('Informe um número: '))
    vetor.append(numero)

    if numero >= 0:
        soma_positivo = soma_positivo + numero
    else:
        quantidade_negativo = quantidade_negativo + 1

print(f'Vetor: {vetor}')
print(f'Soma de todos os positivos: {soma_positivo}')
print(f'Quantidade de números negativos: {quantidade_negativo}')
