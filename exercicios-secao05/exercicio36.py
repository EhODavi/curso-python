valor_venda = float(input('Informe o valor da venda: '))

if valor_venda >= 100000.00:
    print(f'Comissão: {700.00 + 0.16 * valor_venda}')
elif 80000.00 <= valor_venda < 100000.00:
    print(f'Comissão: {650.00 + 0.14 * valor_venda}')
elif 60000.00 <= valor_venda < 80000.00:
    print(f'Comissão: {600.00 + 0.14 * valor_venda}')
elif 40000.00 <= valor_venda < 60000.00:
    print(f'Comissão: {550.00 + 0.14 * valor_venda}')
elif 20000.00 <= valor_venda < 40000.00:
    print(f'Comissão: {500.00 + 0.14 * valor_venda}')
elif valor_venda < 20000.00:
    print(f'Comissão: {400.00 + 0.14 * valor_venda}')
