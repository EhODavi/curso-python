nome_arquivo_leitura = input('Informe o nome do arquivo de leitura: ')
nome_arquivo_escrita = input('Informe o nome do arquivo de escrita: ')

with open(nome_arquivo_leitura) as arquivo:
    conteudo = arquivo.read()
    novo_conteudo = ''

    for letra in conteudo:
        novo_conteudo += letra.upper()

    with open(nome_arquivo_escrita, 'w') as novo_arquivo:
        novo_arquivo.write(novo_conteudo)
