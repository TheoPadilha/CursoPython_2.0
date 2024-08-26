# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

dados = {}
lista = []
while True:
    dados['Nome'] = str(input('Nome do jogador(a): ')).title().strip()
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

    totg = 0
    dados['Gols'] = [] 

    for x in range(1, partidas+1):
        gols = (int(input(f' - Quantos gols na {x}ª partida: ')))
        dados['Gols'].append(gols)
        totg += gols
    dados['Total de Gols'] = totg
    lista.append(dados.copy())
    
    while True:
        resp = str(input('Quer continuar [S/N]: ')).title().strip()
        if resp in ['S' , 'N']:
            break
        print('Entrada inválida, insira [S] para sim ou [N] para não.')
    if resp == 'N':
        break
    
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*30)
for i,x in enumerate(lista):
    print(f'{i+1:>3} ', end='')
    for d in x.values():
        print(f'{str(d):<15}',end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador (999 pra parar): '))-1
    if busca == 998:
        break
    if busca >= len(lista):
        print(f'ERRO não exite jogador com o codigo {busca+1}')
    else:
        print(f'levantamento do jogador {lista[busca]['Nome']}:')
        for i, g in enumerate(lista[busca]['Gols']):
            print(f' - No jogo {i +1} fez {g} gols.')
