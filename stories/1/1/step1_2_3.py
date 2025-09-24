import sys
from collections import deque


def eni(n, exp, mod):
    v = 1
    out = ""
    for _ in range(exp):
        v *= n
        v %= mod
        out = str(v) + out

    return int(out)


def eni2(n, exp, mod, size):
    v = 1
    out = []
    for _ in range(exp):
        v *= n
        v %= mod
        out = [v] + out

    out = out[:size]
    return int("".join(map(str, out)))


def eni2_opt(n, exp, mod, size):
    v = 1
    out = deque([])
    for i in range(exp):
        v *= n
        v %= mod
        if v in out and len(out) > size:
            out.rotate(exp - i)
            break
        out.appendleft(v)

    out = list(out)[:size]
    return int("".join(map(str, out)))


def get_tail_middle(out, v):
    tail = deque([])
    while out[-1] != v:
        tail.append(out.pop())
    return tail, out


def eni3(n, exp, mod):
    v = 1
    out = deque([])
    out_v = set()
    for _ in range(exp):
        v *= n
        v %= mod
        if v in out_v:
            total_n = exp
            s = 0

            tail, middle = get_tail_middle(out, v)
            s = sum(tail)
            total_n -= len(tail)

            s += (total_n // len(middle)) * sum(middle)
            total_n %= len(middle)

            middle.rotate(total_n)
            s += sum(list(middle)[:total_n])
            return s
        out.appendleft(v)
        out_v.add(v)

    return sum(out)


lines = sys.stdin.readlines()

max_val = 0
for line in lines:
    a, b, c, x, y, z, m = map(lambda x: int(x[2:]), line.split())
    max_val = max(max_val, eni3(a, x, m) + eni3(b, y, m) + eni3(c, z, m))
print("Step 3:", max_val)

max_val = 0
for line in lines:
    a, b, c, x, y, z, m = map(lambda x: int(x[2:]), line.split())
    max_val = max(
        max_val, eni2_opt(a, x, m, 5) + eni2_opt(b, y, m, 5) + eni2_opt(c, z, m, 5)
    )
print("Step 2 opt:", max_val)

max_val = 0
for line in lines:
    a, b, c, x, y, z, m = map(lambda x: int(x[2:]), line.split())
    max_val = max(max_val, eni2(a, x, m, 5) + eni2(b, y, m, 5) + eni2(c, z, m, 5))
print("Step 2:", max_val)

max_val = 0
for line in lines:
    a, b, c, x, y, z, m = map(lambda x: int(x[2:]), line.split())
    max_val = max(max_val, eni(a, x, m) + eni(b, y, m) + eni(c, z, m))
print("Step 1:", max_val)
