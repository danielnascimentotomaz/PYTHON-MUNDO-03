l = int(input('DIGITE A QUANTIDADE DE LINHA'))
c = int(input('DIGITE A QUANTIDADE DE COLUNA:'))
matriz = []
for x in range(1, l + 1):
    lista = []
    for y in range(1, c + 1):
        valor = int(input(f'DIGITE O ELEMENTO DA {x}° LINHA  E {y}° COLUNA :'))
        lista.append(valor)
    matriz.append(lista[:])

for z in matriz:
    print(z)