import sys


def find_paths(tree):
    todo = [["RR"]]
    solutions = []
    while todo:
        path = todo.pop(0)
        if path[-1] not in tree:
            continue
        for p in tree[path[-1]]:
            if p in path:
                continue
            new_path = path + [p]
            if p == "@":
                solutions.append(new_path)
                continue
            todo.append(new_path)
    return solutions


def find_unique(paths):
    i = 0
    while i < len(paths):
        if len(paths[i]) != len(paths[i + 1]):
            return paths[i]
        i = i + 1
        while len(paths[i]) == len(paths[i - 1]):
            i += 1

    return paths[-1]


tree = dict()
for line in sys.stdin.readlines():
    name, nodes = line.strip().split(":")
    nodes = nodes.split(",")
    tree[name] = nodes

paths = find_paths(tree)
unique_path = find_unique(paths)
print("Part 1:", "".join(unique_path))
print("Part 2,3:", "".join([x[0] for x in unique_path]))
