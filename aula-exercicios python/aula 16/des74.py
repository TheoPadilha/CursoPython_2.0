# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random

n1 = random.randrange(0 , 100)
n2 = random.randrange(0 , 100)
n3 = random.randrange(0 , 100)
n4 = random.randrange(0 , 100)
n5 = random.randrange(0 , 100)

nuns = (n1 , n2 , n3 , n4 , n5)
print(nuns)

if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(f'O maior número eh o {n1}')
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print(f'O maior número eh o {n2}')
if n3 > n2 and n3 > n1 and n3 > n4 and n3 > n5:
    print(f'O maior número eh o {n3}')
if n4 > n2 and n4 > n3 and n4 > n1 and n4 > n5:
    print(f'O maior número eh o {n4}')
if n5 > n2 and n5 > n3 and n5 > n4 and n5 > n1:
    print(f'O maior número eh o {n5}')
    
if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
    print(f'O menor número eh o {n1}')
if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    print(f'O menor número eh o {n2}')
if n3 < n2 and n3 < n1 and n3 < n4 and n3 < n5:
    print(f'O menor número eh o {n3}')
if n4 < n2 and n4 < n3 and n4 < n1 and n4 < n5:
    print(f'O menor número eh o {n4}')
if n5 < n2 and n5 < n3 and n5 < n4 and n5 < n1:
    print(f'O menor número eh o {n5}')
    
    
# Guanabara

# from random import randint

# n = ((randint(0 , 100)),(randint(0 , 100)),(randint(0 , 100)),(randint(0 , 100)),(randint(0 , 100)))
# print(f'Os valores sorteados foram: ',end='')
# for num in n:
#     print(f'{num} ',end='')
# print('')
# print(f'O maior número eh o {max(n)}')
# print(f'O menor número eh o {min(n)}')