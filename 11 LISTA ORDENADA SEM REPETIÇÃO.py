"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""
numeros = []
for c in range(5):
    num = int(input('Digite um valor: '))

    for i, v in enumerate(numeros):
        if num < v:
            numeros.insert(i, num)
            break

    if len(numeros) < c + 1:
        numeros.append(num)


print('-=' * 28)
print(f'Os valores digitados em ordem foram: {numeros} ')