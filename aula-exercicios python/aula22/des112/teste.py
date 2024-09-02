# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.


# import moeda
# from moeda import aumentar,diminuir,dobro ,metade


from utilidadecev import moeda
from utilidadecev import dado

num = dado.leiaDinherio(('Digite um preço: R$'))
tax = int(input('Informe a taxa em %: '))
moeda.resumo(num,tax)






