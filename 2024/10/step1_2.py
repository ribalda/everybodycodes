import sys


def find_val(lines, pos):
    letters = set()
    for col in range(len(lines[0].strip())):
        v = lines[pos[0]][col]
        if v != ".":
            if v in letters:
                return v
            letters.add(v)
    for line in range(len(lines)):
        v = lines[line][pos[1]]
        if v != ".":
            if v in letters:
                return v
            letters.add(v)


def find_word(lines):
    out = ""
    for x, line in enumerate(lines):
        for y, v in enumerate(line):
            if v == ".":
                out += find_val(lines, (x, y))
    return out


def find_power(word):
    out = 0
    for i, v in enumerate(word):
        out += (ord(v) - ord("A") + 1) * (i + 1)
    return out


def get_runics(data):
    for hor in data.split("\n\n"):
        hor = hor.splitlines()
        seps = [i for i, v in enumerate(hor[0]) if v == " "]
        seps += [len(hor[0])]
        start = -1
        for end in seps:
            out = []
            for l in hor:
                out += [l[start + 1 : end]]
            yield out
            start = end


power = 0
first = True
for runic in get_runics(sys.stdin.read()):
    word = find_word(runic)
    if first:
        print("Step 1:", word)
        first = False
    power += find_power(word)
print("Step 2:", power)
