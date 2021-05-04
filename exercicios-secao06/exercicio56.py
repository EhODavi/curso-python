soma_primos = 2

for i in range(3, 2000000, 2):
    primo = True

    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            primo = False
            break
    if primo:
        soma_primos = soma_primos + i

print(f'Soma: {soma_primos}')
