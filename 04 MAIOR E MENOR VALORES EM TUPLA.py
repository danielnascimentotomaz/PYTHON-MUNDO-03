# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e
# o maior valor que estão na tupla.

from random import sample

aleatorio = tuple(sample(range(10), 5))  ## obs: o 10 é o intervalo entre 0 e 10, e o 5 é a quantidade  de sorteio

print('OS VALORES SORTEADOS FORAM:', end=' ')

for i in aleatorio:
    print(f'{i} ', end='')

print(f'\nO MAIOR VALOR SORTEADO FOI {max(aleatorio)}')
print(f'O MENOR VALOR SORTEADO FOI {min(aleatorio)}')

# SOTEAR 5 NÚMERO
# valores = ((randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)),(randint(1,10)))