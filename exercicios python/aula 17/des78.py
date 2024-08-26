# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior 
# e o menor valor digitado e as suas respectivas posições na lista.

num = 0
maior = menor = 0
valores = []
for v in range(0,5):
    valores.append(int(input(f'Digite o {v+1}º valor: '))) # ou 'Digite o valor para a posição {v}: aqui começara do 0.
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
        
print(f'A lista ficou {valores}')
print(f'O maior valor da lista foi {maior}') 
print(f'O menor valor da lista foi {menor}') 

