from random import randint
from time import sleep
from operator import itemgetter

valor = {'JOGADOR 1': randint(1, 6),
         'JOGADOR 2': randint(1, 6),
         'JOGADOR 3': randint(1, 6),
         'JOGADOR 4': randint(1, 6)
         }

for r, t in valor.items():
    print(f'{r} TIROU {t} NO DADOS')
    sleep(1)

print('-=-' * 15)
ranking = sorted(valor.items(), key=itemgetter(1), reverse=True) # ORDENAR O DICIONARIO  E COLOCAR EM ORDEN REVERSA
print('   == RANKING DOS JOGADORES ==')

for r, e in enumerate(ranking):
    print(f'     {r + 1}° LUGAR {e[0]} COM {e[1]}')
    sleep(1)
