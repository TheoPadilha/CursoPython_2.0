# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
import datetime
dados ={}
ano_atual = datetime.datetime.now().year

dados['Nome'] = str(input('Nome: ')).strip().capitalize()
ano_nasc = int(input('Ano de Nascimento: '))
dados['Idade'] = ano_atual - ano_nasc
dados['Ctps'] = int(input('Carteira de trabalho (0 se não houver): '))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - ano_atual)
    
print('='*20)  
for x ,y in dados.items():
    print(f' - {x}: {y}')