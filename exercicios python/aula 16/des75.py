# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.

# B) Em que posição foi digitado o primeiro valor 3.

# C) Quais foram os números pares.


nuns = (int(input('1º Valor: ')),
int(input('2º Valor: ')),
int(input('3º Valor: ')),
int(input('4º Valor: ')))
print(f'Você digitou os valores {nuns}')

print(f'O número 9 apareceu {nuns.count(9)} vezes.')
if 3 in nuns:
    print(f'O número 3 apareceu na {nuns.index(3) +1}ª posição,')
else:
    print('O número 3 não apareceu.')
par = 0
print(f'os números pares foram:' , end=' ')
for c in nuns:
    if c % 2 == 0:
        par += 1
        print(c, end=' ')
print(' ')
print(f'Apareceu {par} números pares')
        
