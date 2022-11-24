matricula = []
nota1 = []
nota2 = []
nota3 = []
faltas = []
l_media = []

while True:
    # menu
    print("=" * 47)
    print("\t\tmenu")
    print("=" * 47)
    print("\nCadastrar aluno............................:[1]")
    print("Remover aluno..............................:[2]")
    print("Imprimir médias............................:[3]")
    print("Informar melhor aluno......................:[4]")
    print("Listar alunos reprovados por falta.........:[5]")
    print("Informar dados estatísticos................:[6]")
    print("Digite zero para encerrar..................:[0]")
    n = int(input())

    if n == 0:
        break
    # notas
    elif n == 1:
        m = int(input("Insira a matricula do aluno:"))
        matricula.append(m)
        m = int(input("digite sua nota 1:"))
        while m < 0 or m > 10:
            print("erro")
            m = int(input("digite sua nota 1:"))
        nota1.append(m)
        m = int(input("digite sua nota 2:"))
        while m < 0 or m > 10:
            print("erro")
            m = int(input("digite sua nota 2:"))
        nota2.append(m)
        m = int(input("digite sua nota 3:"))
        while m < 0 or m > 10:
            print("erro")
            m = int(input("digite sua nota 3:"))
        nota3.append(m)
        m = int(input("Insira a quantidade de falta do aluno:"))
        faltas.append(m)

    # remover aluno
    elif n == 2:
        t = int(input("Insira a matricula do aluno que deseja remover:"))
        for i in range(len(matricula)):
            if t == matricula[i]:
                matricula.remove(t)
                t = nota1[i]
                print("aluno removido")
                nota1.remove(t)
                t = nota2[i]
                nota2.remove(t)
                t = nota3[i]
                nota3.remove(t)
                t = faltas[i]
                faltas.remove(t)
            else:
                print("matricula inexistente")
        if (len(matricula)) == 0:
            print("nenhum aluno cadastrado.")
    # media
    elif n == 3:
        for x in range(len(matricula)):
            media = ((nota1[x] + nota2[x] + nota3[x]) / 3)
            print("matricula:", matricula[x], end=' ')
            print("media:", media)

    # maior media
    elif n == 4:
        for x in range(len(matricula)):
            l = ((nota1[x] + nota2[x] + nota3[x]) / 3)
            l_media.append(l)
        maior_media = max(l_media)
        print("matricula:", matricula[x], end=' ')
        print("media:", maior_media)

    # faltas
    elif n == 5:
        for x in range(len(matricula)):
            if faltas[x] > 17:
                print("matricula:", matricula[x], end=' ')
                print("reprovado por falta.")
    # dados estatisticos
    elif n == 6:
        media_geral = 0
        contador = 0
        contador_f = 0
        contador_ap = 0
        for x in range(len(matricula)):
            if faltas[x] > 17:
                contador_f = contador_f + 1
        for i in range(len(nota1)):
            l = ((nota1[i] + nota2[i] + nota3[i]) / 3)
            if l < 5:
                contador = contador + 1
            else:
                contador_ap = contador_ap + 1
            l_media.append(l)
            media_geral = media_geral + l
            if (len(l_media)) != 0:
                media_geral = (media_geral / (len(nota3)))
            else:
                media_geral = 0
        print("media geral:", media_geral)
        print("quantidade de alunos reprovados por media:", contador)
        print("quantidade de alunos reprovados por falta:", contador_f)
        print("quantidade de alunos aprovados:", contador_ap)

print("FIM")
