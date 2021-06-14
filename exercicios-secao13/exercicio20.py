quantidade_alunos = int(input('Informe a quantidade de alunos: '))

nomes = []
notas = []

for i in range(quantidade_alunos):
    nome = input('Informe o nome do aluno: ')
    nota = input('Informe a nota do aluno: ')

    nomes.append(nome)
    notas.append(nota)

with open('novo_arquivo.txt', 'w') as saida:
    for i in range(quantidade_alunos):
        saida.write(nomes[i] + ' ' + notas[i] + '\n')
