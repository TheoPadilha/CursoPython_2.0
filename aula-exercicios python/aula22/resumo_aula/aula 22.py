from meu_modulo import numeros

num= int(input('Digite um número: '))
resp = numeros.fatorial(num)
print(f'O fatorial de {num} eh {resp}')
print(f'O dobro de {num} eh {numeros.dobro(num)}')

# 1. Importando um módulo inteiro
import math
resultado = math.sqrt(16)
print(resultado)  # Saída: 4.0

# 2. Importando partes específicas de um módulo
from math import sqrt
resultado = sqrt(25)
print(resultado)  # Saída: 5.0

# 3. Renomeando módulos ou funções
import math as m
resultado = m.factorial(5)
print(resultado)  # Saída: 120

from math import sqrt as raiz
resultado = raiz(36)
print(resultado)  # Saída: 6.0

# 4. Criando seu próprio módulo (salvar este código em meu_modulo)
# def saudacao(nome):
#     return f"Olá, {nome}!"

# 5. Usando seu próprio módulo
import meu_modulo
mensagem = meu_modulo.saudacao("Theo")
print(mensagem)  # Saída: Olá, Theo!

# 6. Explorando módulos padrão
import random
numero_aleatorio = random.randint(1, 100)
print(numero_aleatorio)

# 7. Instalando e usando módulos externos
# (Executar no terminal ou prompt de comando)
# pip install requests

import requests
response = requests.get('https://api.github.com')
print(response.status_code)
