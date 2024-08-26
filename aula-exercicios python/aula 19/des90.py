# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

dados = {}

dados['Nome'] = str(input('Nome: ')).title().strip()
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))

if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'

for a, b in dados.items():
    print(f' - {a}: {b}')
