# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: 
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada: 
# a) de 1 até 10, de 1 em 1          
# b) de 10 até 0, de 2 em 2       
# c) uma contagem personalizada

import time

def contador(inicio , fim , passo):
    
    if passo < 0:
        passo*= -1
    if passo == 0:
        passo = 1
            
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if passo < 0:
        passo*= -1
    if passo == 0:
        passo = 1
    
    
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}',end=' ' , flush=True)
            time.sleep(0.5)
            cont += passo
        print('.')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}',end=' ',flush=True)
            time.sleep(0.5)
            cont -= passo
        print('.')
        
contador(1, 10, 1)

contador(100, 0 , 10)

print('Agora é sua vez de personalizar a contagem')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: ')) 

contador(i,f,p)

