ced = 100
totalced = 0
print('-' * 30)
print('BANCO PARAISO')
print('-' * 30)
valor = int(input('Digite o Valor que Voce Quer Sacar: R$'))
total = valor
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Foram {totalced} Cedulas de R${ced}')
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
