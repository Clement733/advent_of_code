import re
text = open('../inputs/day2')
input_text = text.read()

sum(int(gid[5:]) for gid, res in [g.strip().split(": ") for g in open("../inputs/day2").readlines()] if sum(1 for cnt, cl in [d.split() for d in res.replace(";", ",").split(", ")] if (cl == "blue" and int(cnt) > 14) or (cl == "green" and int(cnt) > 13) or (cl == "red" and int(cnt) > 12)) < 1)
sum(max(int(cnt) for cnt, cl in [d.split() for d in res.replace(";", ",").split(", ")] if cl == "red") * max(int(cnt) for cnt, cl in [d.split() for d in res.replace(";", ",").split(", ")] if cl == "blue") * max(int(cnt) for cnt, cl in [d.split() for d in res.replace(";", ",").split(", ")] if cl == "green") for gid, res in [g.strip().split(": ") for g in open("../inputs/day2").readlines()])
