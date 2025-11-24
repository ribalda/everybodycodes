import sys
from heapq import *


def make_map(ins):
    lines, cols = set(), set()
    d2c = {
        "L": complex(0, 1),
        "R": complex(0, -1),
    }
    d, pos = complex(-1, 0), complex(0, 0)

    if ins[0][0] == "L":
        cols.add((complex(0, -1), complex(0, -1)))
    else:
        cols.add((complex(0, 1), complex(0, 1)))

    for i in ins:
        lr, n = d2c[i[0]], int(i[1:])
        d *= lr
        new_pos = pos + d * n

        if d.imag:
            lines.add((pos, new_pos))
        else:
            cols.add((pos, new_pos))

        pos = new_pos
    return lines, cols, pos


def available_knots(pos, lines, cols, end):
    # Crossing cols
    left, right = None, None
    for col in cols:
        a, b = col[0].real, col[1].real
        a, b = min(a, b), max(a, b)
        c = col[1].imag
        if pos.real >= a and pos.real <= b:
            if c < pos.imag:
                if (left == None) or c > left:
                    left = c
            if c > pos.imag:
                if (right == None) or c < right:
                    right = c

    # Crossing lines
    top, bottom = None, None
    for line in lines:
        a, b = line[0].imag, line[1].imag
        a, b = min(a, b), max(a, b)
        c = line[1].real
        if pos.imag >= a and pos.imag <= b:
            if c < pos.real:
                if (top == None) or c > top:
                    top = c
            if c > pos.real:
                if (bottom == None) or c < bottom:
                    bottom = c
    for col in cols:
        for c in (col[1].imag - 1, col[1].imag + 1):
            if ((left == None) or c > left) and ((right == None) or c < right):
                yield complex(pos.real, c)

    for line in lines:
        for l in (line[1].real - 1, line[1].real + 1):
            if ((top == None) or l > top) and ((bottom == None) or l < bottom):
                yield complex(l, pos.imag)

    if ((top == None) or end.real > top) and ((bottom == None) or end.real < bottom):
        yield complex(end.real, pos.imag)

    if ((left == None) or end.imag > left) and ((right == None) or end.imag < right):
        yield complex(pos.real, end.imag)

    step_diff = abs(end.real - pos.real) + abs(end.imag - pos.imag)
    if step_diff == 1:
        yield complex(end.real, end.imag)

    return


def find_dist(lines, cols, end):
    dummy = 0
    todo = []
    visited = set()
    heappush(todo, (0, dummy, complex(0, 0)))
    while todo:
        step, _, pos = heappop(todo)
        if pos in visited:
            continue
        visited.add(pos)
        if pos == end:
            return step
        for new_pos in available_knots(pos, lines, cols, end):
            step_diff = abs(new_pos.real - pos.real) + abs(new_pos.imag - pos.imag)
            dummy += 1
            heappush(todo, (step + int(step_diff), dummy, new_pos))

    return None


ins = tuple(sys.stdin.readline().split(","))

lines, cols, end = make_map(ins)

print("Step 1,2,3:", find_dist(lines, cols, end))
