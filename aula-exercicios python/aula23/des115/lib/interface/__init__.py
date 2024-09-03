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


def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
    
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[0m - \033[34m{item}\033[0m')
        c+=1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[0m')

    return opc  
    