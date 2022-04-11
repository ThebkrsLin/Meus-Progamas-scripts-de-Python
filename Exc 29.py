vel = float(input('Em que velocidade voce ta?'))
mul = (vel-80) * 7
if  vel > 80:
    print('Voce ultrapassou o limite de velocidade ira pagar uma multa de R${:.2f}!'.format(mul))
print('Voce estar obdecendo o limite de velocidade diriga com segurança!')