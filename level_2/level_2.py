#!/usr/bin/python3


import requests
from http import cookies

url = 'http://158.69.76.135/level2.php'
id = 1844
time = 1024
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

for votes in range(time):
    passValues = {'id': '1844', 'holdthedoor': 'Submit', 'key': ''}
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    r = requests.get(url, headers=headers)
    r = requests.post(url, data=passValues, headers=headers)
