nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))
nota3 = float(input('Informe a terceira nota do aluno: '))

media_ponderada = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4

print(f'MÉDIA DO ALUNO: {media_ponderada}')

if media_ponderada >= 60:
    print('ALUNO APROVADO!')
else:
    print('ALUNO REPROVADO!')
