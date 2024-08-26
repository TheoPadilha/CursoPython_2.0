# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.



# totidade = 0
# mais_velho = 0
# media_idade = 0
# for c in range(1,3):
#     print(f'---- {c}ª PESSOA ----')
#     nome = str(input(f'Nome: ')).capitalize()
#     idade = int(input(f'Idade: '))
#     sexo = str(input(f'Sexo [M/F] ')).capitalize()
#     totidade += idade

# media_idade = totidade / 4  
# print(f'A media de idade do grupo foi de {idade :.1f} anos')

# if sexo == 'M':
#     if c == 1:
#         mais_velho = idade
#     else:
#         if idade > mais_velho:
#             mais_velho = idade
# print(f'O homem mais velho se chama {nome} e tem {idade}.')





totidade = 0
mais_velho = 0
media_idade = 0
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    print(f'---- {c}ª PESSOA ----')
    nome = str(input(f'Nome: ')).capitalize()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F] ')).capitalize()
    totidade += idade
    
    if c == 1 and sexo == 'M':
         mais_velho = idade
         nomevelho = nome
    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nomevelho = nome
    
    if sexo == 'F' and idade < 20:
        totmulher20 += 1
         
media_idade = totidade / 4  
print(f'A media de idade do grupo foi de {media_idade :.1f} anos')
print(f'O homem mais velho se chama {nomevelho} e tem {mais_velho} anos de idade.')
print(f'No total tem {totmulher20} mulheres menor de 20 anos no grupo')