import sys
from collections import deque


def get_wheel(lines):
    wheel = deque([1])
    nums = map(get_range, lines)
    p = 0
    for i, r in enumerate(nums):
        if (i % 2) == 1:
            for v in r:
                wheel.appendleft(v)
                p += 1
        else:
            for v in r:
                wheel.append(v)
    wheel.rotate(-p)
    return wheel


def get_range(line):
    if "-" not in line:
        return range(int(line), int(line) + 1)
    a, b = map(int, line.split("-"))
    assert a <= b
    return range(a, b + 1)


def get_wheel_ranges(lines):
    wheel = deque([range(1, 1 + 1)])
    length = 1
    p = 0
    nums = map(get_range, lines)
    for i, r in enumerate(nums):
        length += len(r)
        if (i % 2) == 1:
            wheel.appendleft(r[::-1])
            p += len(r)
        else:
            wheel.append(r)

    return wheel, length, p


def get_value_at(wheel, length, offset, pos):
    pos += offset
    pos %= length
    for r in wheel:
        l = len(r)
        if pos >= l:
            pos -= l
            continue
        return r[pos]

    return None


lines = sys.stdin.readlines()

wheel, length, offset = get_wheel_ranges(lines)
print("Step 1", get_value_at(wheel, length, offset, 2025))
print("Step 2", get_value_at(wheel, length, offset, 20252025))
print("Step 3", get_value_at(wheel, length, offset, 202520252025))

print()

wheel = get_wheel(lines)
print("Step 1", wheel[2025 % len(wheel)])
print("Step 2", wheel[20252025 % len(wheel)])
print("Step 3", wheel[202520252025 % len(wheel)])
