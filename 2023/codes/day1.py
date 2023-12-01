import re

text = open('../inputs/day1')

n = []


for line in text:
    to = []
    t = []
    if 'one' in line:
        line = line.replace('one', '1')
    if 'two' in line:
        line = line.replace('two', '2')
    if 'three' in line:
        line = line.replace('three', '3')
    if 'four' in line:
        line = line.replace('four', '4')
    if 'five' in line:
        line = line.replace('five', '5')
    if 'six' in line:
        line = line.replace('six', '6')
    if 'seven' in line:
        line = line.replace('seven', '7')
    if 'eight' in line:
        line = line.replace('eight', '8')
    if 'nine' in line:
        line = line.replace('nine', '9')
    for c in line:
        if c.isnumeric():
            t.append(c)
            to = [t[0], t[-1]]
            to = ''.join(to)
            to = int(to)

    n.append(to)
    print(n)
print(n[51])
print(sum(n))
