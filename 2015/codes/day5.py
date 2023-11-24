import re
text = open("2015/inputs/day_5")


strings = [x.strip() for x in text]

# Part 1
print(len([s for s in strings if (re.search(r'([aeiou].*){3,}', s) and
                                  re.search(r'(.)\1', s) and
                                  not re.search(r'ab|cd|pq|xy', s))]))

# Part 2
print(len([s for s in strings if (re.search(r'(..).*\1', s) and
                                  re.search(r'(.).\1', s))]))
