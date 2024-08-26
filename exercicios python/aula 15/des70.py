# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
# continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.

print('-+'*10)
print('LOJAS MITHE')
print('-+'*10)

totP = prod1000 = quantP = barato = 0
nomeB = ' '
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    totP += preço
    quantP += 1
    
    if preço > 1000:
        prod1000 += 1
    
    if quantP == 1: # or preço < barato 
        barato = preço
        nomeB = nome
    else:
       if preço < barato: 
            barato = preço
            nomeB = nome

    while True:
        avançar = str(input('Quer continuar [S/N]: ')).capitalize().strip()
        if avançar in ['S' , 'N']:
            break
        print('Entrada inválida. Por favor, insira "S" para sim ou "N" para não.')
        
    if avançar == 'N':
        break
print(f'{'FIM DO PROGRAMA':-^40}')
print(f'Você gastou um total de R${totP:.2f} nessas compra.')
if prod1000 == 1:
    print(f'{prod1000} produto custa mais de R$ 1000 ')
else:
    print(f'{prod1000} produtos custam mais de R$ 1000 ')
print(f'O produto mais barato é o {nomeB} e seu preço é R$ {barato}')