# Listas in Python

lanche = ['Pizza' , 'Refrigerante' , 'Chocolate' , 'Pastel']
print(lanche)

print(lanche[2])

lanche[3] = 'Macarrao'
print(lanche)

lanche.append('Hotdog') #.append() Adiciona o item dentro do () à lista.
print(lanche)

lanche.insert(1, 'salgadinho' ) #.insert(n , '') Adiciona a string no endereço que vc digitar.
print(lanche)

del lanche[4] # del ..... Deleta o item do endereço selecionado.
lanche.pop(4) # .pop(n) Deleta o item do endereço selecionado.
lanche.pop() # .pop() Remove o ultimo item da lista. 

# lanche.remove('Refrigerante')
if 'Refrigerante' in lanche:
    lanche.remove('Refrigerante')
    print('Refrigerante removido com secesso!')
else:
    print('Refrigerante não esta na lista')
print(lanche)


valores = list(range(2 , 10))
print(valores)

valores = [8,6,4,2,1,3,9,7,5]
print(valores)

valores.sort()
print(valores)

valores.sort(reverse=True)
print(valores)

print(len(valores)) # len() Mostra o tamanho da lista ,como no exemplo valores tem 9 elementos!

valores = []
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))
print(valores)  


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o número {v}')
    

a = [1,3,6,5]
b = a    # Fazendo b = a estamos fazendo uma ligação de lista.
b = a[:] # Assim estam,os fqazendo uma copia da lista 
b[2] = 4
print(f'Lista a: {a}')
print(f'Lista b: {b}')