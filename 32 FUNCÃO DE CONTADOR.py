from time import sleep


def contador(a, b, c):
    print("==" * 20)

    if c < 0:
        c = c * (-1)
    if c == 0:
        c = 1

    print(f'CONTAGEM DE {a} ATÉ {b} DE {c} EM {c}')


    if a < b:
        count = a
        while count <= b:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count = count + c
        print()
        print("==" * 20)

    elif a > b:
        count = a
        while count >= b:
            print(f'{count}', end=' ', flush=True)
            sleep(0.5)
            count = count - c
        print()
        print('==' * 20)


contador(0, 20, 2)

contador(20, 0, 2)

print('AGORA É SUA VEZ DE PERSONALIZAR  A CONTAGEM !')
inicio = int(input('INICIO:'))
fim = int(input('FIM:'))
passo = int(input('PASSO:'))
contador(inicio, fim, passo)
