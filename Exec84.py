lista = list()
dados = list()
maior = menor =  0
while True:
    lista.append(str(input('Qual o nome?: ')))
    lista.append(float(input('Qual o peso?: ')))
    if len(dados) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    dados.append(lista[:])
    lista.clear()
    op = str(input('Quer continuar?[S/N]: ')).strip()
    if op in 'Nn':
        break
print(f'Foram cadastradas {len(dados)} pessoa(s)')
print(f'O maior peso foi {maior}Kg e as pessoa(s) mais pesadas sao: ', end=' ')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]} ', end=' ')
print(f'\nE o menor peso foi {menor}Kg e as pessoas com menos pesos são: ',end=' ')
for m in dados:
    if m[1] == menor:
        print(f'{m[0]} ', end=' ')