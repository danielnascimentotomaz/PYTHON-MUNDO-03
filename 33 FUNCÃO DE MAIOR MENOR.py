def conjunto(valor):
    maior = menor = count = 0

    while count < len(valor):

        if count == 0:
            maior = valor[count]
            menor = valor[count]

        else:
            if valor[count] > maior:
                maior = valor[count]

            if valor[count] < menor:
                menor = valor[count]
        count = count + 1

    print(f'=-=' * 12)
    print('ANALISANDO OS VALORES PASSADOS....')
    for z in valor:
        print(f'{z}', end=' ')

    print(f'FORAM {len(valor)} VALORES AO TODO.')

    print(f'O MAIOR VALOR INFORMADO FOI {maior}')
    print(f'O MENOR VALOR INFORMADO FOI {menor}')
    print(f'=-=' * 12)


a = [1, 2, 3, 4, 5, 6, 7, 8]
conjunto(a)

conjunto([1, 3, 48, 99, 22])

# OBS; BASE DO PROGRAMA FUNCÃO COM PARAM-ETRO
