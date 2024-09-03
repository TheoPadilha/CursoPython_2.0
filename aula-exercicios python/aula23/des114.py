# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com')
except urllib.error.URLError:
    print('\033[31mDeu erro\033[0m')

else:
    print('\033[32mO site está acessível\033[0m')
    # print(site.read())
