respostas = []

for i in range(5):
    respostas.append([])

    if i == 0:
        print(f'Lendo as respostas do aluno {i + 1}:\n')
    else:
        print(f'\nLendo as respostas do aluno {i + 1}:\n')

    for j in range(10):
        resposta = input()
        respostas[i].append(resposta)

gabarito = []

print('\nLendo o gabarito:\n')

for i in range(10):
    resposta = input()
    gabarito.append(resposta)

notas = []

for i in range(5):
    notas.append(0)

    for j in range(10):
        if respostas[i][j] == gabarito[j]:
            notas[i] = notas[i] + 1

print('\nRespostas:\n')

for i in range(5):
    print(respostas[i])

print('\nGabarito:\n')
print(gabarito)

print(f'\nNotas de cada aluno: {notas}')
