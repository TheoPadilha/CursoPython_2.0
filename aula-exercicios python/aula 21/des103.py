# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='',gols =0):
    if nome == '':
        resp = '<desconhecido>'
    else:
        resp = nome
    if gols == '':
        respG = 0
    else:
        respG = gols
    a = (f'O jogador {resp} fez {respG} gols na partida.')
    return a
    

n = str(input('Nome do jogador: ')).title().strip()
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
print(ficha(n,g))