idade = int(input('Informe a idade do trabalhador: '))
tempo_servico = int(input('Informe o tempo de serviço do trabalhador: '))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print('APOSENTADO!')
else:
    print('AINDA NÃO ESTÁ APOSENTADO!')
