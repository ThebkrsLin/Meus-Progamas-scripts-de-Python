sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Ocorreu um erro na digitaçao, por favor digite novamente: ')).strip().upper()[0]
print('O sexo {} foi validado com sucesso!'.format(sexo))


