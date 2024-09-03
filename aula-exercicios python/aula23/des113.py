# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError,ValueError):
            print('\033[;31mERRO! Digite um número interio válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[;31mO usuário não quis preencher o campo\033[m.')
            return 0
        else:
            return n
        
        
def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[;31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[;31mO usuário não quis preencher o campo\033[m.')
            return 0
        else:
            return n

num = leiaint('Digite um número inteiro: ')
num2 = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {num2}')