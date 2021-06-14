arquivo_entrada = input('Informe o nome do arquivo de entrada: ')
arquivo_saida = input('Informe o nome do arquivo de saída: ')

with open(arquivo_entrada) as entrada, open(arquivo_saida, 'w') as saida:
    linhas = entrada.readlines()
    linhas = linhas[::-1]

    for linha in linhas:
        saida.write(linha[::-1])
