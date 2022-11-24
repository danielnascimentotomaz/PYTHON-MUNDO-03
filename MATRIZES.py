matriz = []

linha = int(input('QUANTIDADE DE LINHA'))
coluna = int(input('QUANTIDADE DE COLUNA'))

for l in range(linha):
    lista = []
    for c in range(coluna):
        elemento = int(input(f'O ELEMENTO DA LINHA {l + 1} E DA COLUNA {c + 1}:'))
        lista.append(float(elemento))
    matriz.append(lista)

for e in matriz:
    print(e)

print(22 * '-=-')

print(matriz[0])  # pega a primeira linha
print(matriz[1])  # pega segunda linha

print(matriz[0][0]) # acessar elemento dentro da matriz

print(len(matriz))  # retorna quantidade de linha

print(len(matriz[0])) # retorna quantidade de coluna
