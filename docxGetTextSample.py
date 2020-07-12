# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:24:50 2020

@author: erich
"""


import docx

def getText(filename):
    doc=docx.Document(filename)
    fullText = []
    for p in doc.paragraphs:
        fullText.append(p.text)
    return '\n'.join(fullText)

print(getText(r'C:\Users\erich\Desktop\Python\Sample Resume 2.docx'))