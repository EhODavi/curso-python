nota_laboratorio = float(input('Informe a nota do laboratório do estudante: '))
nota_avaliacao_semestral = float(input('Informe a nota da avaliação semestral do estudante: '))
nota_exame_final = float(input('Informe a nota do exame final do estudante: '))

if 0 <= nota_laboratorio <= 10 and 0 <= nota_avaliacao_semestral <= 10 and 0 <= nota_exame_final <= 10:
    media_ponderada = (nota_laboratorio * 2 + nota_avaliacao_semestral * 3 + nota_exame_final * 5) / 10

    print(f'Média do estudante: {media_ponderada}')

    if media_ponderada <= 2.9:
        print('ESTUDANTE REPROVADO!')
    elif media_ponderada <= 4.9:
        print('ESTUDANTE EM RECUPERAÇÃO!')
    else:
        print('ESTUDANTE APROVADO!')
else:
    print('NOTAS INVÁLIDAS!')
