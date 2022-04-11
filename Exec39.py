from datetime import date
atual = date.today().year
nasc = int(input('Qual a data do seu nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Em {} voce tem {} anos se aliste imediatamente! '.format(atual, idade))
elif idade < 18:
    print('Em {} voce tem {} voce ira se alistar daqui a {} ano(s) em {}'.format(atual, idade, 18 - idade, (18 - idade)+atual))
elif idade > 18:
    print('Em {} voce tem {} anos mas voce ja deveria ter se alistado ha {} ano(s) atraz '.format(atual, idade, (idade - 18)))
