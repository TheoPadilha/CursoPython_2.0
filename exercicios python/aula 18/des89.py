# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# lista = []
# dados = []
# while True:
#     nome = str(input('Nome do aluno: ')).title()
#     n1 = float(input('1ª Nota: '))
#     n2 = float(input('2ª Nota: '))
#     dados.append(nome)
#     dados.append(n1)
#     dados.append(n2)
#     lista.append(dados[:])
    
#     media = (n1 + n2 ) / 2
#     dados.append(media)
    
#     while True:
#         resp = str(input('Quer continuar [S/N]: ')).upper().strip()
#         if resp in 'SN':
#             break
#         if resp != ['S' ,'N']:
#             print('Entrada invalida ,Digite "S" para sim e "N" para não.')
#     if resp == 'N':
#         break
# print(30*'=+')
# cont = 1
# print(lista)
# print(dados)
    
    
ficha =[]
while True:
    nome = str(input('Nome do aluno: ')).title()
    n1 = float(input('1ª Nota: '))
    n2 = float(input('2ª Nota: '))
    media = (n1 + n2 ) / 2
    ficha.append([nome, [n1,n2] , media])
    
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()
        if resp in 'SN':
            break
        if resp != ['S' ,'N']:
            print('Entrada invalida ,Digite "S" para sim e "N" para não.')
    if resp == 'N':
        break
    
print(30*'=-')
print(f'{'No.':<4}{'NOME':<10}{'MEDIA':>8}')
print(26*'=')

for i , z in enumerate(ficha):
    print(f'{i:<4}{z[0]:<10}{z[2]:>8.1f}')
while True:
    print('='*26)
    opc = int(input('Quer ver as notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Programa finalizado')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}' )
    