lista = []
par = []
impar = []
while True:
    n = int(input('Digite um Valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    op = str(input('Quer Continuar?[S/N]: '))
    if op in 'Nn':
        break
print(f'A sua lista e: {lista}')
print(f'E a ordem é {lista.sort()}')
print(f'Os Numeros Pares foram: {par}')
print(f'Os numeros Impares foram: {impar}')