# Exercício  Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.
lista = []

while True:
    n = (int(input('Digie um valor: ')))
    
    if n not in lista:
        lista.append(n)
        print(f'Valor adicionado com sucesso!')
    else:
        print('Valor duplicado... Não irei adicionar à lista.')
        
    while True:
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()
        if resp in ['S', 'N']:
            break
        elif resp != ['S' , 'N']:
            print('Entrada inválida. Por favor, insira "S" para sim ou "N" para não.')
    
    if resp == 'N':
        break
    
    
        
print(f'Você digitou os valores {sorted(lista)}')