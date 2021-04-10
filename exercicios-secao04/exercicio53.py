comprimento = float(input('Informe o comprimento do terreno: '))
largura = float(input('Informe a largura do terreno: '))
preco_tela = float(input('Informe o preço do metro de tela: '))

custo = (2 * (comprimento + largura)) * preco_tela

print(f'Custo: {custo}')
