# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
# from moeda import aumentar,diminuir,dobro ,metade

num = float(input('Digite um preço: R$'))
tax = int(input('Informe a taxa em %: '))
print(f'Aumentando {tax}% de {moeda.moeda(num)} temos {moeda.moeda(moeda.aumentar(num,tax))}')
print(f'Diminuindo {tax}% de {moeda.moeda(num)} temos {moeda.moeda(moeda.diminuir(num,tax))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')






