# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
# você deve mostrar, para cada palavra, quais são as suas vogais.
palvras = ('gato' ,'cachorro' ,'pássaro', 'elefante', 'girafa','leão', 'tigre', 'cavalo', 'zebra', 'urso')


for p in palvras:
    print(f'\nNa palavra {p} temos as vogais:',end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
            
            