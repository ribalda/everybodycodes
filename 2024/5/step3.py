import sys


def to_const(rows):
    return tuple(map(tuple, rows))


def do_insert(row, val):
    pos = val - 1
    pos %= len(row) * 2
    if pos > len(row):
        pos = len(row) - pos
    row.insert(pos, val)


def get_head(rows):
    return int("".join([str(x[0]) for x in rows]))


def cycle(rows, step):
    r = step % len(rows)
    do_insert(rows[(r + 1) % len(rows)], rows[r][0])
    rows[r] = rows[r][1:]


rows = []
for i in range(4):
    rows.append([])
for l in sys.stdin.readlines():
    for i, v in enumerate(l.split()):
        rows[i].append(int(v))

i = 0
visited = set()
maxval = 0
while True:
    cycle(rows, i)
    i += 1
    maxval = max(get_head(rows), maxval)
    const_rows = to_const(rows)
    if const_rows in visited:
        print("Step 3:", maxval, i)
        break
    visited.add(const_rows)
