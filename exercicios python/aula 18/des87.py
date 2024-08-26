# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
# A) A soma de todos os valores pares digitados.  
# B) A soma dos valores da terceira coluna.  
# C) O maior valor da segunda linha.

lista = [[0,0,0],[0,0,0],[0,0,0]]
Spar = maiL = scol = 0
for l in range(0 , 3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^5}]',end='')
        if lista[l][c] % 2 == 0:
            Spar += lista[l][c]
    print()
print(f'A soma dos pares é : {Spar}')
for l in range(0,3):
    scol += lista[l][2]
print(f'A soma dos números da tertceira coluna é : {scol}')

for c in range(0,3):
    if lista[1][c] >= maiL:
        maiL = lista[1][c]
print(f'O maior valor da segunda linha é : {maiL}') 