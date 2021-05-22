gabarito = []

print('Lendo o gabarito:')

for i in range(10):
    resposta = input()
    gabarito.append(resposta)

respostas = []
matriculas = []

for i in range(3):
    respostas.append([])

    matricula = int(input(f'\nInforme a matrícula do aluno {i + 1}: '))

    matriculas.append(matricula)

    print(f'Informe as respostas do aluno {i + 1}:')

    for j in range(10):
        resposta = input()
        respostas[i].append(resposta)

notas = []

for i in range(3):
    notas.append(0)

    for j in range(10):
        if respostas[i][j] == gabarito[j]:
            notas[i] = notas[i] + 1

qtd_aprovados = 0

for i in range(3):
    print(f'\nAluno {i + 1} com matrícula {matriculas[i]}:')
    print(f'Respostas = {respostas[i]}')
    print(f'Nota = {notas[i]}')

    if notas[i] >= 7.0:
        qtd_aprovados = qtd_aprovados + 1

print(f'\nPercentual de aprovação = {(qtd_aprovados / 3) * 100}%')
