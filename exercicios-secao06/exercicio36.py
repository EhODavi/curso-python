soma_quadrado = 0
quadrado_soma = 0

for i in range(1, 101):
    soma_quadrado = soma_quadrado + i ** 2
    quadrado_soma = quadrado_soma + i

quadrado_soma = quadrado_soma ** 2

print(f'A diferença entre a soma dos quadrados dos cem primeiros números naturais e o quadrado da soma é '
      f'{quadrado_soma} - {soma_quadrado} = {quadrado_soma - soma_quadrado}')
