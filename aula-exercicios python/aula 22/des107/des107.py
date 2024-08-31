# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moedas

num = float(input('Digite um preço: R$'))
print(f'Aumentando 10% de {num} temos {moedas.aumentar(num)}')
print(f'Diminuindo 10% de num temos {moedas.diminuir(num)}')
print(f'O dobro de {num} é {moedas.dobro(num)}')
print(f'A metade de {num} é {moedas.metade(num)}')






