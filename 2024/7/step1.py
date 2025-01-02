import sys


def calc_power(devices, steps):
    out = dict()
    for d in devices:
        total = 0
        p = 10
        for i in range(steps):
            op = devices[d][i % len(devices[d])]
            if op == "+":
                p += 1
            elif op == "-":
                p -= 1
            elif op == "=":
                p = p
            else:
                print(Error)
            total += p
        out[d] = total
    return out


devices = dict()
for line in sys.stdin.readlines():
    name, ops = line.strip().split(":")
    devices[name] = ops.split(",")

power = calc_power(devices, 10)
ranking = "".join(
    x[1] for x in sorted(((v, k) for k, v in power.items()), reverse=True)
)
print("Step 1:", ranking)
