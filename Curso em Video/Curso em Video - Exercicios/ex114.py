import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://movitel.co.mz/')
except urllib.error.URLError:
    print('O site nao esta acessivel no momento!')
else:
    print('Consegui acessar o site com sucesso')
