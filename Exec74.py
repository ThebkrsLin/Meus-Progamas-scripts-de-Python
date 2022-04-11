from random import randint
sorteio = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os Numeros Sorteados Foram: ', end=' ')
for n in sorteio:
    print(f'{n}', end= ' ')
print(f'\nO maior Valor foi: {max(sorteio)}')
print(f'O Menor Valor Foi: {min(sorteio)}')