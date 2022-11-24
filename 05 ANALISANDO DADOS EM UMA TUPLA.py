# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


numero = (int(input('DIGITE UM NÚMERO:')),
          int(input('DIGITE OUTRO NÚMERO:')),
          int(input('DIGITE MAIS UM NÚMERO:')),
          int(input('DIGITE ÚLTIMO NÚMERO:')))

print(f'VOCÊ DIGITOU OS VALORES {numero}')

print(f'O VALOR 9 APARECEU {numero.count(9)} VEZES')

if 3 in numero:  # (SE O 3 TIVER DENTRO DA TUPLA)
    print(f'O VALOR 3 APARECEU NA  {numero.index(3) + 1}° POSICÃO')
else:
    print('O VALOR 3 NÃO FOI DIGITADO EM NENHUMA POSIÇÃO ')

print('OS VALORES PARES DIGITADOS FORAM', end=' ')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')
