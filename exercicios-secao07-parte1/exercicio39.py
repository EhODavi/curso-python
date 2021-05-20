n = int(input('Informe um número inteiro positivo n: '))

triangulo_pascal = []

for i in range(n):
    triangulo_pascal.append([])
    triangulo_pascal[i].append(1)

for i in range(1, n):
    for j in range(len(triangulo_pascal[i - 1])):
        if j != len(triangulo_pascal[i - 1]) - 1:
            triangulo_pascal[i].append(triangulo_pascal[i - 1][j] + triangulo_pascal[i - 1][j + 1])
        else:
            triangulo_pascal[i].append(1)

for i in range(n):
    for j in range(len(triangulo_pascal[i])):
        print(f'{triangulo_pascal[i][j]} ', end="")
    print()
