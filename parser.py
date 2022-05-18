import requests
from bs4 import BeautifulSoup

url = 'https://readrate.com/rus/news'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
post = soup.find('div', class_='container news-post')
title = post.find('a', class_='title-link d-block my-sm-2').text.strip()
describe = post.find('div', class_='subtitle d-none d-sm-block').text.strip()
url = post.find('a', class_='title-link d-block my-sm-2', href=True)['href'].strip()


print(title, describe, url, sep='\n\n')