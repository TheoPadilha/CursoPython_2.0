# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados 
# em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
import time
from operator import itemgetter
a ={}

a['1º Jogador'] = randint(1 ,6)
a['2º Jogador'] = randint(1 ,6)
a['3º Jogador'] = randint(1 ,6)
a['4º Jogador'] = randint(1 ,6)


print('JOGANDO...')
time.sleep(1)
r ={} 
for x, y in a.items():
    print(f'{x} tirou {y} no dado.')
    time.sleep(1)
    
r = sorted(a.items(), key=itemgetter(1) , reverse=True)
print('='*30)

print(f'{'RANKING DOS JOGADORES':^30}')
for t ,m in enumerate(r):
    print(f'{t+1}º lugar: {m[0]} com {m[1]} no dado.')
    time.sleep(1)