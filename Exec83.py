ex = str(input('Digite uma Expressao: '))
pilha = []
for sim in ex:
    if sim == '(':
          pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta Certa!')
else:
    print('Sua expressao esta errada!')

