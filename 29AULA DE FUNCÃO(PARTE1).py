################ FUNÇÃO def #############################

# EX1 FUNÇÃO SEM PARÂMETRO
#########################################################################################################
"""def mostrar():
    print('-------------------------------')


mostrar()
print('VOU APRENDER PYTHON ')
mostrar()

# obs: toda ver que eu escrever " mostra()" vai aparecer um print com print(--------------------------)"""

########################################################################################################

# EX2
# FUNCÃO COM PARÂMETRO
########################################################################################################
"""def bloco(mensagen):
    print('-=-' * 10)
    print(mensagen)
    print("-=-" * 10)

def ax(b):
    print("-" * 20)
    print(b)
    print('-' * 20)
    

bloco('OLÁ MUNDO')
ax('daniel')"""
#########################################################################################################


######################################### PRATICA ########################################################

# EX3
#########################################################################################################
# SOMA 2 NUMERO
"""def soma(a, b):
    print('-' * 8)
    s = a + b
    print(s)
    print('-' * 8)


soma(2, 6) # print direto
soma(a=3, b=4)

a = int(input('DIGITE PRIMEIRO VALOR:')) # pedindo pra usuario digita o valor
b = int(input('DIGITE SEGUNDO VALOR:'))
soma(a, b)"""

###########################################################################################################

##################### EMPACOTADOR ##################################
# USAR QUANDO NÃO TENHO UM NúMERO FIXO DE ELEMENTO
# obs: "* " USAR QUANDO NAO TEM UMA QUANTIDADE VALORES DETERMINADO

"""def conjunto(*a):
    print("=====" * 11)

    for r in a:
        print(r, end=" ")
    print("FIM")

    print(f"TOTAL DE NUMEROS {len(a)}")

    print("=====" * 11)


conjunto(1, 2, 3, 4, 5, 6)
conjunto(2, 4, 9, 0)"""

#################################################################################
#################################################################################
"""def soma(*a):
    som = 0
    count = 0
    for r in a:
        som = som + r
        count = count + 1
    print("==" * 11)
    print(f"A SOMA O TOTAL È {som}")
    print(f"AO TODO FORAM SOMADO {count} NUMEROS")
    print("==" * 20)


soma(2, 4)
print()
soma(2, 4, 5, 7, 8, 9, 0)"""

####################################################################################
""""def dobra(a):

    pos = 0
    while pos < len(a):
        a[pos] *= 2
        pos = pos + 1



valor = [1, 3, 5, 6, 7]
dobra(valor)
print(valor)
"""
######################################################################################
"""def dobra(s):
    pos = 0
    while len(s) > pos:
        s[pos] *= 2
        pos = pos + 1


dados = []
for a in range(1, 6):
    valor = int(input())
    dados.append(valor)
dobra(dados)
print(dados)"""


############################################################################################

################################### DESEMPACOTAR ###########################################

def dados(*a):
    d = 0
    for r in a:
        d = d + r
    print(f"SOMANDO OS VALORES {a} TOTAL {len(a)} NUMEROS E O TOTAL DA SOMA È {d} ")


dados(1, 4, 8, 9, 0)
