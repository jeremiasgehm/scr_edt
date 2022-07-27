from cgitb import html
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import urllib
import urllib3
import socket
from urllib.request import urlopen

from sklearn.model_selection import train_test_split #libraries machine learning
from sklearn.linear_model import LinearRegression #Libraries machine learning

list_projects = []
html = requests.get('http://www.finep.gov.br/chamadas-publicas?situacao=aberta').content
soup = BeautifulSoup(html, 'html.parser')
abertos_finep = soup.find('div', attrs={'class': 'item'})
abertos_finep.h3.string

abertos_finep_data_de_pub = soup.find('div', attrs={'class': 'data_pub div'})
abertos_finep_prazo = soup.find('div', attrs={'class': 'prazo div'})
ab1 = abertos_finep.h3.string + abertos_finep_data_de_pub.strong.string + abertos_finep_data_de_pub.span.string + abertos_finep_prazo.strong.string + abertos_finep_prazo.span.string     
ab1

abertos_finep = soup.find('div', attrs={'class': 'item'})
#print(abertos_finep)
abertos_finep_item = abertos_finep.find_all('a')

last_links = soup.find(class_='AlphaNav')
#last_links.decompose()

abertos_finep = soup.find(class_='BodyText')
#abertos_finep_item = abertos_finep.find_all('a')

for abertos_finep in abertos_finep_item:
  names = abertos_finep.contents[0]
  print(names)
