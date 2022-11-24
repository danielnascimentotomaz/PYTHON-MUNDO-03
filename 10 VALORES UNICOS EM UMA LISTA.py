dados = []

while True:

    valores = float(input('DIGITE UM VALOR:'))
    if valores not in dados:
        dados.append(valores)
        print('ADICIONADO COM SUCESSO...')
    else:
        print('VALOR DUPLICADO NÃO VOU ADICIONAR')

    continuar = str(input('QUER CONTINUAR [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('DADO INVALIDO, TENTE NOVAMENTE.QUER CONTINUAR [S/N]')).upper().strip()[0]

    if continuar == 'N':
        break

print(f'VOÇÊ DIGITOU OS VALORES {sorted(dados)}')
