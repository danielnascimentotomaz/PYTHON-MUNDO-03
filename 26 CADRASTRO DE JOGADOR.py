dados = dict()
lista = []

dados['NOMES'] = str(input('NOME DO JOGADOR:'))
partida = int(input(f'QUANTAS PARTIDA {dados["NOMES"]} JOGOU:'))

if partida > 0:

    for t in range(1, partida + 1):
        gol = int(input(f'QUANTOS GOLS NA {t}° PARTIDA :'))
        lista.append(gol)



    dados['GOL'] = lista[:]
    dados['TOTAL'] = sum(lista)

print('=-=' * 15)
print(dados)
print('=-=' * 15)
for r, t in dados.items():
    print(f'O CAMPO {r} TEM VALOR {t}')
print('=-=' * 15)

print(f'O JOGADOR  {dados["NOMES"]} JOGOU {len(dados["GOL"])} PARTIDAS ')
for t, s in enumerate(lista):
    print(f'>>> NA PARTIDA {t + 1}, FEZ {s} GOL.')
print(f'FOI UM TOTAL DE {dados["TOTAL"]} GOL')