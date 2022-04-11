valores = []
maior =  0
menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um Valor na posiçao {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print('-'*40)
print(f'A lista e: {valores}')
print(f'O maior Valor e {maior} e esta nas posiçoes(ao): ', end=' ')
for i, p in enumerate(valores):
    if p == maior:
        print(f'{i}, ', end=' ')
print(f'\nO menor valor e {menor} e esta na(s) posiçoes(ao): ', end=' ')
for i, p in enumerate(valores):
    if p == menor:
        print(f'{i}...  ', end=' ')
print('-'*40)
