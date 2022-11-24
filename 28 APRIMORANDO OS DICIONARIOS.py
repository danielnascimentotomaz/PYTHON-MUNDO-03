from time import sleep
dados = dict()
gol = []
dadoscompleto = []
while True:
    print()
    print('==============\033[0;32m CADASTRO DE JOGADOR\033[m ================')

    print('==' * 26)
    print('CADASTRAR O JOGADOR.............................[1]')
    print('DADOS DE TODOS OS JOGADOR CADASTRADO............[2]')
    print('REMOVER  JOGADOR................................[3]')
    print('TOTAL DE JOGADORES CADASTRADOS..................[4]')
    print('MOSTRA O DADOS INDIIDUAL DE CADA JOGADOR........[5]')
    print('ENCERRAR O PROGRAMA.............................[6]')

    print('==' * 26)

    n = int(input('\033[34mDIGITE A OPÇÃO:\033[m'))
    while n < 0 or n > 7:
        print('\033[0;31mERRO... DIGITE UMA OPÇÃO VALIDA.\033[m')

        n = int(input('\033[34mDIGITE A OPÇÃO:\033[m'))



    if n == 1:
        dados.clear()  # limpar o dicionario para cada  novo laço
        dados['NOMES'] = str(input('NOME DO JOGADOR:'))

        total = int(input(f'QUANTAS PARTIDA {dados["NOMES"]} JOGOU:'))
        if total > 0:

            gol.clear()  # limpar a lista de gol para cada novo laco
            for t in range(1, total + 1):
                gol1 = int(input(f'QUANTOS GOLS NA {t}° PARTIDA :'))
                gol.append(gol1)
            dados['Gol'] = gol[:]
            dados['Total'] = sum(gol)

        dadoscompleto.append(dados.copy())

    elif n == 2:
        for y, x in enumerate(dadoscompleto):
            print(f'POSIÇÃO {y} >>> NOME = {x["NOMES"]}>>> GOL {x["Gol"]} >>> TOTAL DE {x["Total"]}')
    elif n == 3:
        print('QUAL A POSICÃO DO JOGADOR QUE DESEJA EXCLUIR')
        F = int(input())
        del (dadoscompleto[F])
    elif n == 4:
        print(f'O TOTAL DE JOGADORES CADASTRADO FORAM {len(dadoscompleto)}')

    elif n == 5:
        print('QUAL A POSICÃO DO JOGADOR QUER DESEJA ER OS DADOS')
        A = int(input())

        if A <= len(dadoscompleto):
            print(f'LEVANTAMENTO DO JOGADOR {dadoscompleto[A]["NOMES"]}')
            for s, l in enumerate(dadoscompleto[A]["Gol"]):
                print(f'>>>>>>NO JOGO {s} FEZ {l}')

    elif n == 6:
        print('ENCERRANDO O PROGRAMA...')
        sleep(2)
        break


print('--- FIM---')