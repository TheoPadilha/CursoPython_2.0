# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

import datetime

ano_atual = datetime.date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    
    ano_nasc = int(input(f'Informe o ano de nascimento da {c}ª pessoa: '))
    idade = ano_atual - ano_nasc

    if idade < 21:
        print(f'A {c}ª é de menor com {idade} anos.\n')
        totmenor += 1
    else:
        print(f'A {c}ª é de maior com {idade} anos.\n')
        totmaior += 1
print(f'No total são {totmenor} pessoas de menor e {totmaior} pessoas de maior.')