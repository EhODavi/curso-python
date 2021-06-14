with open('emp.txt', 'w') as saida:
    for i in range(5):
        profissao = input('Informe a profissão do funcionário: ')
        tempo_servico = input('Informe o tempo de serviço do funcionário: ')

        saida.write(profissao + ' ' + tempo_servico + '\n')
