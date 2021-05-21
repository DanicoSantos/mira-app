import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

urlpage = 'https://statusinvest.com.br/acoes/busca-avancada'
print(urlpage)
driver = webdriver.Firefox()
driver.get(urlpage)
driver.execute_script("")
time.sleep(30)
driver.quit()