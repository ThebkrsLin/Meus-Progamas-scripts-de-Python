n = 0
while True:
    n = int(input('Digite um Numero Que Voce Quer Ver a Tabuada(Digite um Numero Negativo Pra Fechar o Progama): '))
    if n < 0:
        break
    for c in range (0, 11):
        print(f'{n} x {c} = {n*c} ')
    print('='*30)
print('Fim do Progama! Volte Sempre')