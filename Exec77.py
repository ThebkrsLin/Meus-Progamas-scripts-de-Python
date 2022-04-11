pala = ('Curso', 'Aprender', 'Viver', 'Ganhar', 'Vida', 'Crescer', 'Progamar', 'Trabalhar')
for palavra in pala:
    print(f'Na Palavra {palavra.upper()} Temos ', end= ' ')
    for letra in palavra:
        if letra.lower()  in 'aeiou':
            print(letra, end= '  ')

