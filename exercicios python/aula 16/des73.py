# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Vasco.



times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Bahia', 'Cruzeiro', 'São Paulo', 'Fortaleza', 'Athletico-PR', 'Atlético-MG', 'Bragantino',
         'Vasco', 'Internacional', 'Juventude', 'Criciúma', 'Cuiabá', 'Vitória', 'Corinthians', 'Grêmio', 'Atlético-GO', 'Fluminense')

print(f'Tabela do Brasileirão: {times}')

print('=-'*45)

print(f'Os primeiros 5 colocados são {times[:5]}')

print('=-'*45)

print(f'Os ultimos 4 colocados são {times[-4:]}')

print('=-'*45)

print(f'Os times em ordem alfabética ficam {sorted(times)}')

print('=-'*45)


print(f'O Vasco está na {times.index('Vasco')+1}ª posição.')