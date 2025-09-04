import re
s='ANANA'
print(len(re.findall('(?=ANA)', s)))