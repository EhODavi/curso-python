vetor = []
vetor_impares = []
contador = 0

while contador < 10:
    numero = int(input('Informe um número no intervalo [0,50]: '))

    if 0 <= numero <= 50:
        vetor.append(numero)
        contador = contador + 1

        if numero % 2 != 0:
            vetor_impares.append(numero)

print(f'Vetor:')

for i in range(10):
    if i % 2 == 0:
        print(f'{vetor[i]} ', end="")
    else:
        print(vetor[i])

print()

print(f'Vetor dos ímpares:')

for i in range(len(vetor_impares)):
    if i % 2 == 0:
        print(f'{vetor_impares[i]} ', end="")
    else:
        print(vetor_impares[i])
