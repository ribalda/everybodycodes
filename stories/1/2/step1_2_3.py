import sys
from collections import deque


def parse_add(line):
    op, id, left, right = line.split()
    id = int(id[3:])
    left = left[6:-1].split(",")
    right = right[7:-1].split(",")
    return op, id, int(left[0]), left[1], int(right[0]), right[1]


def tree_add(root, num, letter, id):
    node = [num, letter, id, None, None]
    if root == None:
        return node

    tree = root
    while True:
        if node[0] <= tree[0]:
            if tree[-2] == None:
                tree[-2] = node
                return root
            tree = tree[-2]
            continue
        if tree[-1] == None:
            tree[-1] = node
            return root
        tree = tree[-1]


def tree_swap(tree_left, tree_right, id):

    # Left
    todo = deque([tree_left])
    while todo:
        node = todo.popleft()
        if node[2] == id:
            node_left = node
            break
        for n in node[-2], node[-1]:
            if n:
                todo.append(n)
    # Right
    todo = deque([tree_right])
    while todo:
        node = todo.popleft()
        if node[2] == id:
            node_right = node
            break
        for n in node[-2], node[-1]:
            if n:
                todo.append(n)

    for i in range(2):
        node_left[i], node_right[i] = node_right[i], node_left[i]

    return None


def tree_swap3(tree_left, tree_right, id):

    if id == 1:
        return tree_right, tree_left

    todo = deque([tree_left, tree_right])
    left_idx = None
    left_node = None
    right_idx = None
    right_node = None
    while todo and not (left_idx and right_idx):
        node = todo.popleft()
        for i in (-2, -1):
            n = node[i]
            if not n:
                continue
            if n[2] == id:
                if not left_idx:
                    left_idx = i
                    left_node = node
                else:
                    right_idx = i
                    right_node = node
            todo.append(n)

    right_node[right_idx], left_node[left_idx] = (
        left_node[left_idx],
        right_node[right_idx],
    )

    return tree_left, tree_right


def navigate_tree(tree, lines):
    todo = deque([(1, tree)])
    while todo:
        level, node = todo.popleft()
        if len(lines) <= level:
            lines.append("")
        lines[level] = lines[level] + node[1]
        for n in node[-2], node[-1]:
            if n:
                todo.append((level + 1, n))
    return lines


def get_longest_line(lines):
    out = ""
    for l in lines:
        if len(l) > len(out):
            out = l
    return out


lines = sys.stdin.readlines()

tree_left = None
tree_right = None
for l in lines:
    if l.startswith("ADD"):
        l = parse_add(l)
        tree_left = tree_add(tree_left, l[2], l[3], l[1])
        tree_right = tree_add(tree_right, l[4], l[5], l[1])
        continue
    if l.startswith("SWAP"):
        _, id = l.split()
        id = int(id)
        tree_swap(tree_left, tree_right, id)

lines_left = navigate_tree(tree_left, [""])
lines_right = navigate_tree(tree_right, [""])

print("Step 1 & 2:", get_longest_line(lines_left) + get_longest_line(lines_right))


tree_left = None
tree_right = None
for l in lines:
    if l.startswith("ADD"):
        l = parse_add(l)
        tree_left = tree_add(tree_left, l[2], l[3], l[1])
        tree_right = tree_add(tree_right, l[4], l[5], l[1])
        continue
    if l.startswith("SWAP"):
        _, id = l.split()
        id = int(id)
        tree_left, tree_right = tree_swap3(tree_left, tree_right, id)

lines_left = navigate_tree(tree_left, [""])
lines_right = navigate_tree(tree_right, [""])

print("Step 3:", get_longest_line(lines_left) + get_longest_line(lines_right))
