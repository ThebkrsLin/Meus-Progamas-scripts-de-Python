n1 = float(input('Primeira nota: '))
n2 = float(input('Segundaa nota: '))
re = (n1 + n2) / 2
if re >=7.0:
    print('''Com {:.1f} e {:.1f} o aluno fica com {:.1f} esta \033[32mAprovado! '''.format(n1, n2, re))
elif re >= 5.0 and re < 7:
    print('Com {:.1f} e {:.1f} pontos o aluno fica com {:.1f} ficara de \033[33mRecuperação!'.format(n1, n2, re))
else:
    print('Com {:.1f} e {:.1f} pontos o aluno fica com {:.1f} sera \033[31mReprovado!'.format(n1, n2, re))






