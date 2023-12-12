with open('../inputs/day12') as f:
    lines = f.readlines()
lines = [e.strip().split() for e in lines]
print(lines)

def getcount(memo, line, counts, pos, current_count, countpos):
      key = (pos, current_count, countpos)
      if key in memo:
            return memo[key]
      if pos == len(line):
            ret = 1 if len(counts) == countpos else 0
      elif line[pos] == '#':
            ret = getcount(memo, line, counts, pos + 1, current_count + 1, countpos)
      elif line[pos] == '.' or countpos == len(counts):
            if countpos < len(counts) and current_count == counts[countpos]:
                  ret = getcount(memo, line, counts, pos + 1, 0, countpos + 1)
            elif current_count == 0:
                  ret = getcount(memo, line, counts, pos + 1, 0, countpos)
            else:
                  ret = 0
      else:
            hash_count = getcount(memo, line, counts, pos + 1, current_count + 1, countpos)
            dot_count = 0
            if current_count == counts[countpos]:
                  dot_count = getcount(memo, line, counts, pos + 1, 0, countpos + 1)
            elif current_count == 0:
                  dot_count = getcount(memo, line, counts, pos + 1, 0, countpos)
            ret = hash_count + dot_count
      memo[key] = ret
      print(memo)
      return ret

s1 = 0
for row in lines:
      counts = [int(x) for x in row[1].split(',')]
      s1 += getcount({}, row[0] + '.', counts, 0, 0, 0)
print(s1)

s2 = 0
for row in lines:
      counts = [int(x) for x in row[1].split(',')] * 5
      s2 += getcount({}, (row[0] + '?') * 4 + row[0] + '.', counts, 0, 0, 0)
print(s2)
