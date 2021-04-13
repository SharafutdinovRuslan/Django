from bs4 import BeautifulSoup
import requests


html = requests.get('https://wikipedia.org/').text
soup = BeautifulSoup(html, 'lxml')
tags = soup('a', 'other-project-link')

print([tag['href'] for tag in tags])
