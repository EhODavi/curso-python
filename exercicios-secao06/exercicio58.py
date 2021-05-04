a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))

soma_primos = 0

for i in range(a, b + 1):
    primo = True

    for j in range(2, i):
        if i % j == 0:
            primo = False
            break

    if primo and i != 0 and i != 1:
        soma_primos = soma_primos + i

print(f'Soma dos primos entre {a} e {b}: {soma_primos}')
