'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidades de notas
    - A maior nota
        - A menor nota
            - A média da turma 
                - A situação(opcional)
'''
        
def notas(*n, sit=False):
    """_summary_

    Args:
        sit (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    d = {}
    d['Total'] = len(n)
    d['Maior'] = max(n)
    d['Menor'] = min(n)
    d['Média'] = sum(n) / len(n)
    if sit:
        if d['Média'] == 10:
            d['Situação'] = 'EXELENTE'
        elif d['Média'] >= 7:
            d['Situação'] = 'BOA'
        elif d['Média'] >= 5:
            d['Situação'] = 'RASOAVEL'
        else:
            d['Situação'] = 'RUIM' 
    return d
        
        
        
resp = notas(10,10,10,10,sit=True)
print(resp)
help(notas)
