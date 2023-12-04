input = open('../inputs/day4').read()

cards = [l.split('|') for l in input.splitlines()]
winning = [c[0].split()[2:] for c in cards]
have = [c[1].split() for c in cards]
copies = [1 for _ in cards]

pt1 = 0
for i in range(len(cards)):
    both = {int(c) for c in winning[i]} & {int(c) for c in have[i]}
    pt1 += 2**(len(both)-1) if len(both)>0 else 0
    for j in range(len(both)):
        copies[i+j+1] += copies[i]

print(pt1)
print(sum(copies))
