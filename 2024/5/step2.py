import sys
from collections import defaultdict


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
values = defaultdict(int)
while True:
    cycle(rows, i)
    i += 1
    head = get_head(rows)
    values[head] += 1
    if values[head] == 2024:
        break

print("Step 1:", head * i)
