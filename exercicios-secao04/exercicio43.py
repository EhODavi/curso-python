total = float(input('Informe o total: '))

total_desconto = 0.90 * total
valor_parcela = total / 3
comissao_vista = 0.05 * total_desconto
comissao_parcelada = 0.05 * total

print(f'Total a pagar com desconto de 10%: {total_desconto}')
print(f'Valor de cada parcela, no parcelamento de 3x sem juros: {valor_parcela}')
print(f'Comissão do vendedor, no caso da venda ser a vista: {comissao_vista}')
print(f'Comissão do vendedor, no caso da venda ser parcelada: {comissao_parcelada}')
