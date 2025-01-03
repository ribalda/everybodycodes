import sys
from functools import cache


def parse_faces(faces_txt, n_ins):
    faces_txt = faces_txt.splitlines()
    faces = []
    for i in range(n_ins):
        face = []
        for j in range(len(faces_txt)):
            aux = faces_txt[j][4 * i : 4 * i + 3]
            if aux == "" or aux[0] == " ":
                break
            face += [(aux)]

        faces += [tuple(face)]
    return tuple(faces)


def run(faces, offset, inst):
    out = []
    for i, ins in enumerate(inst):
        out += [(offset[i] + ins) % len(faces[i])]
    return tuple(out)


def get_top(faces, offsets):
    out = []
    for i, offset in enumerate(offsets):
        out += [faces[i][offset]]
    return out


def get_value(top):
    top = [x[0] + x[-1] for x in top]
    top = "".join(top)
    tokens = set(top)
    out = 0
    for t in tokens:
        out += max(0, top.count(t) - 2)
    return out


def get_cycle(faces, inst):
    coin = 0
    out = [0]
    offsets = tuple([0] * len(inst))
    while True:
        offsets = run(faces, offsets, inst)
        top = get_top(faces, offsets)
        coin += get_value(top)
        out += [coin]
        if sum(offsets) == 0:
            return out


def left_lever(faces, offsets, inc):
    out = []
    for i, o in enumerate(offsets):
        out += [(o + inc) % len(faces[i])]
    return tuple(out)


@cache
def get_op(faces, inst, offsets, nrun, op):
    if nrun == 0:
        return 0
    vals = []
    for inc in (-1, 1, 0):
        new_offsets = left_lever(faces, offsets, inc)
        new_offsets = run(faces, new_offsets, inst)
        top = get_top(faces, new_offsets)
        val = get_value(top)
        val += get_op(faces, inst, new_offsets, nrun - 1, op)
        vals.append(val)
    return op(vals)


ins, faces = sys.stdin.read().split("\n\n")
ins = tuple(map(int, ins.split(",")))
faces = parse_faces(faces, len(ins))

offsets = tuple([0] * len(ins))
for _ in range(100):
    offsets = run(faces, offsets, ins)

print("Step 1:", " ".join(get_top(faces, offsets)))

big_n = 202420242024
cycle = get_cycle(faces, ins)
out = (big_n // (len(cycle) - 1)) * cycle[-1]
out += cycle[big_n % (len(cycle) - 1)]
print("Step 2:", out)

sys.setrecursionlimit(10000)
n_runs = 256
offsets = tuple([0] * len(ins))
max_val = get_op(faces, ins, offsets, n_runs, max)
min_val = get_op(faces, ins, offsets, n_runs, min)
print("Step 3:", max_val, min_val)
