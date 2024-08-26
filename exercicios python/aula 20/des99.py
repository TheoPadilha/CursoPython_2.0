# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

import time
def maior(*num):
    m =  (float('-inf'))
    
    print('-='*20)
    print(f'Análisando os valores passados...')
    for n in num:
        if n > m:
            m = n
        print(n,end=' ',flush=True)
        time.sleep(0.4)
        
    print('. ',end='' )
         
    print(f'Foram informados {len(num)} números ao todo.', end='',flush=True )        
    print(f'\nO maior número eh {m}')
    print('-='*20)

# principal
maior(2,8,6,12,9,7)

maior(8,66,102,150050,3)

maior(0)

maior(-3,-7,-10)