notas = []

for i in range(10):
    notas.append([])

    if i != 0:
        print()

    print(f'Lendo as notas do aluno {i + 1}:')

    for j in range(3):
        nota = int(input())
        notas[i].append(nota)

qtd_prova = []

for i in range(3):
    qtd_prova.append(0)

aluno_escolhido = []

for i in range(10):
    aluno_escolhido.append(False)

for j in range(3):
    for i in range(10):
        if j == 0:
            if notas[i][j] <= notas[i][j + 1] and notas[i][j] <= notas[i][j + 2] and not aluno_escolhido[i]:
                qtd_prova[j] = qtd_prova[j] + 1
                aluno_escolhido[i] = True
        elif j == 1:
            if notas[i][j] <= notas[i][j + 1] and notas[i][j] <= notas[i][j - 1] and not aluno_escolhido[i]:
                qtd_prova[j] = qtd_prova[j] + 1
                aluno_escolhido[i] = True
        else:
            if notas[i][j] <= notas[i][j - 1] and notas[i][j] <= notas[i][j - 2] and not aluno_escolhido[i]:
                qtd_prova[j] = qtd_prova[j] + 1
                aluno_escolhido[i] = True

print()

for i in range(3):
    print(f'Quantidade de alunos cuja pior nota foi na prova {i + 1}: {qtd_prova[i]}')
