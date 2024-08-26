# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada 
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média

idade_acima = []
mulheres = []
lista = []
dados = {}
totp = 0
toti = 0
while True:
    dados['Nome'] = str(input('Nome: ')).title().strip()
    
    while True:
        dados['Sexo'] = str(input('Sexo [M/F]: ')).title().strip()
        if dados['Sexo'] in ['M' ,'F']:
            break
        #if dados['Sexo'] != ['M' , 'F']:
        print(f'Entrada inválida, use [M] para masculino ou [F] para feminino.')   
             
    dados['Idade'] = int(input('Idade: '))
    totp += 1
    lista.append(dados.copy())
    toti += dados['Idade']
    media = toti / totp
    
    if dados['Sexo'] == 'F':
        mulheres.append(dados.copy())
        
        
    if dados['Idade'] > media:
        idade_acima.append(dados.copy())
        
    while True:
        resp = str(input('Quer continuar [S/N]: ')).title().strip()
        if resp in ['S' , 'N']:
            break
        # if resp != ['S','M']:
        print('Entrada inválida, insira [S] para sim e [N] para não')
    if resp == 'N':
        break 
    
print(20*'=')
if totp == 1:
    print(f'Foi cadastrada {totp} pessoa.')
else:
    print(f'Foram cadastradas {totp} pessoas.')
print(20*'=')
    
print(f'A média das idades foi de {media} anos.')

print(20*'=')
print('~~Lista mulheres~~')
for x in mulheres:
    print(f' - {x['Nome']}')

print(20*'=')
print('~~Lista idade acima da media~~')
for m in idade_acima:
    print(f' - {m['Nome']} com {m['Idade']} anos')
  
 
    