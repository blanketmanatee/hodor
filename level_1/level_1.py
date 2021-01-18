#!/usr/bin/python3


import requests
from http import cookies

url = 'http://158.69.76.135/level1.php'
id = 1844
time = 4096

for votes in range(time):
    passValues = {'id': '1844', 'holdthedoor': 'Submit', 'key': 'freshCookie'}
    kookies = {'HoldTheDoor': 'freshCookie'}
    r = requests.post(url, data=passValues, cookies=kookies)
    print(r.status_code)
    print('done')
