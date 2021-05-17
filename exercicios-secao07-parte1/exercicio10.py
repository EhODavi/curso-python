notas = []

for i in range(15):
    nota = float(input('Informe a nota do aluno: '))
    notas.append(nota)

print(f'Média geral: {sum(notas) / 15}')
