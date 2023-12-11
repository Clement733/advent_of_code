from itertools import combinations, accumulate

with open('../inputs/day11') as f:
    data = f.read().split()

g = [(x,y) for y,r in enumerate(data)
           for x,c in enumerate(r) if c == '#']

def dist(ps):
    *exp, = accumulate((l, 1)[p in ps] for p in range(max(ps)+1))
    return sum(abs(exp[a]-exp[b]) for a,b in combinations(ps, 2))

for l in 2, 1_000_000: print(sum(map(dist, zip(*g))))
