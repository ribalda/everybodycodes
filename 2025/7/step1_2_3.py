import sys
from itertools import pairwise


def get_paths(lines):
    out = dict()
    for l in lines:
        fr, to = l.strip().split(" > ")
        out[fr] = set(to.split(","))

    return out


def valid_name(name, paths):
    for f, t in pairwise(name):
        if t not in paths.get(f, set([])):
            return False

    return True


def get_names(name, path):
    out = set()
    if len(name) >= 7:
        out.add(name)

    if len(name) == 11:
        return out

    for n in paths.get(name[-1], []):
        out |= get_names(name + n, path)

    return out


def step3(names, paths):
    out = set()
    for n in names:
        out |= get_names(n, paths)
    return len(out)


names, paths = sys.stdin.read().split("\n\n")
names = names.split(",")
paths = get_paths(paths.splitlines())

good_names = list(map(lambda x: valid_name(x, paths), names))
good_names_val = [n for tf, n in zip(good_names, names) if tf]
print("Step 1:", good_names_val[0])

good_names_idx = [idx + 1 for idx, (tf, _) in enumerate(zip(good_names, names)) if tf]
print("Step 2:", sum(good_names_idx))

print("Step 3:", step3(good_names_val, paths))
