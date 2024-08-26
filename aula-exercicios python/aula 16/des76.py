# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, 
# na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

itens = ('Lapis', 3.00, 'Mouse' , 50.00, 'teclado' , 149.90,'Controle' , 10.99 ,'controle ps4', 80.00, 'caderno' , 25.00,
         'Cadeira gamer', 1290.00)

print('='*32)
print(f'{'Listagem de preços':^32}')
print('='*32)

for pos in range(0 , len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<20}', end=' ')
    else:
        print(f'R${itens[pos]:>8.2f}')
        
print('='*32)
