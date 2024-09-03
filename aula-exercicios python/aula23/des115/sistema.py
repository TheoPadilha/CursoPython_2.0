from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'curso.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','sair'])
    if resp == 1:
        # Opção de listar o conteudo de um arquivo.
        lerArquivo(arq)
    elif resp == 2:
        # Cadastrar um a nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).title().strip()
        idade = leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resp == 3:
        # Sair do sistema
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[0m')
    sleep(1.5)
