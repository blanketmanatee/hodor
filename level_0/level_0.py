#!/usr/bin/python3


import requests

url = 'http://158.69.76.135/level0.php'
id = 1844
time = 1024

for vote in range(time):
    requests.post(url, data={'id': id, 'holdthedoor': 'submit'})
    