import itertools
import numpy as np

def day17():
    bottles = list(map(int, open('../inputs/day17', 'r').read().strip().split('\n')))
    total = 0
    for i in range(len(bottles)):
        subtotal = 0
        for combination in itertools.combinations(bottles, i):
            if sum(combination) == 150:
                subtotal += 1
        total += subtotal
    return total

day17()

def min_c():
    cont = list(map(int, open('../inputs/day17', 'r').read().strip().split('\n')))
    total = 150
    min_containers = float('inf')
    count_min_combinations = 0

    for i in range(1 << len(cont)):
        current_sum = 0
        current_containers = []
        for j in range(len(cont)):
            if (i & (1 << j)) != 0:
                current_sum += cont[j]
                current_containers.append(cont[j])

        if current_sum == total:
            if len(current_containers) < min_containers:
                min_containers = len(current_containers)
                count_min_combinations = 1
            elif len(current_containers) == min_containers:
                count_min_combinations += 1

    return count_min_combinations

result = min_c()
print("Number of combinations with minimum containers:", result)
