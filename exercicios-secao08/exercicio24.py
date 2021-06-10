def imprime_triangulo(n: int) -> None:
    qtd_asteriscos: int = 1
    qtd_espacos: int = n - 1

    for i in range(n):
        print(' ' * qtd_espacos, end='')
        print('*' * qtd_asteriscos)

        qtd_asteriscos += 2
        qtd_espacos -= 1
