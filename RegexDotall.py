#! Python3

import re

# Caret (^) means the RegEx has to be in the beginning of the string
beginsWithHelloRegex=re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello there!'))
print(beginsWithHelloRegex.search('Hi-Hello there!'))

# Dollar ($) means the RegEx has be at the end of the string
endsWithWorldRegex = re.compile(r'World!$')
print(endsWithWorldRegex.search('Hello World!'))
print(endsWithWorldRegex.search('Hello World'))

# Dot (.) means any character except for new line
atRegex=re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

atRegex2=re.compile(r'.{1,2}at')
print(atRegex2.findall('The cat in the hat sat on the flat mat.'))

# Dot-Star (.*) expands across many characters except for new line
sentence = 'First Name: Eric Last Name: Oh'
nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(sentence))

# pass ',re.DOTALL' after the regular expression pattern to make . to include \n
prime='Serve the public trust.\nProtect the innocent.\nUphold the law.'
dotStar=re.compile(r'.*')
dotAllStar=re.compile(r'.*',re.DOTALL)
print(dotStar.search(prime))
print(dotStar.findall(prime))
print(dotAllStar.search(prime))
print(dotAllStar.findall(prime))

# pass 're.IGNORECASE' to ignore the regular expression lower/upper case
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('AEIOU aeiou AEIOU aeiou'))
vowelRegex2 = re.compile(r'[aeiou]',re.IGNORECASE)
print(vowelRegex2.findall('AEIOU aeiou AEIOU aeiou'))

# .* is greedy. .*? is non greedy
serve = '<<To serve humans> for dinner.>'
greedy = re.compile('<(.*)>')
nongreedy = re.compile('<(.*?)>')
print(greedy.findall(serve))
print(nongreedy.findall(serve))


