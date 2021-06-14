nome_arquivo = input('Informe o nome do arquivo: ')

with open(nome_arquivo) as arquivo:
    conteudo = arquivo.read()

    conteudo = conteudo.replace('a', '*')
    conteudo = conteudo.replace('A', '*')
    conteudo = conteudo.replace('e', '*')
    conteudo = conteudo.replace('E', '*')
    conteudo = conteudo.replace('i', '*')
    conteudo = conteudo.replace('I', '*')
    conteudo = conteudo.replace('o', '*')
    conteudo = conteudo.replace('O', '*')
    conteudo = conteudo.replace('u', '*')
    conteudo = conteudo.replace('U', '*')

    with open('novo_arquivo.txt', 'w') as novo_arquivo:
        novo_arquivo.write(conteudo)
