from math import sqrt, floor, ceil
from functools import reduce
with open('../inputs/day6') as ff:
    lines = [line.strip() for line in ff.readlines()]

times = list(map(int,lines[0].split(':')[1].strip().split()))
distances = list(map(int,lines[1].split(':')[1].strip().split()))

def findroots(t,d):
    x1, x2 = (t - sqrt(t**2-4*d))/2, (t + sqrt(t**2-4*d))/2
    x1, x2 = ceil(min(max(min(x1,x2),0),t)), floor(min(max(max(x1,x2),0),t))
    return x2 - int(-x2**2 + t*x2 == d) - x1 - int(-x1**2 + t*x1 == d) + 1

total = reduce(lambda x,y: x*y, map(findroots, times, distances))
print(total)

newtime = int("".join(map(str,times)))
newdist = int("".join(map(str,distances)))
print(findroots(newtime,newdist))
