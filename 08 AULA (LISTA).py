# lista utilizar []

############### MANIPULAÇÃO DA LISTA ######################

###########################################################
"""lista = ['x', 'y', 'z']
print(lista)     # mostra a lista
print(lista[0])  # primeiro elemento da lista
print(lista[1])  # segundo elemento da lista
print(lista[2])  # terceiro elemento da lista"""
#############################################################

#############################################################
### TROCAR ELEMENTO DENTRO DE UMA LISTA
"""lista = ['x', 'y', 'z']
lista[0] = 'a'
print(lista)"""
##############################################################


##################### COMANDOS ##############################

#############################################################
### ADICIONAR ELEMENTO EM UMA LISTA
"""X. append('a')"""
#############################################################

#############################################################
### ADICIONAR ELEMENTO EM UMA POSICÃO NA LISTA
"""x.insert(0,'c')"""  # OBS: (0) E A POSICÃO E (c) O ELEMENTO
###############################################################

################################################################
## APAGAR ELEMENTO DE UMA LISTA

"""del.x[2]"""  # APAGAR NA POSICÃO 2
"""x.pop(2)"""  # APAGAR NA POSICÃO 2
"""x.pop()"""  # APAGAR O ÚLTIMO ELEMENTO DA LISTA
"""x.remove(b)"""  # APAGAR O ELEMENTO (b) DA LISTA
###############################################################


#################################################################
## VERIFICANDO  SE  O  ELEMENTO ESTA NA LISTA PARA APAGAR
"""lanche = ['a', 'b', 'c', 'd']
if 'r' in lanche:
    lanche.remove('r')
    print(lanche)
else:
    print('não foi encontrado o elemento '.upper())"""
#####################################################################


######################################################################
## LISTA UTILIZANDO RANGE()
"""valores = list(range(1, 11))
print(valores)"""
######################################################################

######################################################################
## ORGANIZAR ELEMENTO EM ORDEM DE UMA LISTA
"""nome = ['s', 'w', 't', 'g', 'a', 'b']
valores = [2, 3, 9, 1, 3]
nome.sort()
valores.sort()
print(nome)
print(valores)"""
######################################################################

######################################################################
### ORDEM REVERSA DE UMA LIST


"""nome = ['a', 'b', 'c', 'd']
valores =[1, 2, 3, 4, 5]
nome.sort(reverse=True)
valores.sort(reverse=True)
print(nome)
print(valores)"""
#######################################################################

#######################################################################
## TAMANHO DA LISTA
"""nome = ['a', 'b', 'c', 'd']
valores = [1, 2, 3, 4, 5]
tamanho = (len(nome), len(valores))  # uma tupla
print(tamanho[0])
print(tamanho[1])"""
########################################################################


############################# PRATICA ##################################


#######################################################################
## ADICIONAR VALORES NA LISTA
"""valores = [1, 2, 3, 4, 5]
valores.append(6)
print(valores)"""
########################################################################

########################################################################
## INSERIR VALORES EM UMA LISTA

"""valores = [1, 2, 3, 4, 5]
nome = ['a', 'b', 'c', 'd']
valores.insert(1, 67)  # OBS: 1 É A POSICÃO DA LISTA,,, 67 VAI SER ADICIONADO NA POSICAO 1 DA LISTA
nome.insert(3, 'daniel')
print(valores)
print(nome)"""

##########################################################################


###################  REMOVER ELEMENTO DA LISTA ###########################

##########################################################################
### REMOVER ÚLTIMO ELEMENTO DA LISTA
"""valores = [1, 2, 3, 4, 5]
nome = ['a', 'b', 'c', 'd']
nome.pop()
valores.pop()
print(nome)
print(valores)"""
#########################################################################

#########################################################################
## REMOVER POR POSICÃ0:
"""valores = [1, 2, 3, 4, 5]
nome = ['a', 'b', 'c', 'd']
valores.pop(2)  ## na posicão 2
nome.pop(2)  ## na posicão 2
print(valores)
print(nome)"""
############################################################################

############################################################################
# PERCORRER UMA LISTA PARA ELIMINAR  ELEMENTO

# EX: QUERO ELIMINAR O ELEMENTO 3 DA LISTA
"""lista = [1, 3, 3, 4, 5, 6, 2, 1, 3]
for x in range(len(lista) + 1):
     if 3 in lista:
        lista.remove(3)
print(lista)"""
##############################################################################

##############################################################################
### REMOVER O PRIMEIRO ELEMENTO DA LISTA :
"""valores = [1, 2, 3, 4, 5]

if 4 in valores:
    valores.remove(4)
print(valores)"""
################################################################################

################################################################################
#### ADICIONANDO VALORES NUM LISTA
"""valores = []
valores.append(2)
valores.append(1)
valores.append(3)
for a in valores:
    print(a, end=' ')"""
##################################################################################

##################################################################################
### MOSTRAR A POSICÃO E O ELEMENTO DESSA POSICÃO:
"""lista = [1, 2, 3, 4] 
for x, b in enumerate(lista):
    print(f'NA POSICAO {x}° ENCONTREI O VALOR {b}')"""
# obs ""enumerate "" vai percorrer e mostra elemento da lista
###################################################################################

####################################################################################
###LER VALORES PELO TECLADO E QUARDA NUMA LISTA:
"""valores = []
for x in range(1, 4):
    valores.append(int(input('digite um valor')))

print(valores)"""
####################################################################################

####################################################################################
### LIGACÃO ENTRE DUAS LISTA(SE EU MEXER EM UMA LISTA VAI MEXER TAMBEM NA OUTRA)
"""a = [1, 2, 3, 4, 5]
b = a
b[2] = 5
print(f'LISTA A ={a}')
print(f'LISTA B ={b}')"""
#####################################################################################

#####################################################################################
### COPIA DUAS LISTA
"""a = [1, 2, 3, 4, 5]
b = a[:]

print(f'A LISTA A É {a}')
print(f'A LISTA B É {b}')"""
#######################################################################################

# REMOVER PARÊNTESE  DE VALORES EM UMA LISTA
"""LISTA = [1, 3, 4, 5, 7]
for r in range(0, len(LISTA)):
    LISTA[r] = str(LISTA[r])
x = ' '.join(LISTA)
print(x)"""

###########################################################################################
