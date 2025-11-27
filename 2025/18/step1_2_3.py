import sys
import z3


def get_plant(data):
    plants = data.split("\n\n")
    out = dict()
    for plant in plants:
        o = dict()
        plant = plant.splitlines()
        _, num, _, _, thick = plant[0].split(" ")
        num, thick = int(num), int(thick[:-1])
        o["thickness"] = thick
        br = dict()
        for branch in plant[1:]:
            branch = branch.split(" ")
            if len(branch) == 6:
                br[None] = int(branch[-1])
            else:
                br[int(branch[4])] = int(branch[-1])
        o["branches"] = br
        out[num] = o
    return out


def get_testcases(data):
    data = data.splitlines()
    return tuple(map(lambda x: tuple(map(int, x.split())), data))


def find_light(node, plant):
    out = 0
    for pl, val in plant[node]["branches"].items():
        if pl == None:
            out += val
        else:
            out += find_light(pl, plant) * val
    if out < plant[node]["thickness"]:
        return 0
    return out


def part2(testcases, last, plant):
    out = 0
    for test in testcases:
        for i, val in enumerate(test):
            plant[i + 1]["branches"] = {None: val}
        out += find_light(last, plant)
    return out


def get_max_val(last, plant):
    todo = [last]
    unk = 0
    visited = set()

    s = z3.Optimize()
    while todo:
        p = todo.pop()
        if p in visited:
            continue
        visited.add(p)
        branches = plant[p]["branches"]
        z3_br_list = []
        if None in branches:
            z3_unk = z3.Int(f"unk{unk}")
            unk += 1
            z3_br_list.append(z3_unk)
            s.add(z3_unk >= 0)
            s.add(z3_unk <= 1)
        else:
            for br, v in branches.items():
                z3_br = z3.Int(f"plant{br}") * v
                z3_br_list.append(z3_br)
                todo.append(br)
        z3partial = z3.Int(f"partial{p}")
        s.add(z3partial == sum(z3_br_list))
        z3plant = z3.Int(f"plant{p}")
        s.add(z3plant == z3.If(z3partial >= plant[p]["thickness"], z3partial, 0))

    h = s.maximize(z3.Int(f"plant{last}"))
    s.check()
    return h.value().as_long()


def part3(testcases, last, plant):
    maxv = get_max_val(last, plant)
    out = 0
    for test in testcases:
        for i, val in enumerate(test):
            plant[i + 1]["branches"] = {None: val}
        temp = find_light(last, plant)
        if temp > 0:
            out += maxv - temp
    return out


inp = sys.stdin.read().split("\n\n\n")

plant = get_plant(inp[0])
last = list(plant)[-1]
print("Step 1:", find_light(last, plant))

if len(inp) == 1:
    sys.exit(0)
testcases = get_testcases(inp[1])

print("Step 2:", part2(testcases, last, plant))
print("Step 3:", part3(testcases, last, plant))
