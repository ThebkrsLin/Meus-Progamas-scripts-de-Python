print('|---------------------Lojas Americanas---------------------|')
preco = float(input('Qual o preço das compras? R$'))
print("Formas de Pagamento:"
"\n[ 1 ] A vista dinheiro/cheque;"
"\n[ 2 ] A vista cartao;"
"\n[ 3 ] 2x no cartao; "
"\n[ 4 ] 3x a cartao;")
op = int(input('Qual e a sua opçao? '))
if op == 1:
    total = preco - (preco * 10 / 100)
    print('Em a vista a sua compra custara R${:.2f} com 10% de desconto'.format(total))
elif op == 2:
    total = preco - (preco * 5 / 100)
    print('Em a vista no cartao a compra custara R${:.2f} com 5% de desconto '.format(total))
elif op == 3:
    total = preco
    parce = total / 2
    print('Sua compra sera parcelada em 2x  de R${:.2f} sem juros!'.format(parce))
elif op == 4:
    total = preco + (preco * 20 / 100)
    totpac = int(input('Com quantas parcelas? '))
    parce1 = total / totpac
    print('Sua compra sera parcelada em {}x  de R${:.2f} com Juros! '.format(totpac, parce1))
else:
    total = preco
    print('Opçao invalida tente novamente')
print('Sua compra de R${:.2f} custara R${:.2f} no final'.format(preco, total))




