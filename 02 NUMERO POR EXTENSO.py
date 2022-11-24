# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
# até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

nomes = ('UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO',
         'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE',
         'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
    while True:
        valor = int(input('DIGITE UM VALOR:'))
        if 0 <= valor <= 20:
            break
        print('TENTE NOVAMENTE', end=' ')

    print(f'VOCÊ DIGITOU O NÚMERO {nomes[valor -1]}')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('QUER  CONTINUAR [S/N]')).upper().strip()[0]
        if continuar != 'S' and continuar != 'N':
            print('TENTE NOVAMENTE', end=' ')
    if continuar == 'N':
        break



print('=== FIM DO PROGRAMA ===')

################  PROGRAMA SIMPLE ###################

"""lista = 'ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', \
        'DEZ', 'ONZE', 'DOZE', 'TREZE', 'CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', \
        'DEZOITE', 'DEZENOVE', 'VINTE'

while True:

    while True:
        num = int(input('DIGITE UM VALOR ENTRE 0 E 20:'))
        if 0 <= num <= 20:
            break
        print('TENTE NOVAMENTE.', end='')

    print(f'VOCÊ DIGITOU O NUMERO {lista[num]}')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUER CONTINUAR [S/N]')).upper().strip()[0]

    if resp == 'N':
        break

print('===FIM DO PROGRAMA===')"""
