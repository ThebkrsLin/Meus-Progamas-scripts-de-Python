num = ('Zero', 'Um','Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dizesseis', 'Dizessete', 'Dezoito', 'Dizenove', 'Vinte')
res = int(input('Digite um Numero de 0 a 20: '))
if res < 0 or  res > 20:
    res = int(input('Tente Novamente.Digite Um Numero de 0 a 20: '))
print(f'Voce Digitou o Numero {num[res]}')
