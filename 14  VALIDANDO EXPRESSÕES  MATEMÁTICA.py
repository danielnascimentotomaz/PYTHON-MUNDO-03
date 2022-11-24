

expresao = str(input('DIGITE A EXPRESSÃO:'))

lista  = []
for y in expresao:
    if y == '(':
        lista.append('(')
    elif y == ')':
        if len(lista) > 0:
          lista.remove('(')
        else:
            lista.append(')')
            break


if len(lista) == 0:
   print('SUA EXPRESSÃO ESTA VALIDA')
else:
  print('SUA EXPRESÃO ESTA INVALIDA')
