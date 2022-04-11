from time import sleep
num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo Valor: '))
opç = 0
div = num1 / num2
while opç != 6:
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos Numeros\n[ 5 ] Divisao \n[ 6 ] Sair do progama')
    opç = int(input('>>>>>>Qual e a sua opçao? '))
    if opç == 1:
        soma = num1 + num2
        print('A soma entre {} e {} e {}'.format(num1, num2, soma))
    elif opç == 2:
        mult = num1 * num2
        print('O resultado de {} x {} e {}'.format(num1, num2, mult))
    elif opç == 3:
         if num1 > num2:
             print('O numero {} e o maior entre os dois'.format(num1))
         else:
          print('O numero {} e o maior entre os dois'.format(num2))
    elif opç == 4:
        print('Informe os numeros novamente: ')
        num1 = int(input('Primeiro Valor: '))
        num2 = int(input('Segundo Valor: '))
    elif opç == 5:
        div = num1 / num2
        print('A divisao entre {} e {} e de {}'.format(num1, num2, div))
    elif opç == 6:
       print('Finalizando')
       print('...')
       sleep(0.7)
    else:
      print('Opçao invalida. Tente Novamente')
    print('==' * 10)
print('Fim do programa, Volte Sempre! ')
