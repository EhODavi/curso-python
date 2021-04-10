nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input('Informe a segunda nota do aluno: '))

if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    print(f'Média das notas: {(nota1 + nota2) / 2}')
else:
    print('NOTAS INVÁLIDAS!')
