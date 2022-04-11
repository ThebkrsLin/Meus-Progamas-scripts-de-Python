num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Análisando o número {}....'.format(num))
print('Unidades {}'.format(u))
print('Dezenas {}'.format(d))
print('Centanas {}'.format(c))
print('Milhar {}'.format(m))