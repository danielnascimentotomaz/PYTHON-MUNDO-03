"""lista = [['daniel', 2], ['leia', 4], ['silas', 6]]

print(lista[0][0])
print(lista[1][1])
print(lista[2][1])
print(lista[1])"""

############################################################
"""
teste = []
teste.append('gustavo')
teste.append(40)
galera = []
galera.append(teste)

print(galera)"""
###############################################################
"""teste = []
teste.append('gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 23
galera.append(teste[:])
print(galera)"""
################################################################
"""galera = [['joao', 19], ['ana', 33], ['joaquim', 13], ['maria', 45]]
for x in galera:
    print(x) # lista completa
    print(x[0]) # nomes
    print(x[1]) # idade"""
################################################################
galera = []
dados =[]
for x in range(1,4):
    a = str(input('nome'))
    dados.append(a)
    b = int(input('idade'))
    dados.append(b)
    galera.append(dados[:])
    dados.clear()# excluir lista de dados
print(galera)
for p in galera:
    if p[1] > 22:
        print(f'{p[0]} e maior de idade')
    else:
        print(f'{p[0]} é menor de idade')