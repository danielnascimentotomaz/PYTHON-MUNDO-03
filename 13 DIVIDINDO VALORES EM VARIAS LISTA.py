lista = []
pares = []
impares = []

while True:
    valor = int(input('DIGITE UM VALOR:'))
    lista.append(valor)

    continuar = str(input('QUER CONTINUAR [S/N]:')).upper().strip()[0]
    while continuar not in 'NS':
        continuar = str(input('TENTE NOVAMENTE. QUER CONTINUAR[S/N]:')).upper().strip()[0]

    if continuar == 'N':
        break

print('-=-' * 25)

print(f'A LISTA COMPLETA È {lista} ')


for y in lista:
    if y % 2 == 0:
        pares.append(y)

    elif y % 2 == 1:
        impares.append(y)

print(f'A LISTA DE PARES È {pares}')
print(f'A LISTA DE IMPARES È {impares}')
 