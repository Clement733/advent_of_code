import sys
from itertools import permutations

text = open('../inputs/day9')

places = set()
distances = dict()
for line in text:
    (source, _, dest, _, dist) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest] = int(dist)
    distances.setdefault(dest, dict())[source] = int(dist)

shortest = sys.maxsize
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)

print("Longest is: ", longest)
print("Shortest is: ", shortest)
