# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print(50 * '-')
print(f'\033[0;32m{"LISTAGEM DE PRECOS":^50}\033[m')
print(50 * '-')

listagem = ('LAPIS', 1.75,
            'BORRACHA', 2,
            'CADERNO', 15.90,
            'ESTOJO', 25,
            'TRANSFERIDOR', 4.20,
            'COMPASS0', 4.20,
            'MOCHILA', 120.32,
            'CANETAS', 22.30,
            'LIVRO', 34.90)

for x in range(0, len(listagem)):
    if x % 2 == 0:
        print(f'{listagem[x]:.<30}', end=' ')
    else:
        print(f'R$ = {listagem[x]:.2f}')


print(50 * '-')