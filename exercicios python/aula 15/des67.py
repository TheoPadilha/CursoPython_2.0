# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

cont = 0
while True:
    num = int(input('Qual a tabuada: '))
    if num <= 0:
        break
    print('+=+=+=+=++=+=+=+=')
    while cont <= 10:
        print(f'{cont} x {num} = {cont*num}')
        cont += 1
    print('=+=+=+=+=+=+==+=+')
    cont = 0  
print('Fim do programa')
        

# Guanabara

# while True:
#     num = int(input('Qual a tabuada: '))
#     if num <= 0:
#         break
#     print('+=+=+=+=++=+=+=+=')
#     for c in range(1 , 11):
#         print(f'{num} x {c} = {num*c}')   
#     print('=+=+=+=+=+=+==+=+')
# print('Fim do programa')
        
