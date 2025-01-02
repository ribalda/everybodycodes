import sys


def find_rune(rune, line):
    idx = 0
    out = set()
    while True:
        p = line[idx:].find(rune)
        if p == -1:
            return out
        out |= set(range(idx + p, idx + p + len(rune)))
        idx += p + 1


def transposed_lines(lines):
    out = []
    for i in range(len(lines[0].strip())):
        txt = ""
        for j in range(len(lines)):
            txt += lines[j][i]
        out += [txt]
    return out


words, text = sys.stdin.read().split("\n\n")

words = words.strip()[6:].split(",")
lines = text.splitlines()
tlines = transposed_lines(lines)

out = set()

for word in words:
    for rune in (word, word[::-1]):
        for i, line in enumerate(lines):
            ext_line = line + line[0 : len(rune) - 1]
            pos = find_rune(rune, ext_line)
            for p in pos:
                out.add((i, p % len(line)))
        for i, line in enumerate(tlines):
            pos = find_rune(rune, line)
            for p in pos:
                out.add((p, i))

print("Part 3:", len(out))
