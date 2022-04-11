n = cont = s = 0
m = 1
while True:
    n = int(input('Digite um Numero: '))
    if n >= 999:
        break
    cont += 1
    m = m * n
    s += n
print(f'Voce Digitou {cont} Numeros a Multiplicaçao Entre Eles Sao {m} e a Soma e {s}')