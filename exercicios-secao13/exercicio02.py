nome_arquivo = input('Informe o nome do arquivo: ')

with open(nome_arquivo) as arquivo:
    print(f'O arquivo {nome_arquivo} possui {len(arquivo.readlines())} linhas')
