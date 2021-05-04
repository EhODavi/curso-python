a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))

qtd_primos = 0

for i in range(a, b + 1):
    primo = True

    for j in range(2, i):
        if i % j == 0:
            primo = False
            break

    if primo and i != 0 and i != 1:
        qtd_primos = qtd_primos + 1

print(f'Quantidade de primos entre {a} e {b}: {qtd_primos}')
