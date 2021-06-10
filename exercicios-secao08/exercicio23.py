def imprime_triangulo(n: int) -> None:
    qtd_asteriscos: int = 1
    metade: bool = False

    for i in range(2 * n - 1):
        print('*' * qtd_asteriscos)

        if qtd_asteriscos == n:
            metade = True

        if metade:
            qtd_asteriscos -= 1
        else:
            qtd_asteriscos += 1
