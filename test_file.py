from bs4 import BeautifulSoup
import requests
import re
import pprint


if __name__ == '__main__':
    vendor_code = 'T0064282203801'
    url = f'https://www.alltime.ru/search/?NAME={vendor_code}'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    print(page.status_code)
    link = soup.find('a', class_='catalog-item-link', href=True).get('href')
    print(f'{link=}')

    #tag = soup.findAll('div', class_='catalog-item', k='1')
    #print(tag)


    #print(soup.findAll('div', class_='catalog-items'))
    #itemListElement

