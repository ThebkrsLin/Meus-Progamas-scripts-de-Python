num = []
for v in range(0, 5):
    n = int(input('Digite um Numero: '))
    if v == 0 or n > num[-1]:
        num.append(n)
        print('Foi adicionado ao Final da Lista!')
    else:
        pos = 0
        while pos < len(num):
            if pos <= num[pos]:
                num.insert(pos, n)
                print(f'Foi adicionado na posiçao {pos}')
                break
                pos += 1
print(f'Os numeros dessa lista sao: {num}')



