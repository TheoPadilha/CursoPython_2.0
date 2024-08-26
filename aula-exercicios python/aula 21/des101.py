# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro 
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import datetime
    ano_Atual = datetime.now().year
    idade = ano_Atual - ano
    r = idade
    if r < 16:
        r = 'NÃO VOTA'
        return (f'Com {idade} anos: {r}')
         
    if r >= 18 and r < 60:
        r = 'VOTO OBRIGATÓRIO'
        return (f'Com {idade} anos: {r}')
    
    if r >= 60 or r in [16,17]:
        r = 'VOTO OPCIONAL'
        return (f'Com {idade} anos: {r}')
        
        
resp = int(input('Em que ano você nasceu: '))
print(voto(resp))

# def voto(ano):
#     from datetime import datetime
#     ano_Atual = datetime.now().year
#     idade = ano_Atual - ano
#     r = idade
#     if r < 16:
#         r = 'NÃO VOTA'
#         print(f'com {idade} anos: {r}')
#         return r
        
#     if r >= 18 and r < 60:
#         r = 'VOTO OBRIGATÓRIO'
#         print(f'com {idade} anos: {r}')
#         return r
    
#     if r >= 60 or r in [16,17]:
#         r = 'VOTO OPCIONAL'
#         print(f'com {idade} anos: {r}')
#         return r
        
        
# resp = int(input('Em que ano você nasceu: '))
# voto(resp)



# CHAT MELHOROU
# from datetime import datetime

# def voto(ano):
#     ano_atual = datetime.now().year
#     idade = ano_atual - ano
    
#     if idade < 16:
#         status = 'NÃO VOTA'
#     elif 18 <= idade < 60:
#         status = 'VOTO OBRIGATÓRIO'
#     else:  # Inclui as idades 16, 17 e 60+
#         status = 'VOTO OPCIONAL'
    
#     print(f'Com {idade} anos: {status}')
#     return status
        
# resp = int(input('Em que ano você nasceu: '))
# voto(resp)
