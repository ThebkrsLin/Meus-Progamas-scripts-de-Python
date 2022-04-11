from random import randint
alea = randint(0,10)
res = int(input(' ' 'Ola sou o seu computador.\ntente advinhar em que numero eu estou pensando \nentre 0 e 10:' ' '))
erros = 0
while not res == alea:
    erros +=1
    if res < alea:
        res = int(input('mais um pouco.\nTente novamente: '))
    elif res > alea:
        res = int(input('Menos.\nTente novamente: '))
    else:
        erros += res
print('Voce acertou!, voce fez {} tentativa(s) para acertar '.format(erros))
