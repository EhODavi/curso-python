soma_idade = 0
contador = 0

while True:
    idade = int(input('Informe a idade da pessoa: '))

    if idade == 0:
        break

    soma_idade = soma_idade + idade
    contador = contador + 1

print(f'Média das idades: {soma_idade / contador}')
