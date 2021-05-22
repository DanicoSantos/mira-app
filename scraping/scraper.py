from urllib import request
from urllib.request import Request, urlopen,FancyURLopener
from bs4 import BeautifulSoup



urlpage = 'https://statusinvest.com.br/acoes/busca-avancada'

request = Request(urlpage, headers={'User-Agent': 'Mozilla/5.0'})
open_page = urlopen(request)

html = open_page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
print(soup.get_text())
