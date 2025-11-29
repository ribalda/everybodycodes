import sys
from collections import deque


def get_triangle(lines):
    world = dict()
    height = len(lines)
    start, end = None, None

    for x, line in enumerate(lines):
        for y, v in enumerate(line.strip()):
            pos = complex(height - x - 1, y - height + 1)
            if v == ".":
                continue
            if v == "S":
                v = "T"
                start = pos
            elif v == "E":
                v = "T"
                end = pos
            world[pos] = v
    return world, start, end, height


def neighbours(pos, is_part3=False):
    yield pos + 1j
    yield pos - 1j
    ab = (pos.real + abs(pos.imag)) % 2
    if ab == 0:
        yield pos + 1
    else:
        yield pos - 1
    if is_part3:
        yield pos


def part1(triangle):
    conns = set()
    for pos in triangle:
        if triangle[pos] != "T":
            continue
        for new_pos in neighbours(pos):
            if triangle.get(new_pos, "None") == "T":
                a, b = (pos.real, pos.imag), (new_pos.real, new_pos.imag)
                conns.add((min(a, b), max(a, b)))
    return len(conns)


def rotate_tri(height):
    out = dict()
    for i in range(height):
        first_line = height - i - 1
        for j in range(2 * i + 1):
            line = first_line + (j + 1) // 2
            col = line - j
            out[complex(i, j - i)] = complex(line, col)
    return out


def part2_3(triangle, start, end, height, is_part3=False):
    todo = deque([])
    dummy = 0
    todo.append((0, dummy, start))
    visited = set()
    if is_part3:
        rot = rotate_tri(height)
    while todo:
        steps, _, pos = todo.popleft()
        if pos == end:
            return steps
        if pos in visited:
            continue
        visited.add(pos)
        if is_part3:
            pos = rot[pos]
        for new_pos in neighbours(pos, is_part3):
            if triangle.get(new_pos, "None") != "T":
                continue
            dummy += 1
            todo.append((steps + 1, dummy, new_pos))


triangle, start, end, height = get_triangle(sys.stdin.readlines())

print("Part 1", part1(triangle))
print("Part 2", part2_3(triangle, start, end, height))
print("Part 3", part2_3(triangle, start, end, height, True))
