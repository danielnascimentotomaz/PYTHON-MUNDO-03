valor = []
maior = 0
menor = 0
for x in range(0, 5):
    valor.append(int(input(f'digite um valor para posicão {x}°:'.upper())))
    if x == 0:
        maior = valor[x]
        menor = valor[x]
    else:
        if valor[x] > maior:
            maior = valor[x]
        elif valor[x] < menor:
            menor = valor[x]
print(20 * '-=-')

print(f'VOCÊ DIGITOU OS VALORES {valor}')

print(f'O MAIOR VALOR DIGITADO FOI {maior} NAS POSICÕES', end=' ')
for a, b in enumerate(valor):
    if b == maior:
        print(f'{a}...', end=' ')

print(f'\nO MENOR VALOR DIGITADO FOI {menor} NAS POSICÕES', end=' ')
for c, d in enumerate(valor):
    if d == menor:
        print(f'{c}...', end=' ')
