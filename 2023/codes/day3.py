import re
text = open('../inputs/day3').readlines()

n = []

for i, j in enumerate(text):
    n.append(r'.\.+')
    for l, c in enumerate(j):
        if c.isdigit() and
