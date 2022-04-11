total = caro = barato =  cont = 0
while True:
    print('='*30)
    print('Loja Logo Al')
    print('='*30)
    produto = str(input('Digite o Nome do Produto: '))
    preço = float(input('preço: R$'))
    cont += 1
    if preço >= 1000 :
        caro += 1
    total += preço
    if cont == 1:
        barato = preço
    else:
        if preço < barato:
            barato = preço
    op = ' '
    while op not in 'SN':
        op = str(input('Quer Continuar?: ')).strip().upper()[0]
    if op == 'N':
        break
print(f'O Total das Compras foi de R${total:.2f}')
print(f'O Produto Mais Barato foi {produto} com R${barato:.2f}')
print(f'Foram {caro} Produtos Acima de R$1.000')

