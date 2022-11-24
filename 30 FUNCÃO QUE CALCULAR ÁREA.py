def conjunto(a, b):
    print("=================================================")
    print("         CONTROLE DE TERRENOS")
    print("==================================================")
    total = a * b
    print(f'A AREA UM TERRRENO {a:.2f} X {b:.2f} È DE {total:.2f} m²')



for u in range(2):
    print("========================================")
    a = float(input("largura(m)"))
    b = float(input('comprimento(m)'))

    conjunto(a, b)
