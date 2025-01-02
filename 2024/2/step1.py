import sys

words, text = sys.stdin.read().split("\n\n")

words = words.strip()[6:].split(",")
text = text.strip()

out = 0
for w in words:
    out += text.count(w)

print("Part 1:", out)
