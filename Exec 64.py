from emoji import emojize
n = cont = soma = 0
n = int(input('Digite um Numero [999 para parar]: '))
while n != 999:
 soma += n
 cont += 1
 n = int(input('Digite um Numero [999 para parar]: '))
print(emojize('Voce Digitou {} Numeros e a Soma Entre Eles sao {} '.format(cont, soma), use_aliases=True))
