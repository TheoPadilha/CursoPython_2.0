# Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area():
    print('Controle de terrenos')
    print('---------------------')
    largura_terreno = float(input('Largura do terreno (m): '))
    comprimento_terreno = float(input('Comprimento do terreno (m): '))
    area = largura_terreno*comprimento_terreno
    print(f'A área de um terreno {largura_terreno} x {comprimento_terreno} é de {area}m²')
    

area()

# Guanabara

# def area(larg, comp):
#     a = larg * comp
#     print(f'A área de um terreno {larg} x {comp} é de {a}m²')
    
  # programa inicial
# print('Controles de terrenos')
# print('---------------------')
# l = float(input('Largura do terreno (m): '))
# c = float(input('Comprimento do terreno (m): '))
# area(l,c)



