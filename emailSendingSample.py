# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:31:19 2020

@author: erich
"""


#SMTP = Simple Mail Transfer Protocol

import smtplib

connection = smtplib.SMTP('smtp.gmail.com',587)

print(type(connection)) # Checking type of connection

print(connection.ehlo()) # Checking connection. Anything above >200 is a go

print(connection.starttls()) # Start TLS connection to encrypt password

print(connection.login('legitbusinessn00t@gmail.com','Akb194kah073bnq'))

# Email sending syntax
connection.sendmail('legitbusinessn00t@gmail.com','Aceng1025@gmail.com','Subject: Dear Andrew..\n\n Dear Andrew \n This is a test email. \n Thanks for being such a good friend! \n Legit Business N00t')
print('email sent.')

connection.quit() # Cut connection