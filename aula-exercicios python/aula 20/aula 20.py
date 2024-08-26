# FUNÇÕES EM PYTHON PART 1

# Função para mostrar uma linha de divisória
# Útil para criar divisões visuais no terminal
def mostralinha():
    print(20*'-')

mostralinha()
print('Abacaxi')
mostralinha()

# Função que exibe uma mensagem centralizada com uma borda de linhas
# Boa para destacar informações importantes no terminal
def mensagem(msg):
    print(30*'-')
    print(msg)
    print(30*'-')

mensagem('alunos')

# Exemplo comentado de uso repetido da função 'mensagem'
# para entradas fornecidas pelo usuário.
# for x in range(0, 3):
#     mensagem(str(input('Titulo: ')))

# Função que soma dois números e exibe o resultado
# Exemplo simples de uso de parâmetros e operações dentro da função
def soma(a, b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(f'A soma deu {s}')
    print('-'*20)

soma(3, 2)
soma(0, 9)
soma(4, 7)

# Função que conta quantos números foram passados como argumento
# Mostra a flexibilidade de argumentos variáveis (*num)
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')

contador(4, 4, 64, 3)
contador(3, 2, 6)
contador(2)

# Função que dobra os valores de uma lista
# Esta função altera a lista original, multiplicando cada elemento por 2
def dobra(e):
    pos = 0
    while pos < len(e):
        e[pos] *= 2
        pos += 1

# Exemplo de uso da função 'dobra'
valores = [4, 9, 9, 4, 2, 3, 22]
print(f'Antes: {valores}')  # Exibe os valores antes de serem dobrados
dobra(valores)
print(f'Depois: {valores}')  # Exibe os valores após serem dobrados

# Função que soma todos os valores passados como argumento
# Uma variação interessante da função 'soma' anterior, mas agora somando múltiplos números
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}') 

soma(6, 3, 4)
soma(4, 3, 2)
