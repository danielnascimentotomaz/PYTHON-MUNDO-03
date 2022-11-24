import time
a = time.localtime()
dados = dict()

dados['nome'] = str(input('NOME:'))
ano = int(input('ANO DE NASCIMENTO:'))
dados['idade'] = a[0] - ano

dados['carteira'] = int(input('CARTEIRA DE TRABBALHO [0 NÃO TEM]:'))
if dados['carteira'] != 0:
    dados['anocontrataçao'] = int(input('ANO DA CONTRATAÇÃO:'))
    dados['salario'] = float(input('SALARIO: R$ '))
    dados['APOSENTADORIA'] = (dados['anocontrataçao'] - ano) + 35



print('-=-' * 20)

print(f'NOME DO FUNCIONARIO È {dados["nome"]}')
print(f'A IDADE DO FUNCIONARIO È {dados["idade"]}')
print(f'O NUMERO DA CARTEIRA DE TRABALHO DO FUNCIONAIO È {dados["carteira"]}')
print(f'O FUNCIONARIO FOI CONTRATADO NO ANO DE {dados["anocontrataçao"]}')
print(f'O SALARIO DO FUNCIONARIO {dados["nome"]} È R$:{dados["salario"]}')
print(f'O FUNCIONARIO {dados["nome"]} VAI SE APOSENTAR COM {dados["APOSENTADORIA"]} ANOS')
