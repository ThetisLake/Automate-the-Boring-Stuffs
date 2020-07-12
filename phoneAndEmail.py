#! python3

import re, pyperclip

# Create a regex for phone numbers
# Note: Group of Groups return tuple with multiple items so must use for loop to separate it
phoneRegex=re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext.12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?   # 2 types of area code (optional)
(\s|-)?             # first separator
(\d\d\d             # first 3 digits
-                   # separator
\d\d\d\d)           # large 4 digits
(((ext(\.)?\s)|x)   # extension word-part(optional)
(\d{1,5}))?         # extension number-part(optional)
)
''',re.VERBOSE)

# Create a regex for email addresses
emailRegex=re.compile(r'''
# some.+_thing@something.com
[a-zA-Z0-9_.+]+         # name part
@                       # @ symbol
[a-zA-Z0-9_.+]+         # domain name
''',re.VERBOSE)

# Get the text off of the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers=[]
for phoneNumbers in extractedPhone:
    allPhoneNumbers.append(phoneNumbers[0])
print(allPhoneNumbers)
print(extractedEmail)

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers)+'\n'+'\n'.join(extractedEmail)
pyperclip.copy(results)
