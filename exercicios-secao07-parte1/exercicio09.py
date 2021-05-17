vetor = []
quantidade_par = 0

while True:
    numero = int(input('Informe um número inteiro par: '))

    if numero % 2 == 0:
        vetor.append(numero)
        quantidade_par = quantidade_par + 1

        if quantidade_par == 6:
            break

print(f'Vetor invertido {vetor[::-1]}')
