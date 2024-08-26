# Dicionários em Python
  
    # Acessar e Modificar Valores
dados = {'nome': 'Theo', 'idade': 25}
print(dados['nome'], dados['idade'])
dados['idade'] = 26  # Modificando o valor da chave 'idade'

# Adicionar e Remover Itens
dados['Sexo'] = 'M'  # Adicionando um novo par chave-valor
print(dados)
del dados['idade']  # Removendo um item do dicionário

# Métodos Úteis
anime = {
    'Titulo': 'Jujutsu Kaisen',
    'Ano': '2020',
    'Personagem_principal': 'Yuji Itadori'
}
print(anime.values())  # Retorna todos os valores do dicionário
print(anime.keys())    # Retorna todas as chaves do dicionário
print(anime.items())   # Retorna uma lista de tuplas (chave, valor)

# Iterando sobre um Dicionário
for t, m in anime.items():
    print(f'{t} é {m}')  # Itera sobre as chaves e valores  
    # O primiro item ,nesse exemplo o (t) é oq vale as keys que ficam antes dos :.('keys':'values')

# Compreensão de Dicionários
quadrados = {x: x*x for x in range(6)}  # Criando um dicionário usando compreensão
print(quadrados)

# Métodos Úteis
pessoa = {'nome': 'Theo', 'idade': 19, 'sexo': 'M'}
print(pessoa.get('nome', 'Não encontrado'))  # Acessando valor com .get(), retorna 'Não encontrado' se a chave não existir
pessoa.pop('idade', None)  # Remove a chave 'idade' e retorna seu valor, ou None se a chave não existir

# Mergindo Dicionários (Python 3.9+)
novo_dicionario = dados | pessoa  # Mesclando dois dicionários
print(novo_dicionario)

# Verificação de Chaves
if 'nome' in dados:
    print('A chave "nome" existe em dados')  # Verifica se a chave existe no dicionário

# Exemplo Completo
pessoa = {'nome': 'Theo', 'idade': 19, 'sexo': 'M'}
pessoa['nome'] = 'MIH'  # Modificando um valor existente
pessoa['peso'] = 60     # Adicionando um novo par chave-valor
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos e pesa {pessoa["peso"]} kg')

for chave, valor in pessoa.items():
    print(f'{chave}: {valor}')  # Itera sobre as chaves e valores do dicionário


brasil = []
estado1 = {'uf':'Santa Catarina' , 'sigla':'SC'}
estado2 = {'uf':'São Paulo' , 'sigla':'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])
print(brasil[1])

estado = dict()
brasil = list()

for x in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) # .copy() Copia o dicionário e adiciona à lista
    
for e in brasil:
    for a,b in e.items():
        print(f'O campo {a} tem o valor {b}')
        
for e in brasil:
    for v in e.values():
        print(f'a cidade eh {v}', end=' ')
        print()