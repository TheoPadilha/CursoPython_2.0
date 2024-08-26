# Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont  = ('Zero','Um' , 'Dois' , 'Tres' ,'Quatro','Cinco','Seis','Sete','oito','Nove','dez','onze','dose','trese'
         ,'catorze','quinze','deseseis','desesete','desoito','desenove','vinte')

while True:
    while True:
        n = int(input('Escolha um número entre 0 e 20: '))
        if n >= 0 and n <= 20:
            print(f'Você digitou o número {cont[n]}')
            break
        print('Tente novamente.',end=' ')
            
    
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()
        if resp in ['S' , 'N']:
            break
    print('Entrada inválida. Por favor, insira "S" para sim ou "N" para não.')
        
    if resp == 'N':
        break
print('FIM DO PROGRAMA')

    
    
# Guanabara 
    
# num = ('Zero','Um' , 'Dois' , 'Tres' ,'Quatro','Cinco','Seis','Sete','oito','Nove','dez','onze',
#        'dose','trese','catorze','quinze','deseseis','desesete','desoito','desenove','vinte')

# while True:
#     n = int(input('Digite um número entre 0 e 20: '))
#     if n >= 0 and n <=20:
#         break
#     print('Tente novamente.', end=" ")
    
       
     
# print(f'Você digitou o número {num[n]}')