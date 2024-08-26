# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. 
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.

lista = []
pessoas = []
p = 1
pesado = leve = 0

while True:
    print(f'{p}ª Pessoa')
    p += 1
    
    pessoas.append(str(input('Nome: ')).title().strip())
    pessoas.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesado = leve = pessoas[1]
    else:
        if pessoas[1] > pesado:
            pesado = pessoas[1]
        if pessoas[1] < leve:
            leve = pessoas[1]      
              
    lista.append(pessoas[:])
    pessoas.clear()
    
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()
        if resp in 'SN':
            break
        elif resp != ['S','N']:
            print('Entrada invalida, digite S para "sim" ou N para "Não"')
    if resp == 'N':
        break


print(f'foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {pesado}kg.', end='')
for p in lista:
    if p[1] ==  pesado:
        print(f'[{p[0]}]', end='')
        
print(f'\nO menor peso foi de {leve}kg.',end='')
for p in lista:
    if p[1] == leve:
        print(f'[{p[0]}]', end='')