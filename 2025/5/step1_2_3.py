import sys


def quality(tree):
    return int("".join([str(x[1]) for x in tree]))


def add_number(tree, n):
    for i in range(len(tree)):
        if n < (tree[i][1]) and tree[i][0] == None:
            tree[i] = (n, tree[i][1], tree[i][2])
            return tree
        if n > (tree[i][1]) and tree[i][2] == None:
            tree[i] = (tree[i][0], tree[i][1], n)
            return tree
    return tree + [(None, n, None)]


def make_tree(numbers):
    tree = []
    for n in numbers:
        tree = add_number(tree, n)

    return tree


def tree_val(tree, id):
    out = []
    out.append(quality(tree))
    for level in tree:
        out.append(int("".join(str(x) for x in level if x)))
    out.append(id)
    return tuple(out)


def process_line(line):
    id, numbers = line.split(":")
    numbers = tuple(map(int, numbers.split(",")))
    return tree_val(make_tree(numbers), int(id))


def swords_checkshum(swords):
    swords = list(swords)
    swords.sort(reverse=True)
    return sum([(idx + 1) * sword[-1] for idx, sword in enumerate(swords)])


swords = tuple(map(process_line, sys.stdin.readlines()))

quals0 = tuple(x[0] for x in swords)
print("Step 1:", quals0[0])
print("Step 2:", max(quals0) - min(quals0))

print("Step 3:", swords_checkshum(swords))

# 30477500
