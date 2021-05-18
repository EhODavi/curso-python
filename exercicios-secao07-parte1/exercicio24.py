alunos = []

for i in range(10):
    numero_aluno = int(input('Informe o número do aluno: '))
    altura_aluno = float(input('Informe a altura do aluno: '))
    aluno = (numero_aluno, altura_aluno)
    alunos.append(aluno)

aluno_alto = alunos[0]
aluno_baixo = alunos[0]

for i in range(1, 10):
    if alunos[i][1] > aluno_alto[1]:
        aluno_alto = alunos[i]
    if alunos[i][1] < aluno_baixo[1]:
        aluno_baixo = alunos[i]

print(f'O aluno mais alto possui matrícula {aluno_alto[0]} e altura igual a {aluno_alto[1]}!')
print(f'O aluno mais baixo possui matrícula {aluno_baixo[0]} e altura igual a {aluno_baixo[1]}!')
