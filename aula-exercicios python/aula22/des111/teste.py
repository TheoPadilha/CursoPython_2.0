# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.


# import moeda
# from moeda import aumentar,diminuir,dobro ,metade


from utilidadecev import moeda

num = float(input('Digite um preço: R$'))
tax = int(input('Informe a taxa em %: '))
moeda.resumo(num,tax)






