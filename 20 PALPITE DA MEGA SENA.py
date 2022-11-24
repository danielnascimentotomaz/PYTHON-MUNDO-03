"""from random import sample
from time import sleep

print('-=-' * 20)
print('{:^50}'.format("JOGA NA MEGA SENA"))
print('-=-' * 20)

x = int(input('QUANTOS JOGOS VOÇÊ QUER QUE EU SORTEI:'))
print()
print(f'-=-=-= SORTEANDO {x} JOGOS -=-=')

for r in range(1, x + 1):
    a = aleatorio = list(sample(range(60), 5))
    a.sort()
    print(f'JOGO {r}: {a}')
    sleep(1)

print('-=-=-=  < BOA SORTE! > -=-=-=')"""

import random
from  time import sleep

print('==' * 20)
print('      JOGA NA MEGA SENA')
print('==' * 20)

a = int(input('QUANTOS JOGOS VC DESEJA!!!'))

print('==' * 20)
conjunto = []
p = 1
while p <= a:

    valores = []
    count = 1
    while count <= 6:
        aleatorio = random.randint(1, 60)
        if aleatorio not in valores:
            valores.append(aleatorio)
            count = count + 1
    conjunto.append(valores[:])
    valores.clear()
    p = p + 1

for f in conjunto:
    print(f)
    sleep(1)
print('==' * 20)
print('-=-=-=  < BOA SORTE! > -=-=-=')