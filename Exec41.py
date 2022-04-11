idade = int(input('Ano de Nascimento: '))
id1 = 2021 - idade
if id1 <= 9:
    print('Voce tem {} anos voce e um atleta da categoria MIRIN'.format(id1))
elif id1 <= 14:
    print('Voce tem {} anos e um atleta da categoria Infantil'.format(id1))
elif id1 <= 19:
    print('Voce tem {} anos e um atleta da categoria Junior'.format(id1))
elif id1 <= 25:
    print('Voce tem {} anos e um atleta da categoria Senior'.format(id1))
elif id1> 25:
    print('Voce tem {} anos e um atleta da categoria Master'.format(id1))
