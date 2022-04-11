import random
num = int(input('Tente Adivinhar o número que eu pensei de 0 a 5: '))
re = random.randint(0, 5)
if num == re:
    print('Parabens Voce venceu')
else:
    print('HAHA voce perdeu!')