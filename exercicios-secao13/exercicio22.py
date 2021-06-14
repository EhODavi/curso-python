arquivo_entrada = input('Informe o nome do arquivo de entrada: ')
arquivo_saida = input('Informe o nome do arquivo de saída: ')

with open(arquivo_entrada) as entrada, open(arquivo_saida, 'w') as saida:
    linhas = entrada.readlines()

    for linha in linhas:
        vetor_linha = linha.split(' ')
        notas = [int(vetor_linha[1]), int(vetor_linha[2]), int(vetor_linha[3])]
        notas.sort()

        saida.write(vetor_linha[0] + ' ' + str(notas[0]) + ' ' + str(notas[1]) + ' ' + str(notas[2]) + '\n')
