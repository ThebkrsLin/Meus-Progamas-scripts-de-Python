peso = float(input('Qual e o seu peso: '))
altura = float(input('Qual e a sua altura: '))
imc = peso / (altura **2)
if imc < 18.5:
    print('O IMC dessa pessoa é de {:.1f} esta com o peso \033[35mabaixo do NORMAL!'.format(imc))
elif imc >=18.5 and imc < 25.5:
    print("O IMC dessa pessoa e de {:1f} o peso \033[34mNORMAL!".format(imc))
elif imc >= 25.5 and imc < 30:
    print('O IMC dessa pessoa e de {:.1f} esta \033[32mSOBREPESO!'.format(imc))
elif imc >= 30 and imc <= 40:
    print('O IMC dessa pessoa e {:.1f} Esta em \033[33mOBESIDADE!')
else:
    print('O IMC dessa pessoa e de {:.1f} esta em \033[31mObesidade Morbita!'.format(imc))