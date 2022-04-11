maior = 0
totmenor = 0
for num in range(1, 6):
    quilos = float(input('Digite o peso da {}° pessoa: '.format(num)))
    if quilos == 1:
          maior = quilos
          totmenor = quilos
    else:
        if quilos >maior:
            maior = quilos
        if quilos < totmenor:
            totmenor = quilos
print('O maior peso foi {}kg'.format(maior))
print('O menor peso foi {}kg'.format(totmenor))