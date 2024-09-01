# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(n=0,t=0):
        res = n + (n*t/100)
        return res


def diminuir(n=0,t=0):
    res = n - (n*t/100) 
    return res


def dobro(n=0):
    res = n*2
    return res


def metade(n=0):
    res = n/2
    return res
    
def moeda(n=0):
    res = f'R${n:.2f}'
    return res