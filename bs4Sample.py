# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 01:25:30 2020

@author: erich
"""

import bs4, requests, re

# Grab Price Span
headers1 = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
url1 = r'https://www.bestbuy.ca/en-ca/product/dell-27-fhd-75hz-8ms-gtg-ips-led-freesync-gaming-monitor-se2719hr-piano-black-silver/14398509'
res=requests.get(url1,headers=headers1)
res.raise_for_status()

soupObject = bs4.BeautifulSoup(res.text,'html.parser')
element1 = soupObject.select('#root > div > div > div.x-page-content.container_3Sp8P > div.x-product-detail-page > div.row_1Rbqw > div.col-xs-12_1GBy8.col-sm-6_9CRts.col-md-4_2WnBH.collapseColContainer_ueBNu > div.pricingContainer_25k3c > div.productPricingContainer_3gTS3 > span:nth-child(2) > span')

element1[0].text

# Parse to get price
#priceRegex = re.compile(r'\$\d\d\d.\d\d')
#testPrice = priceRegex.search(str(element1))

print(testPrice[0])