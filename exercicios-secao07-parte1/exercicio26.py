v = []

for i in range(10):
    numero = float(input('Informe um número: '))
    v.append(numero)

m = sum(v) / 10

desvio_padrao = 0

for i in range(10):
    desvio_padrao = desvio_padrao + (v[i] - m) ** 2

desvio_padrao = (1 / 9) * desvio_padrao

desvio_padrao = desvio_padrao ** (1 / 2)

print(f'Desvio Padrão: {desvio_padrao}')
