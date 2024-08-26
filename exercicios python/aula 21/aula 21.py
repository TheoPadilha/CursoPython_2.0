# ===INTERACTIVE HELP===
# O Python possui um sistema de ajuda interativo que pode ser acessado usando a função `help()`.
# Ele exibe a documentação de uma função ou objeto, incluindo como usá-los e quais são seus parâmetros.

help(input)  # Mostra a documentação da função `input`

# ===========================================================

# ===DOCSTRING===
# Uma docstring é uma string de documentação que fica logo após a definição da função.
# Ela é usada para descrever o propósito da função, seus parâmetros e o que a função faz.
# Ao chamar `help()` em uma função, a docstring é exibida.

print(input.__doc__)  # Exibe a docstring da função `input`

def contador(i, f, p):
    """Faz uma contagem e mostra na tela.

    Args:
        i (int): Início da contagem
        f (int): Final da contagem
        p (int): Passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('.')

# Exemplo de uso da função `contador`:
contador(2, 10, 2)  # Faz uma contagem de 2 até 10, pulando de 2 em 2

# O `help()` também pode ser usado para exibir a docstring de funções que você mesmo cria.
help(contador)

# ===========================================================

# ===PARÂMETROS OPCIONAIS===
# Funções podem ter parâmetros opcionais, que assumem valores padrão se não forem especificados.
# Isso permite chamar a função com menos argumentos do que o número total de parâmetros.

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}')

# Exemplos de uso da função `somar`:
somar(3, 6, 2)  # Chama a função com 3 argumentos, a soma será 11
somar(2)        # Chama a função com apenas 1 argumento, os outros dois usam os valores padrão 0, a soma será 2
somar(5, 4)     # Chama a função com 2 argumentos, o terceiro usa o valor padrão 0, a soma será 9

# ===========================================================

# ===ESCOPO DE VARIAVEIS===
# Exemplo de Escopo Global
def exemplo_global():
    print(f"A variável global x tem o valor: {x}")  # Acessa a variável global
    
x = 10  # Variável global, acessível em qualquer parte do código
exemplo_global()  # Saída: A variável global x tem o valor: 10


# Exemplo de Escopo Local
def exemplo_local():
    y = 20  # Variável local, acessível apenas dentro desta função
    print(f"A variável local y tem o valor: {y}")  # Acessa a variável local

exemplo_local()  # Saída: A variável local y tem o valor: 20
# print(y)  # Isso causaria um erro porque 'y' não está definida fora da função

# Resumo sobre escopo de variáveis:
# - Escopo global: A variável 'x' é definida fora de qualquer função e pode ser usada em qualquer lugar do código.
# - Escopo local: A variável 'y' é definida dentro da função 'exemplo_local' e só pode ser usada dentro dessa função.
def teste(b):
    a = 8
    b += 4
    c =2
    print(f'A dentro recebe {a}')
    print(f'B dentro recebe {b}')
    print(f'C dentro recebe {c}')
a = 5
teste(a)
print(f'A fora vale {a}')

# Exemplo de uso da palavra-chave 'global' para alterar uma variável global dentro de uma função

# Variável Global
a = 5  # 'a' é uma variável global porque está definida fora de qualquer função

def alterar_global():
    global a  # Diz ao Python que queremos usar a variável global 'a' aqui
    print(f'Valor de "a" dentro da função antes de alterar: {a}')  # Mostra o valor de 'a' antes da alteração
    
    a = 10  # Altera o valor da variável global 'a' para 10
    print(f'Valor de "a" dentro da função após alterar: {a}')  # Mostra o valor de 'a' após a alteração

# Mostra o valor de 'a' antes de chamar a função
print(f'Valor de "a" antes de chamar a função: {a}')  # Espera-se 5

# Chama a função que altera a variável global
alterar_global()  # A função muda o valor de 'a' para 10

# Mostra o valor de 'a' após a função ser chamada
print(f'Valor de "a" depois de chamar a função: {a}')  # Espera-se 10

# ===========================================================

# ===RETORNO DE VARIAVEIS===

# Exemplo de retorno de variáveis em funções

def somar(a, b):
    """Soma dois números e retorna o resultado."""
    resultado = a + b  # Calcula a soma
    return resultado  # Retorna o resultado

# Chamando a função e armazenando o valor retornado em uma variável
resultado_soma = somar(5, 3)

# Mostrando o valor retornado
print(f'O resultado da soma é: {resultado_soma}')  # Saída: O resultado da soma é: 8

# +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

def calcular(a, b):
    """Calcula a soma e o produto de dois números e retorna ambos."""
    soma = a + b
    produto = a * b
    return soma, produto  # Retorna uma tupla com dois valores

# Chamando a função e armazenando os valores retornados em variáveis
resultado_soma, resultado_produto = calcular(4, 5)

# Mostrando os valores retornados
print(f'A soma é: {resultado_soma}')       # Saída: A soma é: 9
print(f'O produto é: {resultado_produto}')  # Saída: O produto é: 20
