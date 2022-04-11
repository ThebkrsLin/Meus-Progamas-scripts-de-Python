n1 = int(input('Digite Um Valor: '))
n2 = int(input('Digite Outro Valor: '))
n3 = int(input('Digite Mais Um Valor: '))
n4 = int(input('Digite Um Ultimo Valor: '))
valores = n1, n2, n3, n4
print(f'O valor 9 Apareceu {valores.count(9)}')
if 3 in valores:
   print(f'O Primeiro Valor Tres foi Digitado na Posiçao {valores.index(3)+1}')
else:
    print('Nao ha o Valor 3 em Nenhuma Posiçao')
print('Os Valores Par(es) Sao: ', end=' ')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
