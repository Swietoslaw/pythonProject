from requests import get
from bs4 import BeautifulSoup
import csv

www = 'https://www.bankier.pl/gielda/wiadomosci/komunikaty-spolek'
page = get(www)
bs = BeautifulSoup(page.content, 'lxml')

for espi in bs.find_all('span', class_='entry-title'):
    href = espi.find('a')
    file = 'https://www.bankier.pl' + href['href']
    print('https://www.bankier.pl' + href['href'])
    

with open('espi.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow('file')

