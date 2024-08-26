# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# tot = 0
# maior = None
# menor = None
# media = 0
# quant = 0

# num = 1
# while num != 0:
#     num = int(input('Informe um valor [0 para parar]: '))
#     tot += num
#     quant += 1
    
#     if quant == 1:
#         maior = menor = num
#     else:
#         if num > maior:
#             maior = num
#         if  num < menor:
#             menor = num
            
            
#     if num == 0:
#         continuar = str(input('Quer continuar [S/N]: ')).capitalize().strip()
#         if continuar == 'S':
#             num = int(input('Informe um valor [0 para parar]: '))
#         elif continuar == 'N':
#             break
#         else:
#             continue
# if quant > 0 :
#     media =( tot / quant )

#     print(f'Média:{media} / Valor Total:{tot} / Quantidade de nuns:{quant} / maior num:{maior} / menor num:{menor} ')
#     print('cabo')
    
    
    
    
# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = menor = tot = cont = 0
resp = "S"
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    cont += 1
    tot += num
    
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    avançar = str(input('Quer continuar [S/N]: ')).capitalize().strip()

    if avançar == 'N':
        break
    elif avançar == 'S':
        continue
    
    if avançar != 'S' or avançar != 'N':
        print('Erro, valor insirido está incorreto! Tente novamente')
        avançar = str(input('Quer continuar [S/N]: ')).capitalize().strip()
        if avançar == 'N':
            break
        if avançar == 'S':
            continue
    
media = tot / cont  
print(f'Foram insiridos {cont} valores , totalizando um total de {tot}')
print(f'A média dos valores insiridos é {media :.2f}')
print(f'O maior valor inserido foi de {maior} e o menor foi de {menor}')


# Guanabara

# resp = 'S'
# soma = quant = maior = menor = media = 0

# while resp in 'Ss':
    
#     num = int(input('Digite um valor: '))
#     soma += num
#     quant += 1
    
#     if quant == 1:
#         maior = menor = num
#     else:
#         if num > maior:
#             maior = num
#         elif num < menor:
#             menor = num
            
#     resp = str(input('Quer continuar [S/N]: ')).capitalize().strip()
# media = soma / quant
# print(f'Foram insiridos {quant} valores , resultadno em {soma}')
# print(f'A média dos valores insiridos é {media :.2f}')
# print(f'O maior valor inserido foi de {maior} e o menor foi de {menor}')