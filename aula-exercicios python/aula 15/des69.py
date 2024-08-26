# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

print('Cadastramento')
pessoa = pessoa18 = homens = mulher20 = 0
p = 1
while True:
    print('-=-=-=-=-=-=-=-=-=')
    print(f'{p}ª Pessoa')
    p += 1
        
    idade = int(input('Idade: '))
    if idade > 18:
        pessoa18 += 1
    while True:   
        sexo = str(input('Sexo [M/F]: ')).capitalize().strip()
        if sexo in ['M', 'F']:
            break
        print('Entrada inválida. Por favor, insira "M" para masculino ou "F" para feminino.')
        
    if sexo == 'M':
        homens += 1
    if sexo == 'F':
        if idade < 20:
            mulher20 += 1
    
    pessoa += 1
    print('-=-=-=-=-=-=-=-=-=')
    while True:
        avançar = str(input('Quer continuar [S/N]: ')).capitalize().strip()
        if avançar in ['S' , 'N']:
            break
        print('Entrada inválida. Por favor, insira "S" para sim ou "N" para não.')
    
    if avançar == 'N':
        break
print(' ')
print(f'Número de pessoas cadastradas foi de {pessoa}.')
print(f'Tem {pessoa18} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {homens} homens')
print(f'Tem {mulher20} Mulheres menor de 20 anos.')



# Guanabara

# tot18 = totH = totM20 = 0
# while True:
#     idade = int(input('Idade: '))
#     sexo = ' '
#     while sexo not in 'MF':
#         sexo = str(input('Sexo [M/F]: ')).capitalize().strip()
        
#     if idade > 18:
#         tot18 += 1
    
#     if sexo == 'M':
#         totH += 1
    
#     if sexo == 'F' and idade < 20:
#         totM20 += 1
        
#     avançar = ' '
#     while avançar not in 'SN':
#         avançar = str(input('Quer continuar [S/N]: ')).capitalize().strip()
#     if avançar == 'N':
#         break
# print(f'Tem {tot18} pessoas maiores de 18 anos.')
# print(f'Foram cadastrados {totH} homens')
# print(f'Tem {totM20} Mulheres menor de 20 anos.')