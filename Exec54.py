from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nas = int(input('Digite o ano em a {}° nasceu: '.format(pessoas)))
    idade = atual - nas
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Foi {} pessoas Maiores de idade'.format(totmaior))
print('E tambem foram {} pessoas menores de idade'.format(totmenor))
