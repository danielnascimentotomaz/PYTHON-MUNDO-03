ficha = []

while True:
    print('--------------------- \033[0;31mBOLETIM\033[m --------------------')
    print('CADRASTRAR ALUNO...............................[1]')
    print('MOSTRAR TODOS ALUNO CADRASTRADO E SUA MEDIA....[2]')
    print('MOSTRAR AS NOTAS DO ALUNO......................[3]')
    print('REMOVER ALUNO..................................[4]')
    print('ENCERRAR PROGRAMA .............................[0]')

    x = int(input())
    while x < 0 or x > 4:
        x = int(input('OPÇÃO INVALIDA. DIGITE UMA OPÇÃO VALIDA'))

    if x == 1:
        nome = str(input('NOME:'))

        nota = float(input('nota 1 :'))
        while nota < 0 or nota > 10:
            nota = float(input('NOTA INVALIDA..DIGITE A NOTA 1 NOVAMENTE:'))

        nota1 = float(input('nota 2 :'))
        while nota1 < 0 or nota1 > 10:
            nota1 = float(input('NOTA INVALIDA..DIGITE A NOTA 2 NOVAMENTE:'))

        nota2 = float(input('nota 3 :'))
        while nota2 < 0 or nota2 > 10:
            nota2 = float(input('NOTA INVALIDA..DIGITE A NOTA 3 NOVAMENTE:'))
        media = (nota + nota1 + nota2) / 3
        ficha.append([nome, [nota, nota1, nota2], media])


    elif x == 2:
        print('=-=' * 20)
        print(f'{"POSICÃO:":<4} {"NOME:":<10}{"MEDIA:":>8}')
        print('---' * 19)
        for t, f in enumerate(ficha):
            print(f' {t:<6}{f[0]:<10}{f[2]:>8.1f}')

    elif x == 3:
        p = int(input('QUAL POSICÃO DO ALUNO QUE PARA MOSTRA AS NOTAS:'))
        if p <= len(ficha) - 1:
            print('---' * 17)
            print(f'AS NOTAS DE {ficha[p][0]} SÃO {ficha[p][1]}')
            print('---' * 17)
        else:
            print('\033[0;31mESSE ALUNO NÃO ESTAR CADRASTRADO.\033[m')

    elif x == 4:
        p = int(input('QUAL POSICÃO DO ALUNO QUE DESEJA REMOVER:'))
        if p <= len(ficha) - 1:
            ficha.remove(ficha[p])
        else:
            print('\033[0;31mESSE ALUNO NÃO ESTAR CADRASTRADO.\033[m')


    elif x == 0:
        break

print('FIM DO PROGRAMA...')