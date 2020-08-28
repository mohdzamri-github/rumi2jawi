from typing import Dict

f = open('rumi-jawi-unicode.txt')

rjDict: Dict[str,str] = {}
for l in f:
    l = l.strip()
    r, j = l.split(',')
    if r not in rjDict:
        rjDict[r] = j
    else:
        if rjDict[r] == j:
            print(r,"same spelling")
