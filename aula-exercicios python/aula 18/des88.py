# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos 
# # jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
   
    
from random import randint
import time

n = int(input('Quantos jogos que jogar: '))
print(f'Sorteando {n} jogos...') 

for i in range(1 , n+1):
    dados = []
    while len(dados) < 6:
        num = randint(1,60)
        if num not in dados:
            dados.append(num)
    dados.sort()
    print(f'{i}º Jogo: {dados} ')
    time.sleep(1)
    
# Guanabara

# from random import randint
# import time

# lista = []
# jogos = []
# cont = 0
# quant = int(input('Quantos jogos vai jogar?'))
# print(f'Sorteando {quant} jogos...')
# tot = 1
# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1 ,60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1

# for i ,l in enumerate(jogos):
#     print(f'{i+1}º Jogo: {l}')
#     time.sleep(1)