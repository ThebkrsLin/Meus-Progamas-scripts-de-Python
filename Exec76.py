lista = ('Estojo', 1.75,
         'Borracha', 1.00,
         'Estilhete', 3.00,
         'Lapis', 1.50,
         'Caneta', 2.00,
         'Lapiszera', 1.60,
         'Bolsa', 110.53,
         'Kit de Reguas', 10.32)
print('='*30)
print('Lista de Preço')
print('='*30)
for pro in range(0, len(lista)):
    if pro % 2 == 0:
        print(f'{lista[pro]:30}-------------------------------------------', end= ' ')
    else:
        print(f'R${lista[pro]:>7.2f}')
print('='*30)
