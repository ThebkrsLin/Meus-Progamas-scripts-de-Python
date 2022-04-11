lista = []
while True:
    print('='*40)
    n = int(input('Digite um Valor a ser Adicionado'))
    if n not in lista:
        lista.append(n)
        print('Valor Adicionado com Sucesso!')
    else:
        lista.pop()
        print('Valo Duplicado! Nao Sera adicionado')
    res = str(input('Quer Continuar?[S/N]: '))
    if res not in 'Ss':
        res = str(input('Resposta Invalida! Por Favor Digite Novamente[S/N]:'))
    if res in 'Nn':
        break
print(f'Sua lista e: {lista}')
print('='*40)
