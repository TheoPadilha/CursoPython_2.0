# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]
for l in range(1 , 8):
    n = (int(input(f'Digite o {l}º valor: ')))
    if n % 2 == 0:
        lista[0].append(n)
    if n % 2 == 1:
        lista[1].append(n) 


print(f'Os números pares da lista são: {sorted(lista[0])}.')    

print(f'Os números impares da lista são: {sorted(lista[1])}')
    
