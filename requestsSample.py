# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:59:31 2020

@author: erich
"""

import requests

# requests module
res = requests.get(r'http://automatetheboringstuff.com/files/rj.txt')
statusCode = res.status_code
print(statusCode)
print(res.text[:500])

# raise_for_status
res2 = requests.get(r'http://google.com/fakelinkfakelinkfakelink')
res.raise_for_status() # used res. so it doesn't bug out


playFile = (open('romeoAndJuliet.txt','wb'))

for chunk in res.iter_content(100000):
        playFile.write(chunk)

playFile.close()

