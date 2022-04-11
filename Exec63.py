from emoji  import emojize
print('=' * 35)
print('Sequencia De Fibonacci:')
print('=' * 35)
n = int(input('Quantas Sequencias Voce Quer Mostrar?  '))
t1 = 0
t2 = 1
print(emojize(':point_right: {} :arrow_right: {}'.format(t1, t2), use_aliases=True), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(emojize(':arrow_right: {}'.format(t3), use_aliases=True), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print(emojize(':arrow_right: FIM :wave:', use_aliases=True))
print('=' * 35)

