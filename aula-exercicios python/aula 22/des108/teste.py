# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


# import moeda
# from moeda import aumentar,diminuir,dobro ,metade
from des108 import moeda

num = float(input('Digite um preço: R$'))
tax = int(input('Informe a taxa em %: '))
print(f'Aumentando {tax}% de {moeda.moeda(num)} temos {moeda.moeda(moeda.aumentar(num,tax))}')
print(f'Diminuindo {tax}% de {moeda.moeda(num)} temos {moeda.moeda(moeda.diminuir(num,tax))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')






