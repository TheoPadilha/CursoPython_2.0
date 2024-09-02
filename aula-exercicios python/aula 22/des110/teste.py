# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.


import moeda
# from moeda import aumentar,diminuir,dobro ,metade
# from des110 import moeda

num = float(input('Digite um preço: R$'))
tax = int(input('Informe a taxa em %: '))
moeda.resumo(num,tax)






