nota_aluno = float(input('Informe a nota do aluno: '))
faltas_aluno = int(input('Informe o número de faltas do aluno: '))

if 9.0 <= nota_aluno <= 10.0 and faltas_aluno <= 20:
    print('CONCEITO: A')
elif 9.0 <= nota_aluno <= 10.0 and faltas_aluno > 20:
    print('CONCEITO: B')
elif 7.5 <= nota_aluno <= 8.9 and faltas_aluno <= 20:
    print('CONCEITO: B')
elif 7.5 <= nota_aluno <= 8.9 and faltas_aluno > 20:
    print('CONCEITO: C')
elif 5.0 <= nota_aluno <= 7.4 and faltas_aluno <= 20:
    print('CONCEITO: C')
elif 5.0 <= nota_aluno <= 7.4 and faltas_aluno > 20:
    print('CONCEITO: D')
elif 4.0 <= nota_aluno <= 4.9 and faltas_aluno <= 20:
    print('CONCEITO: D')
elif 4.0 <= nota_aluno <= 4.9 and faltas_aluno > 20:
    print('CONCEITO: E')
elif 0.0 <= nota_aluno <= 3.9 and faltas_aluno <= 20:
    print('CONCEITO: E')
elif 0.0 <= nota_aluno <= 3.9 and faltas_aluno > 20:
    print('CONCEITO: E')
