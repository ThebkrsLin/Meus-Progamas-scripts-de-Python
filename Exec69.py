idade = homens = velha = nova = doze = 0
while True:
    print('|Cadastrar Usuario|')
    print('='*30)
    idade = int(input('Digite a Idade: '))
    sexo =' '
    print('='*30)
    while sexo not in 'MmFf':
        sexo = str(input('Digite o Sexo[M/F]: ')).strip().upper()[0]
    op = str(input('Quer Cadastar Outro Usuario?[S/N]: ')).strip().upper()[0]
    if sexo == 'F' and idade <= 18:
        nova += 1
    if sexo == 'F' and idade > 20:
        velha += 1
    if sexo == 'M':
        homens += 1
    if op == 'N':
        break
print(f'Foram Cadastradas {nova} Mulheres menos ou Com 18 Anos;')
print(f'Foram Cadastrados {homens} Homens;')
print(f'Foram Cadastradas {velha} Mulheres com Mais de 20 Anos;')