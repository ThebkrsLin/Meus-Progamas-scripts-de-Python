from time import sleep
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
invertido = ''
for letra  in range(len(junto) - 1, -1, -1):
    invertido += junto[letra]
print('A frase {} invertida fica {}'.format(junto, invertido))
if invertido == junto:
    print('A frase digitada acima e Palindromo')
else:
     print('A frase digitada a cima nao e palindromo')



