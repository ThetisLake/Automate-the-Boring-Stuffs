import re

#Lesson on regex, compile, match object, grouping using ()
phoneNumRegEx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegEx.search('My number is 250-508-2830')
print(mo1)

#Lesson on pipe character
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batmobile lost a wheel')
print(mo2)

#Lesson on ? (Zero or One repetition)
batRegex2 = re.compile(r'Bat(wo)?man')
mo3 = batRegex2.search('The Adventures of Batman')
print(mo3)

phoneNumRegEx2 = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo4 = phoneNumRegEx2.findall('My number is 250-508-2830 but I can also be reached at 588-2260')
print(mo4)

#Lesson on * (Zero or more repetition)
batRegex3 = re.compile(r'Bat(wo)*man')
mo5 = batRegex3.search('The Adventures of Batwowowoman')
print(mo5)

#Lesson on + (One or more repetition)
batRegex4 = re.compile(r'Bat(wo)+man')
mo6 = batRegex4.search('The Adventures of Batman')
print(mo6)

#Lesson on {n} (Specifically n time repetition)
haRegex = re.compile(r'(ha){3}')
mo7 = haRegex.search('hahahaha, that is funny haha')
print(mo7)

#Lesson on {x,y} (at least x, and at most y repetition)
haRegex2 = re.compile(r'(ha){1,4}') # Greedy match seeks the longest occuring regex
mo8 = haRegex2.search('hahahaha, that is funny haha') 
print(mo8)

haRegex3 = re.compile(r'(ha){1,4}?') # Non-greedy match seeks the first occuring regex
mo9 = haRegex3.search('hahahaha, that is funny haha') 
print(mo9)

