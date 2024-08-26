# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos
# em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}

dados['Nome'] = str(input('Nome do jogador(a): ')).title().strip()
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

totg = 0
dados['Gols'] = [] 

for x in range(1, partidas+1):
    gols = (int(input(f' - Quantos gols na {x}ª partida: ')))
    dados['Gols'].append(gols)
    totg += gols
    
dados['Total de Gols'] = totg
print(dados)

print('='*30)

for k , v in dados.items():
    print(f'{k}: {v}')
    
print('='*30)

print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')

for y,a in enumerate(dados['Gols']):
    print(f' - Na {y+1}ª Partida, fez {a} gols.')
print(f'Foi um total de {totg} gols.')


# GUANABARA 

# jogador = {}
# partidas = []
# jogador['Nome'] = str(input(f'Nome do jogador: '))
# tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
# for c in range(0 , tot):
#     partidas.append(int(input(f'  Quantos gols na partida {c+1}: ')))
# jogador['Gols'] = partidas[:]
# jogador['Total'] = sum(partidas)

# print(jogador)

# print('='*30)

# for k , v in jogador.items():
#     print(f'{k}: {v}')
    
# print('='*30)

# print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')

# for y,a in enumerate(jogador['Gols']):
#     print(f' - Na {y+1}ª Partida, fez {a} gols.')
# print(f'Foi um total de {jogador["Total"]} gols.')
