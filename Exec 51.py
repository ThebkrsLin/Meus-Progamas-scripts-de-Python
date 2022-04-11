primeiro = int(input('Primeiro Termo: ' ))
raz = int(input('Razao:  '))
dec = primeiro + (20 - 1) * raz
for pa in range (primeiro, dec + raz, raz):
    print('{}'.format(pa), end=" - ")
print('Acabou!')

