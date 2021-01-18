#!/usr/bin/python3


import requests
import BeautifulSoup

url = 'http://158.69.76.135/level2.php'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.content, features="lxml")
results = soup.find('span', {'id': 'Results'}).text
print(results)
