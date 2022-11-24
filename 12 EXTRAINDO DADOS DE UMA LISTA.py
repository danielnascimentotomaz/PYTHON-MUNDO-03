
lista = []
while True:
    valor = float(input('DIGITE UM VALOR:'))
    lista.append(valor)

    continuar = str(input('QUER CONTINUAR:')).upper().strip()[0]
    while continuar not in 'NS':
        continuar = str(input('TENTE NOVAMENTE. QUER CONTINUAR.')).upper().strip()[0]

    if continuar == 'N':
        break
        
print(f'VOCÊ DIGITOU {len(lista)} ELEMENTOS.')

lista.sort(reverse=True)
print(f'OS VALORES EM ORDEM DESCRECENTE SÃO {lista}')

if 5 in lista:
    print('O VALOR 5 FAZ PARTE DA LISTA')
else:
    print('O VALOR 5 NÃO FOI ENCONTRADO NA LISTA')
