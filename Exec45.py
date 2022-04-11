import random
itens = ('Pedra', 'Papel', 'Tesoura')
print("Suas opçoes:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura ")
op = int(input('Digite a sua opçao: '))
comp = random.randint(0, 2)
print('=' * 12)
print('O Computador Jogou {}\nO Jogador Jogou {}'.format(itens[comp], itens[op]))
print('=' * 12)
if comp == 0: # O computador Jogou Pedra
    if op == 0:
        print('Deu \033[33mEmpate')
    elif op == 1:
        print('Jogador \033[32mVenceu!')
    elif op == 2:
        print('O Computador \033[31mVenceu!')
    else:
        print('Jogada \033[31mInvalida!')
elif comp == 1: # O Computador Jogou Papel
    if op == 0:
        print('O Computador \033[31mVenceu!')
    elif op == 1:
        print('Deu \033[33mEmpate!')
    elif op == 2:
        print('O Jogador \033[32mVenceu!')
    else:
        print('Jogada \033[31mInvalida!')
elif comp ==2: # O Computador Jogou Tesoura
    if op == 0:
     print('O Jogador \033[32mVenceu!')
    elif op == 1:
        print('O Computador \033[31mVenceu!')
    elif op == 2:
        print('Deu \033[33mEmpate!')
    else:
        print('Jogada \033[31mInvalida!')



