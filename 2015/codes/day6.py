import numpy as np

text = open("2015/inputs/day6")

def first():
    grid = np.zeros((1000, 1000), dtype = int)
    for line in text:
        words = line.split(' ')
        coords = line.split(' ')[-3:]
        x_st, y_st = map(int, coords[0].split(','))
        x_e, y_e = map(int, coords[2].split(','))
        if words[1] == 'on':
            grid[x_st:x_e+1, y_st:y_e+1] = 1
        elif words[1] == 'off':
            grid[x_st:x_e+1, y_st:y_e+1] = 0
        elif words[0] == 'toggle':
            grid[x_st:x_e+1, y_st:y_e+1] ^= 1
    print(np.sum(grid))

def second():
    grid = np.zeros((1000, 1000), dtype = int)
    for line in text:
        words = line.split(' ')
        coords = line.split(' ')[-3:]
        x_st, y_st = map(int, coords[0].split(','))
        x_e, y_e = map(int, coords[2].split(','))
        if words[1] == 'on':
            grid[x_st:x_e+1, y_st:y_e+1] += 1
        elif words[1] == 'off':
            grid[x_st:x_e+1, y_st:y_e+1] = np.maximum(grid[x_st:x_e + 1, y_st:y_e + 1] - 1, 0)
        elif words[0] == 'toggle':
            grid[x_st:x_e+1, y_st:y_e+1] += 2

    print(np.sum(grid))

second()
