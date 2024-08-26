# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                 
# Depois disso, mostre:                                                                                                            
# A) Quantos números foram digitados.                                                              
# B) A lista de valores, ordenada de forma decrescente.                                                                                      
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    lista.sort(reverse=True)
    
    
    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
        if resp != ['N' , 'S']:
            print('Entrada inválida. Por favor, insira "S" para sim ou "N" para não.')
    if resp in'N':
        break
print(f'Foram digitados {len(lista)} Números.')
print(f'A lista ordenada de forma decrescente fica {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')