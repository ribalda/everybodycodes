import sys
from collections import Counter


def yield_cros(pos, start, end):
    for col in range(start[1], end[1]):
        if col != pos[1]:
            yield (pos[0], col)
    for line in range(start[0], end[0]):
        if line != pos[0]:
            yield (line, pos[1])


def get_cros(lines, pos, start, end):
    letters = ""
    for p in yield_cros(pos, start, end):
        letters += lines[p[0]][p[1]]
    return letters


def set_cros(lines, pos, start, end, new_val):
    for p in yield_cros(pos, start, end):
        v = lines[p[0]][p[1]]
        if v == "?":
            lines[p[0]][p[1]] = new_val


def find_border(lines, pos, start, end):
    letters = get_cros(lines, pos, start, end)

    count = Counter(letters)
    if count["."] > 0:
        return None
    del count["?"]
    singles = [x for x in count if count[x] == 1]
    if len(singles) != 1:
        return None
    return singles[0]


def find_val(lines, pos, start, end):
    ver_vals = list()
    for col in start[1], start[1] + 1, start[1] + 6, start[1] + 7:
        v = lines[pos[0]][col]
        ver_vals += [v]
    hor_vals = list()
    for line in start[0], start[0] + 1, start[0] + 6, start[0] + 7:
        v = lines[line][pos[1]]
        hor_vals += [v]

    cros_val = set(hor_vals) & set(ver_vals)
    if len(cros_val) == 1:
        v = cros_val.pop()
        if v != "?":
            lines[pos[0]][pos[1]] = v
            return True

    all_vals = ver_vals + hor_vals
    if all_vals.count("?") == 1:
        xval = find_border(lines, pos, start, end)
        if not xval:
            return None
        lines[pos[0]][pos[1]] = xval
        set_cros(lines, pos, start, end, xval)
        return True


def fill_word(lines, start, end):
    work_done = False
    for x in range(start[0] + 2, end[0] - 2):
        for y in range(start[1] + 2, end[1] - 2):
            v = lines[x][y]
            if v != ".":
                continue
            val = find_val(lines, (x, y), start, end)
            if val != None:
                work_done = True
    return work_done


def find_power(lines, start):
    out = 0
    i = 0
    for x in range(start[0] + 2, start[0] + 6):
        for y in range(start[1] + 2, start[1] + 6):
            i += 1
            v = lines[x][y]
            if v == ".":
                return 0
            out += (ord(v) - ord("A") + 1) * i
    return out


def get_runics_pos(lines):
    start_line = 0
    end_line = start_line + 8
    while end_line <= len(lines):
        start_col = 0
        end_col = start_col + 8
        while end_col <= len(lines[0]):
            yield ((start_line, start_col), (end_line, end_col))
            start_col += 6
            end_col = start_col + 8
        start_line += 6
        end_line = start_line + 8


lines = sys.stdin.read().splitlines()
lines = list(map(list, lines))

work_done = True
while work_done:
    work_done = False
    for pos in get_runics_pos(lines):
        work_done |= fill_word(lines, pos[0], pos[1])

# out = "\n".join(["".join(x) for x in lines])
# print(out)

out = 0
for pos in get_runics_pos(lines):
    out += find_power(lines, pos[0])
print("Step 3:", out)
