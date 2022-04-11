num = int(input('Digite um numero inteiro: '))
print('''Qual dessas bases voce quer converter esse numero?:
[ 1 ] Codigo Binario;
[ 2 ] Octal;
[ 3 ] HEXADECIMAL;''')
op = int(input('Selecione a sua opçao: '))
if op == 1:
    print('O número {} em binario sera {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O numero {} em Octal sera {} '.format(num, oct(num)[2:]))
elif op == 3:
    print('O numero {} em Hexadecimal sera {}'.format(num, hex(num)[2:]))
else:
    print('\033[31mOpçao invalida!')


