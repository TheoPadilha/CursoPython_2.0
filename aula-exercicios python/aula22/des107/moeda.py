# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(n,t):
        res = n + (n*t/100)
        return res


def diminuir(n,t):
    res = n - (n*t/100) 
    return res


def dobro(n):
    res = n*2
    return res


def metade(n):
    res = n/2
    return res
    
