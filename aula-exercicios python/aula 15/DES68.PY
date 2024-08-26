# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

print('-'*30)
print('Vamos jogar par ou impar')
print('-'*30)

vitoria = 0
escolha = ' '
while True:
    computador = random.randint(0 , 10)
    num = int(input('Diga um valor: '))
    if (num + computador) % 2 == 0:
        escolha = 'PAR'
    elif (num + computador) % 2 == 1:
        escolha = 'IMPAR'
    while True:   
        eu = str(input('Par ou Impar [P/I]: ')).upper().strip()
        if eu == 'P':
            eu = 'PAR'
            break
            
        elif eu == 'I':
            eu = 'IMPAR'
            break
        
        elif eu != 'P' or eu != 'I':
            print('Erro tente novamente!')
            continue
    
    print(f'Você jogou {num} e o computador {computador}. Total de {num+computador}, deu {escolha}')
    if eu == escolha:
        print('Você venceu')
        print('Vamos jogar novamente...')
        vitoria += 1
    if escolha != eu:
        print('Você perdeu.')
        break
if vitoria > 1:
    print(f'GAME OVER! Você venceu {vitoria} vezes.')
else:
    print(f'GAME OVER! Você venceu {vitoria} vez.')


# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Guanabara
# import random

# vitoria = 0
# while True:
#     jogador = int(input('Digite um valor: '))    
#     computador = random.randint(0 , 10)
#     total = jogador + computador
#     tipo = ' '
#     while tipo not in 'PI':
#         tipo = str(input('Par ou impar [P/I]: ')).upper().strip()
#     print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, deu ', end='')
#     if total % 2 == 0:
#         print('PAR')
#     else:
#         print('IMPAR')
    
#     if tipo == 'P':
#         if total % 2 == 0:
#             print('Você venceu!')
#             vitoria += 1
#         else:
#             print('Você perdeu')
#             break
#     elif tipo == 'I':
#         if total % 2 == 1:
#             print('Você venceu')
#             vitoria += 1
#         else:
#             print('Você perdeu')
#             break
#     print('Vamos jogar novamente...')
# print(f'GAME OVER! Você venceu {vitoria} vezes.')