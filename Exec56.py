somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
maisnovas = 0
mulheresnomes = ''
for p in range(1, 5):
    print('|--------- {}° Pessoa---------|'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
       maioridadehomem = idade
       nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        maisnovas += 1
mediaidade = somaidade / 4
print('A media de idade do grupo e de {} anos'.format(mediaidade))
print('O homen chamado {} tem {} anos e o mais velho'.format(nomevelho,  maioridadehomem))
print('O numero de mulher que tem menos de 21 e de {}'.format(maisnovas))