#dicionario1 = {}
#dicionario2 = dict()
###################################################
#### DECLARANDO UM DICIONARIO E MOSTRANDO
"""dicionario = {'nomes': 'pedro', 'idade': '22'}
print(dicionario['nomes'])
print(dicionario['idade'])
print(f'O {dicionario["nomes"]} tem {dicionario["idade"]} anos')"""
###################################################

###################################################
### ADICIONAR NOVO ELEMENTO
"""dicionario = {'nomes': 'pedro', 'idade': '22'}

dicionario['sexo'] = 'M'
print(dicionario)
print(dicionario['nomes'])
print(dicionario['idade'])
print(dicionario['sexo'])"""
#####################################################

#####################################################
## REMOVER ELEMENTO

"""dicionario = {'nomes': 'pedro', 'idade': '22', 'SEXO': 'M'}
del dicionario['nomes']
print(dicionario)"""
##########################################################################

##########################################################################
"""dicionario = {'nomes': 'pedro', 'idade': '22', 'SEXO': 'M'}
print(dicionario.values()) # OS  ELEMENTO DO DICIONARIO
print(dicionario.keys())   # OS NOMES DA POSICAO DE CADA ELEMENTO DICIONARIO
print(dicionario.items())  #  OS ELEMENTOS E NOMES DE CADA POSICAO"""
#############################################################################

############################################################################
### PERCORRER O DICIONARIO MOSTRANDO O ELEMENTO  E NOMES DE CADA POSICAO
"""dicionario = {'nomes': 'pedro', 'idade': '22', 'SEXO': 'M'}
for k, y in dicionario.items():
    print(f'{k} = {y}')"""
##################################################################################

##################################################################################
# percorrer nomes das posicao
"""dicionario = {'nomes': 'pedro', 'idade': '22', 'SEXO': 'M'}
for k in dicionario.keys():
    print(k)"""
#################################################################################

#################################################################################
## percorrer o elemento do dicionario
"""dicionario = {'nomes': 'pedro', 'idade': '22', 'SEXO': 'M'}
for w in dicionario.values():
    print(w)"""
################################################################################

###############################################################################
### TROCAR ELEMENTO DO DICIONARIO E ADICIONAR
"""dicionario = {'nomes':'pedro', 'idade':'22', 'SEXO':'M'}
dicionario['nomes'] = 'daniel' # TROCAR ELEMENTO
dicionario['peso'] = '40' # ADICIONAR ELEMENTO
print(dicionario)"""

###############################################################################
## ANALISE DE DICIONARIO
"""brasil = []
estado1 = {'UF': 'rio janeiro', 'SIGLA': 'RJ'}
estado2 = {'UF': 'são paulo', 'SIGLA': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)# MOSTRA DICIONARIO 1
print(estado2)# MOSTRA DICIONARIO 2
print(brasil) # MOSTRA LISTA COM TODOS DICIONARIO
print(brasil[0])# MOSTRA DICIONARIO 1
print(brasil[1])# MOSTRA DICIONARIO 2
print(brasil[0]['UF']) # MOSTRA O PRIMEIRO ELEMENTO DO PRIMEIRO DICIONARIO 
print(brasil[1]['SIGLA']) # MOSTRA O SEGUNDO  ELEMENTO DO SEGUNDO DICIONARIO"""
######################################################################################
# AMAZERNAR DADOS EM DICIONARIO
estado = {}
brasil = []
for x in range(0, 3):
    estado['UF'] = str(input('UNIDADE FEDERATIVA:'))
    estado['SIGLA'] = str(input('SIGLA DO ESTADO:'))
    brasil.append(estado.copy())
for r in brasil:
    print(r) # MOSTRA CADA DICIONARIO


for s in brasil:
    for x, y in s.items():
        print(f'O CAMPO {x} TEM VALOR {y}') # PERCORRER TODOS ELEMENTO DO DICIONARIO


for m in brasil:
    for t in m.values():
        print(t, end=' ')
    print() # quebra linha quando terminar o primeiro laço







# DICIONARIO  JUNTAR COM LISTA
"""dicionario = {'titulo': 'star wars', 'ano': '1977', 'diretor': 'GEOORGE LUCAS'}
dicionario1 = {'titulo': 'avengers', 'ano': '2012', 'diretor': 'JOSS WHEDON'}
dicionario2 = {'titulo': 'matrix', 'ano': '1999', 'diretor': 'WACHAWSKI'}"""





