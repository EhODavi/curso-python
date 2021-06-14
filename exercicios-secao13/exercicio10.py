arquivo_entrada = input('Informe o nome do arquivo de entrada: ')
arquivo_saida = input('Informe o nome do arquivo de saída: ')

with open(arquivo_entrada) as entrada:
    linhas = entrada.readlines()

    cidade_mais_populosa = ''
    maior_populacao = 0

    for linha in linhas:
        linha_lista = linha.split(';')

        if int(linha_lista[1]) > maior_populacao:
            cidade_mais_populosa = linha_lista[0]
            maior_populacao = int(linha_lista[1])

    with open(arquivo_saida, 'w') as saida:
        saida.write(cidade_mais_populosa + ' ' + str(maior_populacao))
