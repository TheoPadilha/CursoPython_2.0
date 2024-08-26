# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0

for c in range(1 , num + 1):
    
    if num % c == 0:
        print('\033[32m', end="")
        tot += 1 
    else:
        print('\033[31m', end=' ')
    print(f'{c}',end=' ')
    
print(f'\033[m \nO número {num} foi divisivel {tot} vezes')

if tot == 2:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')