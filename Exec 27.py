nome = str(input('Digite o seu nome completo:  ')).strip()
n = nome.split()
print('É  um prazer em te conhecer')
print('O seu primeiro nome e {}'.format(n[0]))
print('O seu Ultimo nome e {}'.format(n[len(n)-1]))