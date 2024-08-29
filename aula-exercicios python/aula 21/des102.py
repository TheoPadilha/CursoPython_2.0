# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# def fatorial(n,show=False):
#     resultado = 1
#     calculo = ''
#     for i in range(2, n + 1):
#         resultado *= i
#     if show :                     
#         for x in range(n,1,-1):
#             calculo += f'{x} x '  
#         calculo +=(f'1 = {resultado}.')
#         return calculo
#     return resultado


# print(fatorial(5 ,True)) # Mude o show para (True ou False) e veja a diferença.



# GUANABARA

def fatorial(n, show=False):
    """Conta fatorial

    Args:
        n= o numero do fatorial que vamos calcular.
        show : Eh pra mostrar as conta que foi feita ou so o resultado.
    """
    f = 1 
    for c in range(n , 0 , -1):
        if show:
            print(c , end='')
            if c> 1:
                print(f' x ',end='')
            else:
                print(f' = ',end='')
        f *= c
    return f

print(fatorial(9,True))
help(fatorial)