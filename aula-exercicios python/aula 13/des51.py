# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos 
# dessa progressão.

print('='*25)
print(' 10 TERMOS DE UMA PA')
print('='*25)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10) * razao
for c in range(primeiro, decimo, razao):
    print(f'{c}', end=' ➡  ')
print('ACABOU')
    
    