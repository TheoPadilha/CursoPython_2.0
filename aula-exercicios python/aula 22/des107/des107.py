# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
# from moeda import aumentar,diminuir,dobro ,metade

num = float(input('Digite um preço: R$'))
tax = float(input('Informe a taxa em %: '))
print(f'Aumentando {tax}% de {(num)} temos {(moeda.aumentar(num,tax))}')
print(f'Diminuindo {tax}% de {(num)} temos {(moeda.diminuir(num,tax))}')
print(f'O dobro de {(num)} é {(moeda.dobro(num))}')
print(f'A metade de {(num)} é {(moeda.metade(num))}')






