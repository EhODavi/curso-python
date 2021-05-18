vetor = []

for i in range(10):
    numero = int(input('Informe um número inteiro: '))
    vetor.append(numero)

for i in range(10):
    quantidade_divisores = 0

    for j in range(1, vetor[i] + 1):
        if vetor[i] % j == 0:
            quantidade_divisores = quantidade_divisores + 1

    if quantidade_divisores == 2:
        print(f'Posição: {i} | Número: {vetor[i]}')
