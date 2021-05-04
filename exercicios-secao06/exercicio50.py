altura_chico = 1.50
taxa_chico = 0.02
altura_ze = 1.10
taxa_ze = 0.03
anos = 0

while altura_ze <= altura_chico:
    altura_chico = altura_chico + taxa_chico
    altura_ze = altura_ze + taxa_ze
    anos = anos + 1

print(f'Anos: {anos}')
