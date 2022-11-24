palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for x in palavra:

    print(f'\nA PALAVRA {x.upper()} temos', end=' ')
    for letra in x:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')


"""

palavra = [["daniel"],["silas"]]

for x in range(0,len(palavra)):
    for y in range(0,len(palavra[x])):
        for z in range(0,len(palavra[x][y])):
            print(palavra[x][y][z])



"""