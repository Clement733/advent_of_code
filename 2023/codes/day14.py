with open('../inputs/day14') as f:
    lines = f.read().split('\n')

total = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == 'O':
            ny = y
            lines[ny][x].replace('O', '.')
            while ny >= 0 and lines[ny][x] == '.':
                ny -= 1
            lines[ny+1][x].replace('.', 'O')
            total += len(lines) - y

print(total)
