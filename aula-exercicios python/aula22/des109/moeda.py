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
