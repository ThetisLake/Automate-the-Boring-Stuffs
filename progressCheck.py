#! python3

import re, pyperclip

#Todo: create regex for hour and minute
hourMinute = re.compile('''
(
((\d)*hr\s?)?
((\d{1,2})min)
)
''',re.VERBOSE)

#Paste from pyperclip and organize

text=pyperclip.paste()
MO1=hourMinute.findall(text)

hours=[]
for i in MO1:
    hours.append(i[2])

minutes=[]
for j in MO1:
    minutes.append(j[4])

sumHours=0
sumMinutes=0
for i in range(0,len(hours)):
    if hours[i] == '':
        continue
    else:
        sumHours+=int(hours[i])
        
for i in range(0,len(minutes)):
    if minutes[i] == '':
        continue
    else:
        sumMinutes+=int(minutes[i])
        
#Reformat so min has max value of 59
excessHours=0
excessHours = sumMinutes/60

sumHours+=int(excessHours)
sumMinutes= (excessHours-int(excessHours))*60

summaryTime=(str(sumHours)+'hr '+ str(int(sumMinutes))+'min')

#Print summary
print(summaryTime)
