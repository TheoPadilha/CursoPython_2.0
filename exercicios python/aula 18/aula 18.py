# LISTAS PART 2
dados = []
dados.append('Theo')
dados.append(19)

pessoas = [['Mih',18],['Jose',19],['Cida',59]]
pessoas.append(dados[:])

print(f'Dados: {dados}')
print(f'Pessoas: {pessoas}')

print(pessoas[0][0])
print(pessoas[3][0])
print(pessoas[1])

print(20*'-')

p = []
p.append('Maria')
p.append(70)

g = []
g.append(p[:])
p[0] = 'Jose'
p[1] = 18
g.append(p[:])

print(g)

print(20*'-')

time = [['Theo',19], ['Jose',19] , ['Felipe',18] , ['Vitor',20] , ['Mlk',21]]
for t in time:
    print(f'{t[0]} tem {t[1]}anos de idade.')

print(20*'-')

pepol = []
da = []
for c in range(1,4):
    print(f'{c}ª Pessoa.')
    da.append(str(input('Nome: ')))
    da.append(int(input('Idade: ')))
    pepol.append(da[:])
    da.clear()
    
for i in pepol:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idade.')
    else:
        print(f'{i[0]} é menor de idade.')


