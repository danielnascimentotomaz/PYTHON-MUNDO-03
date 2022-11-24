# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em
# uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os
# valores pares e ímpares em ordem crescente


dados = [[], []]
for x in range(1, 8):
    valor = int(input(f'DIGITE O {x}° VALOR:'))
    if valor % 2 == 0:
        dados[0].append(valor)
    else:
        dados[1].append(valor)

dados[0].sort()
dados[1].sort()

print(f'OS VALORES PARES DIGITADOS FORAM {dados[0]}')
print(f'OS VALORES IMPARES DIGITADOS FORAM {dados[1]}')





"""dados = []
conjunto = []

for x in range(1, 8):
    valor = int(input(f'DIGITE O PRIMEIRO {x}° VALOR:'))
    dados.append(valor)
    conjunto.append(dados[:])
    dados.clear()

pares = []
impares = []
for y in conjunto:
    if y[0] % 2 == 0:
        pares.append(y[0])
    elif y[0] % 2 == 1:
        impares.append(y[0])

print('-=-' * 20)
pares.sort()
impares.sort()
print(f'OS VALORES PARES DIGITADOS FORAM {pares}')
print(f'OS VALORES IMPARES DIGITADOS FORAM {impares}')"""

