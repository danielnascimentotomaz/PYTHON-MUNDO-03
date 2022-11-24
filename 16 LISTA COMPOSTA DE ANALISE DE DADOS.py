dados = []
conjunto = []
maior = 0
menor = 0

while True:
    nome = str(input('NOME:'))
    dados.append(nome)
    idade = float(input('IDADE:'))
    dados.append(idade)

    # calcular maior e menor peso
    if len(conjunto) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    ###################################
    conjunto.append(dados[:])
    dados.clear()

    continuar = str(input('QUER CONTINUAR [S/N]:')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('TENTE NOVAMENTE. QUER CONTINUAR[S/N]:')).upper().strip()[0]

    if continuar == 'N':
        break

print()
print(f'AO TODO, VOCÊ CADASTROU {len(conjunto)} PESSOAS.')

print()
print(f'MAIOR PESO FOI DE {maior:.1f}Kg. PESO DE ', end='')
for i in conjunto:
    if i[1] == maior:
        print(f'{i[0]},', end=' ')

print()
print(f'\nO MENOR PESO FOI DE {menor:.1f}Kg. PESO DE ', end=' ')
for t in conjunto:
    if t[1] == menor:
        print(f'{t[0]},', end=' ')
