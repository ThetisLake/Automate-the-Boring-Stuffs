import pprint

message = 'This is a test counter of the characters in the said sentence'
count={}

for ch in message.upper():
    count.setdefault(ch,0)
    count[ch]+=1

pprint.pprint(count)
