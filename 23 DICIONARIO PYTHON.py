dados = dict()
dados['nomes'] = str(input('NOME:'))

dados['media'] = float(input(f'MEDIA DE {dados["nomes"]}.'))
while dados['media'] < 0 or dados['media'] > 10:
    dados['media'] = float(input(f'MEDIA DE {dados["nomes"]}.'))

print('-=-' * 20)

print(f'   - NOME E IQUAL A {dados["nomes"]}')
print(f'   - A MEDIA È IQUAL {dados["media"]}')
if dados['media'] >= 7:
    print(f'   - SITUAÇÃO APROVADO')
elif 5 <= dados['media'] < 7:
    print(f'   - SITUAÇÃO RECUPERACÃO')
else:
    print('   - SITUAÇÃO REPROVADO')
