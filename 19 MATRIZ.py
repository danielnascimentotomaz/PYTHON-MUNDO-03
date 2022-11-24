linha = int(input('QUANTIDADE DE LINHA:'))
coluna = int(input('QUANTIDADE DE COLUNA:'))
matriz = []
pares = []
for t in range(1, linha + 1):
    lista = []
    for l in range(1, coluna + 1):
        elemento = float(input(f'ELEMENTO DA {t}° LINHA E DA {l}° COLUNA'))
        lista.append(elemento)
        # os valores pares
        if elemento % 2 == 0:
            pares.append(elemento)

    matriz.append(lista[:])
    lista.clear()

print('-=-' * 30)
# MATRIZ COMPLETA
for u in matriz:
    print(u)
print('-=-' * 30)

# Soma dos valores pares da matriz
soma = 0
for j in pares:
    soma = soma + j
print(f'A SOMA DOS VALORES PARES É {soma} ')


# soma da terceira coluna
if coluna >= 3:
    soma1 = 0
    for y in range(0, linha):
        z = matriz[y][2]
        soma1 = soma1 + z
    print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA É {soma1}')
else:
    print(f'NÃO EXISTIR A COLUNA 3')


# Maior valor da segunda linha
maior = []
if linha >= 2:
    for p in range(0, coluna):
        elemento = matriz[1][p]
        maior.append(elemento)
    print(f'O MAIOR VALOR DA SEGUNDA LINHA É {max(maior)}')
else:
    print('NÃO EXISTE A LINHA 2')