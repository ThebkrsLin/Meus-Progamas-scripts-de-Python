temp = [[],  []]
for v in range(1, 8):
    n = int(input(f'Digite o {v}° Valor: '))
    if n % 2 == 0:
        temp[0].append(n)
    else:
        temp[1].append(n)
print(f'='* 30)
temp[0].sort()
temp[1].sort()
print(f'Os valores Pares sao: {temp[0]}', end=' ')
print(f'\nOs Valores Impares sao: {temp[1]}', end=' ')
