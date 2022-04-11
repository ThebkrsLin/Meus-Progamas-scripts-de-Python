casa = float(input('Qual o valor da casa: R$'))
sala = float(input('Quanto de salario voce recebe no mes: R$'))
ano = int(input('Por quantos anos voce quer financear essa casa: '))
pres = casa/ (ano * 12)
minimo = sala * 30 / 100
print('Para pagar uma casa de R${:.2f}  em {}ano(s) '.format(casa, ano))
print('E a sua prestçao será de R${:.2f}'.format(pres))
if pres <= minimo:
    print('Emprestimo \033[32mconcedido!')
else:
    print('Emprestimo \033[31mnegado!')