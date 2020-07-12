# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:40:06 2020

@author: erich
"""

# Open and in write mode
helloFile = open(r'C:\Users\erich\Desktop\Python\MakeDir\openingTest.txt','w')
helloFile.write('Hello!!!!!!!!\n')
helloFile.write('Hello!!!!!!!!\n')
helloFile.write('Hello!!!!!!!!\n')
helloFile.write('Hello!!!!!!!!\n')
helloFile.close()

# Open file in write mode
baconFile=open(r'MakeDir\bacon.txt','w')
baconFile.write('Bacon is not vegetable.')
baconFile.close()

# Open file in append mode
baconFile2=open(r'MakeDir\bacon.txt','a')
baconFile2.write('\nBacon is a meat product.')
baconFile2.close()

#Saving variables in a binary shelf file
import shelve
shelfFile = shelve.open('mydata') # Creates .bak, .dat, and .dir files 
shelfFile['cats']=['Jimmy','Jjing','Whiteshoes']
print(shelfFile['cats'])
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()
