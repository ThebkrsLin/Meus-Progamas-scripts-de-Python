res = 'S'
soma = quant = media = maior = menor =  0
while res in 'Ss':
  n = int(input('Digite um Numero: '))
  soma += n
  quant += 1
  if quant != 1:
       if n > maior:
           maior = n
       if n < menor:
           menor = n
  else:
       maior = menor = n
  res = str(input('Quer Continuar? [\033[0;32mS/\033[0;31mN\033[m]: ')).upper().strip() [0]
  while res not in 'NnSs':
    res = str(input('Quer Continuar? [\033[0;32mS/\033[0;31mN\033[m]: ')).upper().strip()[0]
media = soma / quant
print('Voce Digitou {} Numeros e a media foi {:.2f} '.format(quant, media))
print('O maior Numero foi {} e o Menor foi {}'.format(maior, menor))
