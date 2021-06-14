primeiro_arquivo = input('Informe o nome do primeiro arquivo: ')
segundo_arquivo = input('Informe o nome do segundo arquivo: ')

with open(primeiro_arquivo) as primeiro, open(segundo_arquivo) as segundo:
    conteudo = primeiro.read() + '\n'
    conteudo += segundo.read()

    with open('novo_arquivo.txt', 'w') as terceiro:
        terceiro.write(conteudo)
