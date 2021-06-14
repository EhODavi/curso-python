arquivo_entrada = input('Informe o nome do arquivo: ')
palavra = input('Informe uma palavra: ')

with open(arquivo_entrada) as entrada:
    conteudo = entrada.read()

    print(f"A palavra '{palavra}' aparece {conteudo.count(palavra)} vezes no arquivo!")
