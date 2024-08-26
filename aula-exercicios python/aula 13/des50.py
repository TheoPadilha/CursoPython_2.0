# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0
for c in range(1 , 7):
    num = int(input('Insira um número inteiro: '))
    if num % 2 ==0:
        soma += num
        cont += 1
if soma == 0 or soma == 2 or soma == 4 or soma == 6 or soma == 8:
    print(f'A soma do número par deu {soma}')
    print(f'Foi digitado {c} números, porem {cont} é número par.')
else:
    print(f'A soma dos números pares deu {soma}')
    print(f'Foi digitado {c} números, porem {cont} são números pares.')