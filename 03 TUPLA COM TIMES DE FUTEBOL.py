# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
# do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

tabela = 'Palmeira', 'Flamengo', 'Internacional', 'Grêmio', 'São paulo', 'Atlético mineiro', \
         'Athetico-pr', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corintians', \
         'Chapecoense', 'Ceara', 'Vasco da gama', 'Sport recife', 'America-Mg', 'Vitoria', 'paraná'

print(10 * '=-=')
print(f'LISTA DE TIMES DO BRASILEIRAO: {tabela}')
print(10 * '=-=')
print(f'OS 5 PRIMEIROS SÃO {tabela[0:5]}')
print(10 * '=-=')
print(f'OS 4 ULTIMOS SÃO {tabela[-4:]}')
print(10 * '=-=')
print(f'OS TIMES EM ORDEM ALFABÉTICA:{sorted(tabela)}')
print(10 * '=-=')
print(f'O CHAPECOENSE ESTA NA {tabela.index("Chapecoense") + 1}° POSICÃO')
