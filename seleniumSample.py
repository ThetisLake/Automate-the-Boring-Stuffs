# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:33:07 2020

@author: erich
"""

# Syntax requires importing as below
from selenium import webdriver

# Open a new browser and get a requested website
browser1 = webdriver.Edge()
browser1.get(r'https://www.google.com/')

# Interact the opened browser element
browser1.back()
browser1.forward()
browser1.refresh()

# Create element by finding elements (more on this in the note)
element1 = browser1.find_element_by_css_selector('#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

# Interact with the element identified
element1.send_keys(r'LoLo Pien')
element1.submit()

# Download Text
element2 = browser1.find_element_by_css_selector(r'#rso > div:nth-child(1) > div > div.s > div > span')
print(element2.text)

# Download the entire page
element3 = browser1.find_element_by_css_selector(r'html')
print(element3.text)

# Close browser
# browser1.quit()