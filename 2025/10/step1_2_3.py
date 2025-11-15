import sys
from collections import deque
from functools import cache


def parse_mapa(lines):
    out = set()
    sheeps = set()
    hides = set()
    start_pos = None
    for x, line in enumerate(lines):
        for y, val in enumerate(line.strip()):
            pos = complex(x, y)
            out.add(pos)
            if val == "D":
                start_pos = pos
            elif val == "S":
                sheeps.add(pos)
            elif val == "#":
                hides.add(pos)
    return start_pos, sheeps, hides, out


def jumps():
    yield complex(-2, -1)
    yield complex(-2, 1)
    yield complex(-1, -2)
    yield complex(-1, 2)
    yield complex(1, -2)
    yield complex(1, 2)
    yield complex(2, -1)
    yield complex(2, 1)


def calc_movements(mapa, pos, steps):
    out = set()

    for p in pos:
        for j in jumps():
            next_pos = p + j
            if next_pos not in mapa:
                continue
            out.add(next_pos)
            if steps != 1:
                out |= calc_movements(mapa, set([next_pos]), steps - 1)

    return out


def move_sheeps(sheeps):
    out = set()
    for s in sheeps:
        out.add(s + complex(1, 0))
    return out


def debug_map(mapa, dragons, hides, sheeps):
    print()
    for i in range(100):
        if complex(i, 0) not in mapa:
            break
        out = ""
        for j in range(100):
            pos = complex(i, j)
            if pos not in mapa:
                break
            if pos in hides:
                out += "#"
                continue
            if pos in dragons:
                out += "D"
                continue
            if pos in sheeps:
                out += "S"
                continue
            out += "."
        print(out)
    print()


def step1(start_pos, sheeps, mapa, steps):
    valid_moves = calc_movements(mapa, set([start_pos]), steps)
    return len(valid_moves & sheeps)


def step2(start_pos, sheeps, hides, mapa, steps):
    n_sheeps = len(sheeps)
    dragon_pos = set([start_pos])
    for _ in range(steps):
        dragon_pos = calc_movements(mapa, dragon_pos, 1)
        unsafe_sheeps = sheeps - hides
        sheeps -= unsafe_sheeps & dragon_pos
        sheeps = move_sheeps(sheeps)
        unsafe_sheeps = sheeps - hides
        sheeps -= unsafe_sheeps & dragon_pos
    return n_sheeps - len(sheeps)


def step3_slow(start_pos, sheeps, hides, mapa):
    todo = deque([(start_pos, sheeps, True)])
    out = 0
    while todo:
        dragon, sheeps, is_sheep = todo.pop()
        if is_sheep:
            done_move = False
            for s in sheeps:
                new_s = s + complex(1, 0)
                if new_s == dragon and new_s not in hides:
                    continue
                done_move = True
                if new_s not in mapa:
                    continue
                next_sheeps = sheeps.copy()
                next_sheeps.remove(s)
                next_sheeps.add(new_s)
                todo.append((dragon, next_sheeps, False))
            if not done_move:
                todo.append((dragon, sheeps, False))
        else:
            for j in jumps():
                next_dragon = dragon + j
                if next_dragon not in mapa:
                    continue
                next_sheeps = sheeps.copy()
                if next_dragon in next_sheeps and next_dragon not in hides:
                    next_sheeps.remove(next_dragon)
                if len(next_sheeps) == 0:
                    out += 1
                    print(out)
                    continue
                todo.append((next_dragon, next_sheeps, True))

    return out


@cache
def step3(sheep_turn, dragon, sheeps):
    sheeps = set(sheeps)
    out = 0
    if sheep_turn:
        done_move = False
        for s in sheeps:
            new_s = s + complex(1, 0)
            if new_s == dragon and new_s not in hides:
                continue
            done_move = True
            if new_s not in mapa:
                continue
            next_sheeps = sheeps.copy()
            next_sheeps.remove(s)
            next_sheeps.add(new_s)
            out += step3(False, dragon, frozenset(next_sheeps))
        if not done_move:
            out += step3(False, dragon, frozenset(sheeps))
    else:
        for j in jumps():
            next_dragon = dragon + j
            if next_dragon not in mapa:
                continue
            next_sheeps = sheeps.copy()
            if next_dragon in next_sheeps and next_dragon not in hides:
                next_sheeps.remove(next_dragon)
            if len(next_sheeps) == 0:
                out += 1
                continue
            out += step3(True, next_dragon, frozenset(next_sheeps))
    return out


start_pos, sheeps, hides, mapa = parse_mapa(sys.stdin.readlines())

print("Step 1:", step1(start_pos, sheeps, mapa, 4))
print("Step 2:", step2(start_pos, sheeps, hides, mapa, 20))
print("Step 3:", step3(True, start_pos, frozenset(sheeps)))
