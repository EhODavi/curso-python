matriz = []

for i in range(5):
    matriz.append([])

    if i != 0:
        print()

    print(f'Lendo informações do aluno {i + 1}:')

    matricula = int(input('Informe a matrícula: '))
    matriz[i].append(matricula)

    media_provas = int(input('Informe a média das provas: '))
    matriz[i].append(media_provas)

    media_trabalhos = int(input('Informe a média dos trabalhos: '))
    matriz[i].append(media_trabalhos)

    matriz[i].append(media_provas + media_trabalhos)

soma = 0
melhor_aluno = (matriz[0][0], matriz[0][3])

for i in range(5):
    soma = soma + matriz[i][3]

    if matriz[i][3] > melhor_aluno[1]:
        melhor_aluno = (matriz[i][0], matriz[i][3])

print(f'\nMelhor aluno: {melhor_aluno[0]}')
print(f'Média aritmética das notas finais: {soma / 5}')
