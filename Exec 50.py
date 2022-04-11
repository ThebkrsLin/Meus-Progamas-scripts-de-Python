soma = 0
cont = 0
for par in range (1, 7):
    n = int(input('Digite o {}° valor: '.format(par)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Voce digitou {} numeros pares e a soma desse numeros e de {}'.format(cont, soma))