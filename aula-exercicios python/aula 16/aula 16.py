# TUPLAS

# Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis 
# que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

# tuplas são imutaveis

Lanche = ('Hamburger' , 'Chocolate' , 'Refri' , 'Pizza' , 'Batata Frita')
print(Lanche)
print(Lanche[2])
print(Lanche[-3])
print(Lanche[0:3])
print(Lanche[:2])
print(Lanche[2:])

print('======================')

print(len(Lanche))
for cont in range(0 , len(Lanche)):
    print(f'Vou comer {Lanche[cont]} na posição {cont}')

print('======================')

for c in Lanche:
    print(f'Vou comer {c}')    #Se Não precisar da posição do alimento usar esse.
print('QUE GOSTOSOOO')

print('======================')

for pos, c in enumerate(Lanche):  #enumerate() Serve para mostrar a posição do item.
    print(f'Vou comer {c} na posição {pos}')

print('======================')

print(sorted(Lanche)) # sorted() Vai organizar em ordem alfabetica a sua tupla.

print('======================')

a = (2 , 4 , 6 , 8 , 10)
b = 1 , 3 , 5 , 7 , 9
c = a + b
print(c)
print(len(c))
print(c.count(3)) # .cont() Conta quantos vezes o elemneto dentro do () apareceu.   
print(c.index(5)) # .index() Mostra qual a posição do elemento dentro do ().

pessoa = ('Theo' , 19 , 'Masculino' , 71.00)
del(pessoa) # del() Apaga completamente a variavel.