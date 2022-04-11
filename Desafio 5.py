n1 = int(input('digite um número:'))
print('o número atual é {} o seu antecessor é {} e o seu sucessor é {}'.format(n1, n1-1, n1+1))
n2 = int(input('digite outro número:'))
dx = n2*2
trx = n2*3
raiz = n2**(1/2)
print('O dobro deste número é {} o triplo é {} e a raìz quadrada é {:3f}...'.format(dx, trx, raiz))
no1 = int(input('A primeira nota:'))
no2 = int(input('A segunda nota:'))
no3 = int(input('A terceira nota:'))
re = no1+no2+no3
re2 = re/3
print('A nota desse aluno será {:.1f}'.format(re2))
m = float(input('Quantos metros percorridos:'))
cm = m*10
mm = m*100
km = m/1000
print('De {}m, foram percorridos \n {}cm \n {}mm \n {}km'.format(m, cm, mm, km))
mul = int(input('Digite um número para a tabuada:'))
print('|--------------------|')
print('{}x{}={}'.format(mul, 1, mul*1))
print('{}x{}={}'.format(mul, 2, mul*2))
print('{}x{}={}'.format(mul, 3, mul*3))
print('{}x{}={}'.format(mul, 4, mul*4))
print('{}x{}={}'.format(mul, 5, mul*5))
print('{}x{}={}'.format(mul, 6, mul*6))
print('{}x{}={}'.format(mul, 7, mul*7))
print('{}x{}={}'.format(mul, 8, mul*8))
print('{}x{}={}'.format(mul, 9, mul*9))
print('{}x{}={}'.format(mul, 10, mul*10))
print('|--------------------|')
real = float(input('Quantos dinheiro vc tem na carteira? R$'))
dolar = real / 5.06
euro = real / 6.0
libra = real / 7.00
print('Com R${} da pra comprar:\n US${:.2f} Dollars\n Є{:.2f} Euros\n £{:.2f} Libras'.format(real, dolar, euro, libra))
lar = float(input('Largura da parede:  '))
altu = float(input('Altura da parede:  '))
area = lar* altu
print('Com a dimensão {}x{} a sua area será de {}m²'.format(lar, altu, area))
litros = area / 2
print("Você irá precisar de {}l para poder pintar essa area".format(litros))
valor = float(input('Qual o preço do produto: '))
des = valor - (valor * 5/100)
print('O valor desse produto era de R${}, mais com 5% de desconto fica com R${}'.format(valor, des))
salari = float(input('Qual o salário atual do fucionário?'))
novo = salari + (salari * 15 / 1000)
print('O salário desse fucionário era de R${} agora com o aumento de 15% ficará com R${}'.format(salari, novo))
c = float(input('Informe a temperatura em °c '))
f = ((9*c)/5) + 32
print('Então de {}°c para ºf será {:.2f}°f'.format(c, f))
alu = int(input('Quantos foi alugado? '))
km2 = float(input('Quantos km percorridos? '))
alu2 = (alu*60) + (km*0.15)
print('Você pagará R${:.264f} nesse aluguel'.format(alu2))
