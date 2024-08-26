# Exercício  Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listPar = []
listImpar =[]

while True:
    n =(int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        listPar.append(n)
    if n % 2 == 1:
        listImpar.append(n)
        
    while True:
        resp = str(input('Quer continuar [S/N]:')).strip().upper()
        if resp in 'SN':
            break
        if resp != ['S' , 'N']:
            print('Entrada inválida. Por favor, insira "S" para sim ou "N" para não.')
    if resp in 'Nn':
        break
    
    
print(f'A lista completa é: {lista}')
print(f'A lista dos números pares é: {listPar}')
print(f'A lista dos números impares é: {listImpar}')

# Guanabara

# num = []
# pares = []
# impares = []

# while True:
#     num.append((int(input('Digite um valor: '))))
#     resp = str(input('Quer continuar [S/N]: '))
#     if resp in 'Nn':
#         break
# for i, v in enumerate(num): 
#     if v % 2 == 0:
#         pares.append(v)
#     if v % 2 == 1:
#         listImpar.append(v)

# print(f'A lista completa é: {lista}')
# print(f'A lista dos números pares é: {listPar}')
# print(f'A lista dos números impares é: {listImpar}')