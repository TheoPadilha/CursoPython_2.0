# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


# import moeda
# from moeda import aumentar,diminuir,dobro ,metade
from des109 import moeda

num = float(input('Digite um preço: R$'))
tax = int(input('Informe a taxa em %: '))
print(f'Aumentando {tax}% de {moeda.moeda(num)} temos {(moeda.aumentar(num,tax,True))}')
print(f'Diminuindo {tax}% de {moeda.moeda(num)} temos {(moeda.diminuir(num,tax,True))}')
print(f'O dobro de {moeda.moeda(num)} é {(moeda.dobro(num,True))}')
print(f'A metade de {moeda.moeda(num)} é {(moeda.metade(num,True))}')






