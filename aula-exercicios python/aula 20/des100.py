# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
# e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sortear(num):
    print('Sorteando 5 valores da lista: ',end='')
    for x in range(0,5):
        n = (randint(1,10))
        num.append(n)
        sleep(0.4)
        print(f'{n}',end=' ',flush=True)
    print()    
    
    
def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'A soma dos números pares da lista {lista} foi {soma}')
        
numeros = []
sortear(numeros)
somaPar(numeros)