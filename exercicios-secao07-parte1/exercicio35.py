a = input('Informe o número a: ')
b = input('Informe o número b: ')

vetor_a = list(a[::-1])
vetor_b = list(b[::-1])

vetor_c = []

if len(vetor_a) <= len(vetor_b):
    for i in range(len(vetor_b)):
        vetor_c.append(vetor_b[i])

    for i in range(len(vetor_a)):
        vetor_c[i] = str(int(vetor_a[i]) + int(vetor_c[i]))
else:
    for i in range(len(vetor_a)):
        vetor_c.append(vetor_a[i])

    for i in range(len(vetor_b)):
        vetor_c[i] = str(int(vetor_b[i]) + int(vetor_c[i]))

for i in range(len(vetor_c)):
    if int(vetor_c[i]) >= 10:
        if i == len(vetor_c) - 1:
            vetor_c.append(vetor_c[i][0])
        else:
            vetor_c[i + 1] = str(int(vetor_c[i + 1]) + int(vetor_c[i][0]))

        vetor_c[i] = vetor_c[i][1]

print(f'\n{a} + {b} = ', end="")

for i in range(len(vetor_c) - 1, -1, -1):
    print(vetor_c[i], end="")

print()
