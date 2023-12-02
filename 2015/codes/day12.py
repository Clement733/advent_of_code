import sys
import re
import json

f = open("../inputs/day12")
string = f.read()
f.close()

print("Sum of all numbers 1:", sum(map(int, re.findall("-?[0-9]+", string))))

def hook(obj):
  if "red" in obj.values(): return {}
  else: return obj
stuff = str(json.loads(string, object_hook=hook))
print ("Sum of all numbers 2:", sum(map(int, re.findall("-?[0-9]+", stuff))))
