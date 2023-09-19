quantidade = float(input('Fale a quantidade de maçãs que deseja: '))

if quantidade < 12:
    custo_total = 1.3 * quantidade
    print(f'Esse será o valor total: ', custo_total)
else:
    custo_total1 = 1.0 * quantidade
    print(f'Esse é valor total: ', custo_total1)
