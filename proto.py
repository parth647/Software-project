import re
f=open('email.txt')
strToSearch=""
for line in f:
    strToSearch+= line

print(strToSearch)

datFinder= re.compile('on the date \d{2}\.\d{2}\.\d{4}',re.IGNORECASE)
date=re.compile('\d{2}\.\d{2}\.\d{4}',re.IGNORECASE)
finddat=re.search(datFinder,strToSearch)
print("    \n  ")

if(finddat):
    print(finddat.group())
    datestring=finddat.group()
    finddate=re.search(date,datestring)
    print(finddate.group())

else:
    print('Date not found')

