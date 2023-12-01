import re

text = open('../inputs/day1')

print(sum((d:=re.findall(r'\d', s)) and int(d[0]+d[-1]) for s in text))
print(sum(d[0]*10+d[-1]for d in[[n%9+1 for i in range(len(l))for n,w in enumerate("one two three four five six seven eight nine 1 2 3 4 5 6 7 8 9".split())if l[i:i+len(w)]==w]for l in text]))
