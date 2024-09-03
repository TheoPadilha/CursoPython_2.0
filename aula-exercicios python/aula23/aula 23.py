# Exemplo básico de tratamento de exceção
try:
    a = 10
    b = 0
    resultado = a / b
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

# Múltiplos blocos except para diferentes tipos de exceções
try:
    a = 10
    b = "zero"
    resultado = a / b
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except TypeError:
    print("Erro: Operação inválida entre tipos diferentes.")

# Usando else e finally
try:
    a = 10
    b = 2
    resultado = a / b
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
else:
    print(f"Resultado é {resultado}.")
finally:
    print("Fim da operação.")

# Criando uma exceção personalizada
class MinhaExcecao(Exception):
    pass

try:
    raise MinhaExcecao("Isso é uma exceção personalizada.")
except MinhaExcecao as e:
    print(e)

# Lista de Exceções Comuns
try:
    # IndexError: acesso a índice inexistente em lista
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Erro: Índice fora do alcance da lista.")

try:
    # KeyError: acesso a chave inexistente em dicionário
    dicionario = {'nome': 'Theo'}
    print(dicionario['idade'])
except KeyError:
    print("Erro: Chave não encontrada no dicionário.")

try:
    # ValueError: valor inadequado para uma operação ou função
    numero = int("abc")
except ValueError:
    print("Erro: Valor inválido para conversão para inteiro.")

try:
    # TypeError: operação com tipos de dados incompatíveis
    resultado = "10" + 5
except TypeError:
    print("Erro: Tipos de dados incompatíveis.")

try:
    # FileNotFoundError: tentativa de abrir um arquivo inexistente
    with open('arquivo_inexistente.txt', 'r') as file:
        conteudo = file.read()
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")

print('='*20)

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except ZeroDivisionError:
    print('Não eh possivel dividir um número por zero ')
except (TypeError,ValueError):
    print('Tivemos um problema com os tipos de dados que você digitou. ')
except Exception as erro:
    print(f'Ocorreu um erro! ERRO: {erro.__cause__}')
else:
    print(f'O resultado eh {r:.2f}')
finally:
    print('Programa encerrado.')
    