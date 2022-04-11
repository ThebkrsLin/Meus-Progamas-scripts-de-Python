from random import randint
from time import sleep
v = 0
while True:
    p1 = int(input('Digite um valor: '))
    comp = randint(0, 10)
    total = p1 + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Impar Ou Par? [P/I]: ')).strip().upper()[0]
    print(f'Voce Jogou {p1} e o Computador Jogou {comp}, o Total Foi de {total}', end=' ')
    print('Deu Par!' if total % 2 == 0 else 'Deu Impar')
    print('=' * 30)
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Ganhou!')
            v += 1
        else:
            print('Voce Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce Ganhou!')
            v += 1
        else:
            print('Voce Perdeu!')
            break

    print('Vamos Jogar Novamente....')
sleep(0.5)
print('Game Over! 'f'Voce Ganhou {v} vez' if v == 1 else f'Voce Ganhou {v} Vezes ')




