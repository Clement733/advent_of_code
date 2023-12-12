import itertools

def day16():
    bottles = list(map(int, open('../inputs/day17', 'r').read().strip().split('\n')))
    total = 0
    for i in range(len(bottles)):
        subtotal = 0
        for combination in itertools.combinations(bottles, i):
            if sum(combination) == 150:
                subtotal += 1
        total += subtotal
        print (subtotal)
    print (total)

day16()
