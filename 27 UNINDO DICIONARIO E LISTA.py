from time import sleep

dados = dict()
conjunto = []
mulher = []
homen = []
while True:
    print()
    print('================== \033[0;34mCADASTRO DE DADO\033[m =====================')
    print('=' * 59)
    print('ADICIONAR UMA PESSOA....................................[1]')
    print('TOTAL DE PESSOA CADASTRADA..............................[2]')
    print('MOSTRA TODAS PESSOA CADATRADA...........................[3]')
    print('NOME DAS MULHERES CADASTRADA............................[4]')
    print('NOME DOS HOMEM CADASTRADA...............................[5]')
    print('REMOVER UMA PESSOA......................................[8]')
    print('ENCERRAR O  PROGRAMA....................................[9]')
    print('=' * 59)

    opcao = int(input('\033[0;31mDIGITE A OPCÃO:\033[m'))
    print('=' * 59)
    print()

    while opcao < 1 or opcao > 8:
        print('OPÇÃO INVALIDA! POR FAVOR DIGITE UMA OPÇÃO VALIDA')
        opcao = int(input('\033[0;31mDIGITE A OPCÃO:\033[m'))

    if opcao == 1:
        dados.clear()
        dados['Nome'] = str(input('NOME:'))

        dados['Sexo'] = str(input('SEXO: [M/F] ')).upper().strip()[0]
        while dados['Sexo'] not in 'MF':
            print('ERR0 !... POR FAVOR, DIGITE  APENAS M OU F')
            dados['Sexo'] = str(input('SEXO: [M/F]')).upper().strip()[0]

        dados['Idade'] = int(input('IDADE:'))
        while dados['Idade'] < 0:
            print('IDADE INVALIDA. DIGITE UMA IDADE VALIDA')
            dados['Idade'] = int(input('IDADE:'))

        conjunto.append(dados.copy())


    elif opcao == 2:
        totalcadastro = len(conjunto)
        if totalcadastro == 0:
            print('NÃO EXISTIR PESSOA CADASTRADA')
        else:
            print(f'>>>>AO TODO TERMOS {totalcadastro} PESSOAS CADASTRADAS')





    elif opcao == 3:
        for y, o in enumerate(conjunto):
            print(f'POSIÇÃO = {y + 1} <> NOME = {o["Nome"]} <> SEXO = {o["Sexo"]} <> IDADE = {o["Idade"]}')




    elif opcao == 4:

        mulher.clear()  # limpar lista cada laco
        for t in conjunto:
            if t['Sexo'] == 'F':
                mulher.append(t["Nome"])
        if len(mulher) > 0:
            print('AS MULHERES CADASTRADA FORAM:')
            for l in mulher:
                print(f'>>>{l}')
        else:
            print(f'>>> NÃO EXISTIR MULHERES CADASTRADA.')

    if opcao == 5:
        homen.clear()
        for k in conjunto:
            if k['Sexo'] == 'M':
                homen.append(k['Nome'])
        if len(homen) > 0:
            print('OS HOMEM CADASTRADA FORAM:')
            for t in homen:
                print(f'>>>{t}')
        else:
            print('NÃO EXISTIR HOMEM CADASTRADO')

    elif opcao == 8:
        if len(conjunto) > 0:
            print('QUAL A POSIÇÃO DA PESSOA QUE DESEJA REMOVER:')
            P = int(input())
            del (conjunto[P - 1])
        else:
            print('>>>>NÃO  EXISTIR NENHUMA PESSOAS CADASTRADA.')
            print('=' * 59)

    elif opcao == 9:
        print(conjunto)
        print('ENCERRANDO O PROGRAMA...')
        sleep(2)
        break

print('=== FIM ===')
