import pandas as pd
import requests
import bs4 as BeautifulSoup

url = 'https://tanvir-anzum.web.app'
page = requests.get(url)
pageContent = page.content
soup= BeautifulSoup.BeautifulSoup(page.content, 'html.parser')
link_list = soup.find_all('a')

for link in link_list:
    if 'href' in link.attrs:
        print(str(link.attrs['href']+'\n'))

