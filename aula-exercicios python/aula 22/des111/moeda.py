# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(n=0,t=0,form=False):
    res = n + (n*t/100)
    return res if form is False else moeda(res)


def diminuir(n=0,t=0,form=False):
    res = n - (n*t/100) 
    return res if form is False else moeda(res)


def dobro(n=0,form=False):
    res = n*2
    return res if form is False else moeda(res)


def metade(n=0,form=False):
    res = n/2
    return res if form is False else moeda(res)
    
    
def moeda(n=0,p='R$',form=False):
    res = f'{p}{n:.2f}'.replace('.',',')
    return res if form is False else moeda(res) 
tb ="  "
def resumo(n=0,t=0):
    print(30*'-')
    print('RESUMO DO VALOR'.center(30))
    print(30*'-')
    print(f'Preço analisado:{tb}{moeda(n)}')
    print(f'Dobro do preço:{tb} {dobro(n,True)}')
    print(f'Metade do preço:{tb}{metade(n,True)}')
    print(f'{t}% de aumento:{tb} {aumentar(n,t,True)}')
    print(f'{t}% de redução:{tb} {diminuir(n,t,True)}')
    print(30*'-')
    