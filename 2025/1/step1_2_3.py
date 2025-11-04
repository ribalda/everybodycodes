import sys


def get_offset(ins):
    n = int(ins[1:])
    if ins[0] == "L":
        n *= -1
    return n


def calc_pos(ins, l, step):
    pos = 0

    for i in ins:
        pos += get_offset(i)
        if step == 1:
            pos = min(max(0, pos), l - 1)
        elif step == 2:
            pos %= l

    return pos


def swap_pos(ins, names):

    for i in ins:
        pos = get_offset(i)
        pos %= len(names)

        names[0], names[pos] = names[pos], names[0]
    return


names, _, ins = sys.stdin.readlines()
names = names.strip().split(",")
ins = ins.strip().split(",")

for i in range(1, 3):
    pos = calc_pos(ins, len(names), i)
    print("Step", i, names[pos])

swap_pos(ins, names)
print("Step 3", names[0])
